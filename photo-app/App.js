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
import { Button } from 'react-native';
import useWebSocket, { ReadyState } from 'react-use-websocket';
//import TcpSocket from 'react-native-tcp-socket';




function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'top' }}>
      <Text>Home </Text>
      <Button
        title="Robot Controls"
        onPress={() => navigation.navigate('RobotControls')}
      />
    </View>
  );
}

function sendMsg() {
  console.log("button clicked!");
  ws.send('yeehaw');

};

function RobotControls() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Robot Controls</Text>
      <Button
        title="Say hello!"
        onPress={() => sendMsg()}
      />
    </View>
  );
};

// inits are here because I'm tired
const Stack = createNativeStackNavigator();
const WS_URL = 'ws://192.168.8.207:8080';
const ws = new WebSocket(WS_URL);

function App() {
  const [serverState, setServerState] = React.useState('Loading...');
  const [messageText, setMessageText] = React.useState('');
  const [disableButton, setDisableButton] = React.useState(true);
  const [inputFieldEmpty, setInputFieldEmpty] = React.useState(true);
  const [serverMessages, setServerMessages] = React.useState([]);

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
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;

/////////////////////////////////OLD CODE///////////////////////////////////////////
/*
import { CameraType } from 'expo-camera';
import { Camera } from 'expo-camera';
import { useState } from 'react';
import { Button, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { Image } from 'react-native'

export default function App() {
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
              console.log(photo.uri);
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


*/