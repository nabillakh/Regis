document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Empêche l'envoi par défaut du formulaire

    fetch('/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value  // Inclus le token CSRF
        },
        body: JSON.stringify({
            username: document.getElementById('username').value,
            email: document.getElementById('email').value,
            password: document.getElementById('password').value
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Error:', data.error);
        } else {
            console.log('Success:', data.message);
            window.location.href = '/welcome/';  // Redirection après succès
        }
    })
    .catch(error => console.error('Error:', error));
});
