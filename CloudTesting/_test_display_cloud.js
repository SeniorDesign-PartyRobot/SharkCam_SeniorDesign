////////////////////////////////////////////////////
// Testing code to display a single hardcoded picture of the bucket, change .file on line 30 to change the picture
// Works by telling the bucket to create a signed URL for given picture for 15 min
// Service account named: "AppUpload" is the one with the credentials to do this
// sharkcamapp-fb6a8b29b514.json is the private key for google authentification for the AppUpload account, do not touch
// Sources: https://cloud.google.com/storage/docs/access-control/signing-urls-with-helpers#storage-signed-url-object-nodejs
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

async function tempURL() {
    // These options will allow temporary read access to the file
    const options = {
        version: 'v4',
        action: 'read',
        expires: Date.now() + 15 * 60 * 1000, // 15 minutes
    };

    // Get a v4 signed URL for reading the file
    const [signedUrl] = await storage
        .bucket('seniordesignbucket')
        .file('testPic')
        .getSignedUrl(options);

    console.log('Signed URL:', signedUrl);
}

tempURL().catch(console.error);