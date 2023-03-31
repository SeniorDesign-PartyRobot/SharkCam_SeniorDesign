/////////////////////////////EXPO EXAMPLE BASE////////////////////////////////////
// https://levelup.gitconnected.com/how-to-click-images-in-react-native-using-expo-camera-for-android-1fbc1181473d
// base tutorial from here: https://medium.com/@nutanbhogendrasharma/implement-camera-in-react-native-mobile-app-part-1-ea307ce924a4
// https://www.freecodecamp.org/news/how-to-create-a-camera-app-with-expo-and-react-native/

//////////////////////////////////Test Code/////////////////////////////////////////
// Navigate between screens: https://reactnavigation.org/docs/navigating
// In App.js in a new project

import * as React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { Button, Switch, Alert, StyleSheet, TouchableOpacity } from 'react-native';
import { SelectList } from 'react-native-dropdown-select-list';
import { useState } from 'react';
import { CameraType } from 'expo-camera';
import { Camera } from 'expo-camera';
import * as Font from 'expo-font';

///////////////////// Styling //////////////////
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#01A39E'
  },
  camera: {
    flex: 1,
  },
  button: {
    alignSelf: 'flex-end',
    alignItems: 'center',
    justifyContent: 'center',
    color: '#FFFFFF'
  },
  buttonContainer: {
    flexDirection: 'row',
    backgroundColor: 'transparent',
    alignItems: 'center',
    justifyContent: 'space-evenly',

  },
  homeButtonContainer: {
    flexDirection: 'column',
    backgroundColor: '#87e0de',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: 10,
    borderRadius: 10,
    margin: 10
  },
  cameraButtonContainer: {
    flex: .9,
    flexDirection: 'row',
    backgroundColor: 'transparent',
    alignItems: 'center',
    justifyContent: 'space-evenly',
  },
  homeButtonText: {
    fontSize: 36,
    color: "#fff",
    fontWeight: "bold",
    alignSelf: "center",
    textTransform: "uppercase"
  },
  settingsButtonText: {
    fontSize: 24,
    color: "#fff",
    fontWeight: "bold",
    alignSelf: "center",
    textTransform: "uppercase"
  },
  text: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
    alignItems: 'center'
  },
  genericContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: "#01A39E",
  }
});

/////////////////// Home Screen ////////////////////////
// get data between screens: https://www.geeksforgeeks.org/how-to-pass-value-between-screens-in-react-native/
function HomeScreen({ navigation }) {
  return (
    <View style={styles.genericContainer}>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => navigation.navigate('RobotControls')}>
          <Text style={styles.homeButtonText}>{"Settings"}</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => navigation.navigate('CameraScreen')}>
          <Text style={styles.homeButtonText}>{"Camera"}</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => navigation.navigate('PhotoScreen')}>
          <Text style={styles.homeButtonText}>{"Photo Viewer"}</Text>
        </TouchableOpacity>


      </View>

    </View>
  );
}
////////////////// Robot Controls /////////////////////////////
function sendMsg(input) {
  console.log("button clicked!");
  try {
    console.log(input);
    ws.send(input);
  } catch {
    console.log("Message could not be sent");
  }

};

function RobotControls() {
  //////////// camera delay code //////////////
  var delay = 10; // default delay, even if not shown on drop down
  const [selected, setSelected] = React.useState("");
  const data = [
    { key: '1', value: '10 Seconds' },
    { key: '2', value: '15 Seconds' },
    { key: '3', value: '30 Seconds' },
  ]
  delay = parseInt(selected); // int version of selected from dropdown menu

  /////////////// auto capture code ///////////////
  const [isEnabled, setIsEnabled] = useState(false);
  const toggleSwitch = () => {
    setIsEnabled(previousState => !previousState);
  };

  return (
    <View style={styles.genericContainer}>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => sendMsg('start')}>
          <Text style={styles.settingsButtonText}>{"Start Robot"}</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => sendMsg('stop')}>
          <Text style={styles.settingsButtonText}>{"Stop Robot"}</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.homeButtonContainer}>
        <View style={styles.buttonContainer}>
          <Text style={styles.settingsButtonText}>{"Autocapture Enable"}</Text>
          <Switch
            trackColor={{ false: '#63fa05', true: '#54f542' }}
            thumbColor={isEnabled ? '#fff' : '#545353'}
            onValueChange={toggleSwitch}
            value={isEnabled}>
          </Switch>
        </View>
      </View>
      <View style={styles.homeButtonContainer}>
        <Text style={styles.settingsButtonText}>{"Autocapture Delay"}
        </Text>
        <SelectList
          boxStyles={{ backgroundColor: "#87e0de", borderRadius: 0, }}
          dropdownStyles={{ backgroundColor: "#87e0de" }}
          search={false}
          setSelected={(delay) => setSelected(delay)}
          data={data}
          save="value"
          color="#fff"
        >
        </SelectList>
      </View>
    </View >
  );
};

