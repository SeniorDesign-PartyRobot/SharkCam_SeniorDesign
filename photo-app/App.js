/////////////////////////////EXPO EXAMPLE BASE////////////////////////////////////
// https://levelup.gitconnected.com/how-to-click-images-in-react-native-using-expo-camera-for-android-1fbc1181473d
// base tutorial from here: https://medium.com/@nutanbhogendrasharma/implement-camera-in-react-native-mobile-app-part-1-ea307ce924a4
// https://www.freecodecamp.org/news/how-to-create-a-camera-app-with-expo-and-react-native/

//////////////////////////////////Test Code/////////////////////////////////////////
// Navigate between screens: https://reactnavigation.org/docs/navigating
// In App.js in a new project

import * as React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer, useFocusEffect } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { Button, Switch, Alert, StyleSheet, TouchableOpacity } from 'react-native';
import { SelectList } from 'react-native-dropdown-select-list';
import { useState, useEffect } from 'react';
import { CameraType } from 'expo-camera';
import { Camera } from 'expo-camera';
import { Image } from 'react-native';
import { storage } from "./firebase_setup.js";
import { uploadBytesResumable, ref, getDownloadURL, listAll } from 'firebase/storage';
import AsyncStorage from '@react-native-async-storage/async-storage';

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
function HomeScreen({ navigation, route }) {
  // retrieve data function
  const getData = async () => {
    try {
      const value = await AsyncStorage.getItem('@enableKey')
      return value;
      if (value !== null) {
        // value previously stored
      }
    } catch (e) {
      // error reading value
    }
  }
  useFocusEffect(() => {
    value = getData(); // get data on home screen nav
    console.log("Stored Data: ", value); // why does stored data value change?
  });
  return (
    <View style={styles.genericContainer}>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => navigation.navigate('RobotControls')}>
          <Text style={styles.homeButtonText}>{"Settings"}</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => {
          navigation.navigate('CameraScreen', {});
        }}>
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
  try {
    console.log(input);
    ws.send(input);
  } catch {
    console.log("Message could not be sent");
  }

};

function RobotControls({ navigation }) {

  // store data function
  const storeData = async (value) => {
    try {
      await AsyncStorage.setItem('@enableKey', value);
      console.log("data stored");
    } catch (e) {
      // saving error
    }
  }

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
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={async () => {
          var stringIsEnabled = String(isEnabled);
          console.log("is enabled: ", stringIsEnabled);
          await storeData(stringIsEnabled);
          navigation.navigate('Home')
        }}>
          <Text style={styles.settingsButtonText}>{"Apply Changes"}</Text>
        </TouchableOpacity>
      </View>
    </View >
  );
};

///////////////// Camera Screen /////////////////////////
function CameraScreen({ navigation, enabled }) {
  const [type, setType] = useState(CameraType.back);
  const [permission, requestPermission] = Camera.useCameraPermissions();
  const [cameraRef, setCameraRef] = useState(null);
  const [enabledRef, setEnabledRef] = useState(false);

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
              const uri = photo.uri
              console.log(photo.uri);
              uploadImage(uri);
            }
          }}>
            <Text style={styles.text}>Take Photo</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('RobotControls')}>
            <Text style={styles.text}>Settings</Text>
          </TouchableOpacity>
        </View>
      </Camera >
    </View >
  );
};

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

////////////////Cloud List all Images/////////////////
//https://firebase.google.com/docs/storage/web/list-files
//https://stackoverflow.com/questions/37335102/how-to-get-a-list-of-all-files-in-cloud-storage-in-a-firebase-app

const ListImagesInBucket = async () => {
  // Create a reference under which you want to list
  const listRef = ref(storage, 'TestingListFolder/');
  const results = await listAll(listRef);
  const item_list = results.items.map((itemRef) => itemRef.name);

  return item_list;
  /*
  // Find all the prefixes and items.
  listAll(listRef).then((results) => {
    results.items.forEach((itemRef) => {
      content2display(itemRef);
      // All the items under listRef.
    });
  }).catch((error) => {
    console.log(error)
  });



  function content2display(itemRef) {
    //itemRef.getDownloadURL().then()
    console.log(itemRef.name)
  }; */
}


//////////////Photo display screen ////////////////////
function PhotoScreen() {
  const [imageList, setImageList] = useState([]);

  const handlePress = async () => {
    const list = await ListImagesInBucket();
    setImageList(list);
  };

  return (
    <View style={styles.genericContainer}>
      <Text style={styles.text}>List of images:</Text>
      {imageList.map((imageName, index) => (
        <Text key={index}>{imageName}</Text>
      ))}
      <Button title="List Images" onPress={handlePress} />
    </View>
  );
}

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