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
import { Image } from 'react-native';
import { storage } from "./firebase_setup.js";
import { uploadBytesResumable, ref, getDownloadURL } from 'firebase/storage';


/////////////////// Home Screen ////////////////////////
function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'top' }}>
      <Text>Home </Text>
      <Button
        title="Robot Controls"
        onPress={() => navigation.navigate('RobotControls')}
      />
      <Button
        title="Camera"
        onPress={() => navigation.navigate('CameraScreen')}
      />
    </View>
  );
}
////////////////// Robot Controls /////////////////////////////
function sendMsg() {
  console.log("button clicked!");
  ws.send('hello!');
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
  delay = parseInt(selected); // selected from dropdown menu
  /////////////// auto capture code ///////////////
  const [isEnabled, setIsEnabled] = useState(false);
  const toggleSwitch = () => {
    setIsEnabled(previousState => !previousState);
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Robot Controls</Text>
      <Button
        title="Say hello!"
        onPress={() => sendMsg()}
      />
      <Text> Auto Capture </Text>
      <Switch
        trackColor={{ false: '#767577', true: '#81b0ff' }}
        thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'}
        onValueChange={toggleSwitch}
        value={isEnabled} />
      <Text> Delay </Text>
      <SelectList
        setSelected={(delay) => setSelected(delay)}
        data={data}
        save="value"
      />
    </View>
  );
};

///////////////// Camera Screen /////////////////////////
function CameraScreen() {
  const [type, setType] = useState(CameraType.back);
  const [permission, requestPermission] = Camera.useCameraPermissions();
  const [cameraRef, setCameraRef] = useState(null);

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
        <View style={styles.buttonContainer}>
          <TouchableOpacity style={styles.button} onPress={toggleCameraType}>
            <Text style={styles.text}>flip</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={async () => {
            if (cameraRef) {
              var photo = await cameraRef.takePictureAsync();
              const uri = photo.uri
              console.log(photo.uri);
              uploadImage(uri);
            }
          }}>
            <Text style={styles.text}>take photo</Text>

          </TouchableOpacity>
        </View>
      </Camera>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
  },
  camera: {
    flex: 1,
  },
  buttonContainer: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: 'transparent',
    margin: 64,
  },
  button: {
    flex: 1,
    alignSelf: 'flex-end',
    alignItems: 'center',
  },
  text: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
  },
});
/////////////////Cloud Upload////////////////////

const uploadImage = async (uri) => {
  const filename = uri.substring(uri.lastIndexOf('/') + 1);
  const uploadUri = uri.replace('file://', '');

  // Fetch the file contents and convert to a Blob
  const response = await fetch(uploadUri);
  const blob = await response.blob();

  const timestamp = Date.now();
  const imageName = `my-image-${timestamp}.jpg`;
  const storageRef = ref(storage, imageName);
  const uploadTask = uploadBytesResumable(storageRef, blob);

  console.log("Photo Upload to firebase");
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
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="RobotControls" component={RobotControls} />
        <Stack.Screen name="CameraScreen" component={CameraScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;