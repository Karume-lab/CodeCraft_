document.getElementById("contactForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get the form values
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var subject = document.getElementById("subject").value;
    var description = document.getElementById("description").value;

    // Create an object with the form data
    var formData = {
        name: name,
        email: email,
        subject: subject,
        description: description
    };

    // Send the form data to the server-side script
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/send_email", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Handle the response from the server
            console.log(xhr.responseText);
            // Optionally display a success message to the user
        }
    };
    xhr.send(JSON.stringify(formData));
});