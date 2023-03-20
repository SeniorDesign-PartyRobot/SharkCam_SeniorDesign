////////////////////////////////////////////////////
// Testing code to delete a single harcoded picture to bucket, change filePath to delte different pic
// Service account named: "AppUpload" is the one with the credentials to do this
// sharkcamapp-fb6a8b29b514.json is the private key for google authentification for the AppUpload account, do not touch
// Sources: https://github.com/googleapis/nodejs-storage/blob/main/samples/deleteFile.js
// TODO: 1) get a loop working
//       2) fuse to main app
//       3) Merge to main
//       4) Add different users
///////////////////////////////////////////////////////////

const { Storage } = require('@google-cloud/storage');
const storage = new Storage({
    keyFilename: 'sharkcamapp-fb6a8b29b514.json', // used for authentification by google, the json file is the private key do not share
    projectId: 'sharkcamapp',
});

async function deleteFile(bucketName, fileName, generationMatchPrecondition) {
    const deleteOptions = {
        ifGenerationMatch: generationMatchPrecondition,
    };
    await storage.bucket(bucketName).file(fileName).delete();
    console.log(`${fileName} deleted`);
}

async function main() { // needs 3 inputs to be given for delete
    const bucketName = 'seniordesignbucket';
    const fileName = 'cloudbeetle.png'; // name to erase
    const generationMatchPrecondition = 0; // I dont understand what this does exactly 
    deleteFile(bucketName, fileName, generationMatchPrecondition) // FileUpload user call
        .catch(console.error);
}

main();
