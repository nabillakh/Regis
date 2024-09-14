document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Empêche la soumission normale du formulaire

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const username = document.getElementById('id_username').value;
    const email = document.getElementById('id_email').value;
    const password1 = document.getElementById('id_password1').value;
    const password2 = document.getElementById('id_password2').value;

    fetch('/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,  // Nécessaire pour les requêtes POST avec Django
        },
        body: JSON.stringify({
            username: username,
            email: email,
            password1: password1,
            password2: password2
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            // Redirection vers la page de bienvenue en cas de succès
            window.location.href = '/welcome/';
        } else if (data.error) {
            // Affiche les erreurs directement dans la page
            document.getElementById('error-message').innerText = data.error;
            document.getElementById('error-message').style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
});
