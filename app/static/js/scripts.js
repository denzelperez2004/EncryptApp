document.getElementById("encrypt-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const inputText = document.getElementById("input-text").value;
    const selectedMethod = document.getElementById("encryption-method").value;

    if (!inputText) {
        alert("Please enter text to encrypt.");
        return;
    }

    // Perform AJAX request to encrypt the text
    fetch("/encrypt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: inputText, method: selectedMethod })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Encrypted Text: " + data.encrypted_text;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});

document.getElementById("decrypt-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const inputText = document.getElementById("input-text").value;
    const selectedMethod = document.getElementById("decryption-method").value;

    if (!inputText) {
        alert("Please enter text to decrypt.");
        return;
    }

    // Perform AJAX request to decrypt the text
    fetch("/decrypt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: inputText, method: selectedMethod })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Decrypted Text: " + data.decrypted_text;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});