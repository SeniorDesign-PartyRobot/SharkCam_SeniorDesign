////////////////////////////////////////////////////
// Testing code to upload a single harcoded picture to bucket, change filePath to upload different pic
// Service account named: "AppUpload" is the one with the credentials to do this
// sharkcamapp-fb6a8b29b514.json is the private key for google authentification for the AppUpload account, do not touch
// Sources: https://shell.cloud.google.com/?page=editor&pli=1&show=ide%2Cterminal
//          https://www.youtube.com/watch?v=pGSzMfKBV9Q
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

async function FileUpload(bucketName, filePath, destFileName, generationMatchPrecondition) {
    const options = {
        destination: destFileName,
        preconditionOpts: { ifGenerationMatch: generationMatchPrecondition },
    };
    await storage.bucket(bucketName).upload(filePath, options); // the actual uploading happens here
    console.log(`${filePath} uploaded to ${bucketName}`);
}

function main() { // needs 3 inputs to be given for upload
    const bucketName = 'seniordesignbucket';
    const filePath = './pics2test/beetle.jpg'; // name before
    const destFileName = 'cloudbeetle.png'; // name after
    const generationMatchPrecondition = 0; // I dont understand what this does exactly 
    FileUpload(bucketName, filePath, destFileName, generationMatchPrecondition) // FileUpload call
        .catch(console.error);
}

main();
