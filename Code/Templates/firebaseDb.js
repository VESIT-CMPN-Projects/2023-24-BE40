// Import the functions you need from the SDKs
 // import { initializeApp } from "firebase/app"
import { getDatabase, ref, set } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";
import {firebase} from "firebase/database";
import {getStorage} from "firebase/storage";


// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyD_hcVTrWN7KInr6Jp09UsKzLKKQJ4TqFM",
    authDomain: "majorproj-auth.firebaseapp.com",
    projectId: "majorproj-auth",
    storageBucket: "majorproj-auth.appspot.com",
    messagingSenderId: "172536099915",
    appId: "1:172536099915:web:61378140640896602f09ce",
    measurementId: "G-5C5TX8VXF7";
}
// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Reference to our database 
const db = getDatabase(app);

document.getElementById("submit").addEventListener('click', function write(e) {
    const data = {
        fname: fname,
        lname: lname,
        email: email,
        phone: phone,
        complaint: complaint,
        platform: platform,
        country: country,
        datecomplaint: datecomplaint,
    };

    // Assuming 'fname' is a unique identifier for your data
    set(ref(db, 'complaints/' + data.fname), data);
    alert("Details Submitted !");
});
    