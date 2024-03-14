document.getElementById('textInputForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    var textInput = document.getElementById('textInput').value;

    // Send text input to Python backend
    fetch('/process_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: textInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
