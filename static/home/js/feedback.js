function addClass() {
    document.body.classList.add("sent");
    setTimeout(function () {
        $(feedbackModal).modal("hide");
        document.body.classList.remove("sent");
    }, 4500);
}

function sendMessage() {
    var description = document.getElementById("messageText").value;
    var name = document.getElementById("feedbackName").value;
    var email = document.getElementById("feedbackEmail").value;

    if (name === "" || email === "" || description === "") {
        return;
    }

    var formData = {
        name: name,
        email: email,
        description: description
    };

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/send_email", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
                addClass();
            } else {
                console.error("Error:", xhr.status, xhr.statusText);
            }
        }
    };
    xhr.send(JSON.stringify(formData));
}

sendLetter.addEventListener("click", sendMessage);