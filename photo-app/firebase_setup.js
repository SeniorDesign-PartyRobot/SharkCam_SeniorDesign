import { initializeApp } from "firebase/app";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
  apiKey: "AIzaSyC4h44YG9eH2CQN1oh1XnIpkmB5r9DRUE0",
  authDomain: "seniordesignfirebase.firebaseapp.com",
  databaseURL: "https://seniordesignfirebase-default-rtdb.firebaseio.com",
  projectId: "seniordesignfirebase",
  storageBucket: "seniordesignfirebase.appspot.com",
  messagingSenderId: "908816564276",
  appId: "1:908816564276:web:4c00cfe1e4ebbcd74c0a61",
  measurementId: "G-F3JNYLYYZB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const storage = getStorage(app);