///////////////// Camera Screen /////////////////////////
function CameraScreen() {
  const [type, setType] = useState(CameraType.back);
  const [permission, requestPermission] = Camera.useCameraPermissions();
  const [cameraRef, setCameraRef] = useState(null);
  const [enabledRef, setEnabledRef] = useState(false);

  var enabled = true;

  function autoCaptureOnOff(enabled) {

    if (enabled) {
      setEnabledRef(true);
    }

  }

  if (!permission) {
    // Camera permissions are still loading
    return <View />;
  }

  if (!permission.granted) {
    // Camera permissions are not granted yet
    return (
      <View style={styles.container}>
        <Text style={{ textAlign: 'center' }}>We need your permission to show the camera</Text>
        <Button onPress={requestPermission} title="grant permission" />
      </View>
    );
  }

  function toggleCameraType() {
    setType(current => (current === CameraType.back ? CameraType.front : CameraType.back));
  }

  return (
    <View style={styles.container}>
      <Camera style={styles.camera} type={type} ref={(ref) => { setCameraRef(ref); }}>
        <View style={styles.cameraButtonContainer}>
          <TouchableOpacity style={styles.button} onPress={toggleCameraType}>
            <Text style={styles.text}>Flip Camera</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={async () => {
            // autoCaptureOnOff(enabled);
            // if (!enabledRef) setEnabledRef(true);
            // console.log("enabled ref: ", enabledRef);
            // while (enabledRef && cameraRef) {
            //   setInterval(() => {
            //     //var photo = await cameraRef.takePictureAsync();
            //     console.log("Auto capture URI: ");
            //   }, 1000);
            // }
            async function autoPhotoCapture() {
              var photo = await cameraRef.takePictureAsync();
              console.log("Auto capture URI: ", photo.uri);
            }
            autoCaptureOnOff(enabled);
            if (enabledRef) {
              var photoIntervalID = setInterval(autoPhotoCapture, 2000); // use clearInterval(photoInvervalID) to stop interval
            }
            if (!enabledRef) {
              try {
                clearInterval(photoIntervalID);
              } catch (error) {
                console.log(error);
              }
            }
            if (cameraRef && !enabledRef) {
              var photo = await cameraRef.takePictureAsync();
              console.log(photo.uri);
            }
            //console.log("Camera ref: ", cameraRef);
          }}>
            <Text style={styles.text}>Take Photo</Text>

          </TouchableOpacity>
        </View>
      </Camera >
    </View >
  );
};

//////////////Photo display screen ////////////////////
function PhotoScreen() {
  return (
    <View style={styles.genericContainer}>
      <Text style={styles.text}>Link to photos displayed here!</Text>
    </View>
  );
};

///////////////// Main //////////////////////////
// inits are here because I'm tired
const Stack = createNativeStackNavigator();
const WS_URL = 'ws://192.168.8.207:8080';
const ws = new WebSocket(WS_URL);

function App() {

  ws.onopen = () => {
    console.log('connected');
  }

  ws.onmessage = (data) => {
    console.log(data);
  }

  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="RobotControls" component={RobotControls} />
        <Stack.Screen name="CameraScreen" component={CameraScreen} />
        <Stack.Screen name="PhotoScreen" component={PhotoScreen} />
      </Stack.Navigator>
    </NavigationContainer >
  );
}

export default App;

