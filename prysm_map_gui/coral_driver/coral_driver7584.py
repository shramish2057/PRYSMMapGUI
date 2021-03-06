#!/usr/bin/env python
# psm.coral.env
#====================================================================

"""
Coral Proxy Driver Script

This script runs the coral model for selected location coordinates and
time period on PRYSM Map GUI. This script consists of a coral_driver function
to run the coral model for time period 1975-1984 and the passed location coordinates.
Hence, the SST and SSS datasets of 1975-1984 collected from World Ocean Atlas are used
as input datasets. 
"""

#importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import csv
import math
from psm.coral.sensor import pseudocoral
from psm.agemodels.banded import bam_simul_perturb
from psm.aux_functions.analytical_error import analytical_error
from psm.aux_functions.analytical_err_simple import analytical_err_simple
import sys

#coral driver function that takes lat & lon as parameters
def coral_driver(latitude, longitude):

    # PREPARATION OF Location Coordinates, SST, and SSS datasets
     
    #Data directory
    sstdatadir='woa018_datasets/sst/' 
    sssdatadir='woa018_datasets/sss/'
    print('Loading data from ', sstdatadir,' ...')

    #Converting latitude and longitudes to float
    lat= float(latitude)
    lon= float(longitude)

    #reading the World Ocean Atlas Sea Surface Temperature csv dataset for 1975-1984
    with open(sstdatadir+'woa18_7584_t00mn01.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # skipping the first intro lines of the data
        next(csv_reader)
        next(csv_reader)

        # Opening a new file to store the equivalent sea surface temperature datasets 
        # according to the selected location coordinates by the user at PRYSM Map GUI
        # This hence saves the sea surface temperature dataset for specific location
        # for depths ranging from 0-5500 m.
        with open(sstdatadir+'woa18_7584_sst.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter='\n')

            for line in csv_reader:
                floatlat= float(line[0])
                floatlon= float(line[1])

                if math.ceil(floatlat) == math.ceil(lat) and math.ceil(floatlon) == math.ceil(lon):
                    csv_writer.writerow(line[2:])

    #reading the World Ocean Atlas Sea Surface Salinity csv dataset for 2005-2017
    with open(sssdatadir+'woa18_7584_s00mn01.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # skipping the first intro lines of the data
        next(csv_reader)
        next(csv_reader)

        # Opening a new file to store the equivalent sea surface temperature datasets 
        # according to the selected location coordinates by the user at PRYSM Map GUI
        # This hence saves the sea surface temperature dataset for specific location
        # for depths ranging from 0-5500 m.
        with open(sssdatadir+'woa18_7584_sss.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter='\n')

            for line in csv_reader:
                floatlat= float(line[0])
                floatlon= float(line[1])

                if math.ceil(floatlat) == math.ceil(lat) and math.ceil(floatlon) == math.ceil(lon):
                    csv_writer.writerow(line[2:])
    # Load SST anomalies [K] (NOTE: THIS SHOULD BE A 1-D VECTOR OF DATA!)
    # yearly
    file = open(sstdatadir+'woa18_7584_sst.csv')
    ssta = np.loadtxt(file, delimiter=",")

    file = open(sssdatadir +'woa18_7584_sss.csv')
    sssa = np.loadtxt(file, delimiter=",")

    # setting up time axis

    time=np.arange(850,1850,1)

    print('Preparing data...')
    # 2.1 Convert Lats and Lons to standard format (if they aren't already).
    # lon: convert (-180: +180) to (0: 360)
    # lat: convert (0: 180) to (-90: +90)


    
    # making sure there are no negative-longitude coordinates: [0 to 360] only.
    # longitude
    if (lon<0.):
        lon = lon+360.

    # latitude
    if (lat>90.):
        lat = lat-90.

    # Making sure that Sea-Surface Temperature is in degrees C, not Kelvin.
    sst=ssta #AAA
    sss=sssa #AAA
    temp_flag = any(sst>200)

    for i in range(len(sst)):
        if (temp_flag):
            sst[i] = sst[i]-274.15


    # SENSOR MODEL EXECUTION

    # NOTE: THIS SHOULD BE A 1-D VECTOR OF DATA!
    print('Running sensor model...')
    coral = np.zeros(len(time))  # this will initialize a [Time x Lat x Lon] matrix of coral values.

    # calling pseudocoral function
    for i in range(len(time)):
        coral[i] = pseudocoral(lat,lon,sst[i],sss[i])

   
   # OBSERVATIONAL MODEL EXECUTION
   
    # Specify and model rate of annual layer miscount: BAM (see doctring)
    print('Running observation model...')
    X = coral
    X = X.reshape(len(X),1)
    tp, Xp, tmc=bam_simul_perturb(X,time,param=[0.02,0.02],name='poisson',ns=1000,resize=0)

    # Adding uncertainty bands based on measurement precision
    sigma=0.1 # permil, measurement  precision
    coral_upper, coral_lower = analytical_err_simple(X,sigma)

    # Gaussian Noise Model for analytical error:
    sigma=0.1
    coral_Xn=analytical_error(X,sigma)

    # Saving coral timeseries fields as numpy arrays in current directory.
    print('Saving time series...')
    print('Coral Age', coral)
    print('Simulated Coral', Xp)
    outdir='./results/'
    np.save(outdir+"simulated_coral"+str(lat)+"_d18O.npy",coral)
    np.save(outdir+"coral_age"+str(lat)+"_perturbed.npy",Xp)

if __name__ == '__main__':
    lat = sys.argv[1]
    lon = sys.argv[2]
    coral_driver(lat, lon)