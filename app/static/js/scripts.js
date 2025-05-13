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
        if (data.error) {
            alert("Error: " + data.error);
        } else {
            document.getElementById("result").innerText = "Encrypted Text: " + data.encrypted_text;

            // Opcional: Mostrar claves RSA si están disponibles
            if (data.rsa_keys) {
                document.getElementById("rsa-public-key").innerText = "Public Key: " + data.rsa_keys.public_key;
                document.getElementById("rsa-private-key").innerText = "Private Key: " + data.rsa_keys.private_key;
            }
        }
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

document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".tabs a");
    const tabContents = document.querySelectorAll(".tab-content");

    tabs.forEach((tab, index) => {
        tab.addEventListener("click", function (e) {
            e.preventDefault();

            // Desactivar todas las pestañas y contenidos
            tabs.forEach(t => t.classList.remove("active"));
            tabContents.forEach(tc => tc.classList.remove("active"));

            // Activar la pestaña y el contenido actual
            tab.classList.add("active");
            tabContents[index].classList.add("active");
        });
    });

    // Activar la primera pestaña por defecto
    tabs[0].classList.add("active");
    tabContents[0].classList.add("active");
});