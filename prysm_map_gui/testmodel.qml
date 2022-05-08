import QtLocation 5.6
import QtPositioning 5.6
import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0
import QtQuick.Controls.Universal 2.0
import QtQuick.Layouts 1.15
import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Controls 1.4


Item {
    width: 600
    height: 600

    Map {
        id: map
        anchors.fill: parent
        plugin: Plugin {
            name: "osm"
        }
        center: QtPositioning.coordinate(59.91, 10.75)
        zoomLevel: 3

        ListModel {
            id: mapModel
        }

        MapItemView {
            model: mapModel
            delegate: MapQuickItem {
                sourceItem: Rectangle {
                    width: 14
                    height: 14
                    color: "#0a541e"
                    radius: 7
                    MouseArea{
                        anchors.fill: parent
                        hoverEnabled: true
                        onEntered: {
                            popup.visible=true
                        }
                        onExited: {
                            popup.visible=false
                        }
                    }
                }
                Popup {
                    id: popup
                    width: 145
                    height: 65
                    modal: true
                    visible: false
                    contentItem: Text {
                        text: "Latitude: " + Math.round(model.lat * 100) / 100 + "\nLongitude: " + Math.round(model.longi * 100) / 100; 
                    }
                }
                anchorPoint: Qt.point(sourceItem.width/2, sourceItem.height/2)
                coordinate : QtPositioning.coordinate(lat, longi)
            }
        }

        MouseArea {
            anchors.fill: parent
            onClicked: {
                var coord = map.toCoordinate(Qt.point(mouse.x,mouse.y))
                mapModel.append({lat : coord.latitude, longi: coord.longitude});
                CSVHelper.saveListModel(mapModel, "location.csv")
                print('Latitude:'+ coord.latitude + 'Longitude:' + coord.longitude)
            }
        }

        Rectangle {
            id: button

            width: 150
            height: 30
            color: "red"
            radius: 5     // Let's round the rectangle's corner a bit, so it resembles more a button

            Text {
                id: buttonText
                text: qsTr("Clear Slected Locations")
                color: "white"
                anchors.centerIn: parent
            }

            MouseArea {
                // We make the MouseArea as big as its parent, i.e. the rectangle. So pressing anywhere on the button will trigger the event
                anchors.fill: parent

                // Exploit the built-in "clicked" signal of the MouseArea component to do something when the MouseArea is clicked.
                // Note that the code associated to the signal is plain JavaScript. We can reference any QML objects by using their IDs
                onClicked: {
                    mapModel.clear();
                }
            }
        }      
    }
}