function showAlert() {
    //show notification on window
    alert('Button clicked! Hello, World!');
}

function submitForm() {
    // Get the input value
    var userName = document.getElementById("userName").value;

    // Display the input value
    document.getElementById("output").innerHTML = "Hello, " + userName + "!";
}

document.getElementById("Sign-in.button").addEventListener("click", function() {
    window.location.href = "index.html";
});