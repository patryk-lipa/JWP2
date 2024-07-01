const SCRIPT_ROOT = 'http://127.0.0.1:5000';

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    fetch(SCRIPT_ROOT + '/auth', {
        "method": "POST",
        "body": formData,
    }).then((response) => {
        return response.json();
    }).then((resp) => {
        console.log(resp);
        document.cookie = "access_token=" + resp.access_token;
        window.location.href = SCRIPT_ROOT + '/login';
    }).catch(error => {
        alert('Nie poprawne dane!');
    });
}

function logout() {
    window.location.href = '/logout';
    document.cookie = "access_token=;";
}

function register() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const email = document.getElementById('email').value;
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    formData.append('email', email);

    fetch(SCRIPT_ROOT + '/user', {
        "method": "POST",
        "body": formData,
    }).then((response) => {
        return response.json();
    }).then((resp) => {
        console.log(resp);
        window.location.href = SCRIPT_ROOT + '/login';
    }).catch(error => {
        alert('Błąd podczas rejestracji');
    });
}

function addNote() {
    const title = document.getElementById('note-title').value;
    const content = document.getElementById('note-content').value;
    const access_token = getCookie('access_token');
    fetch('/api/note', {
        'method': 'POST',
        "headers": {
            "Authorizaton": "Bearer " + access_token,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({title: title, content: content}),
    })
    .then(response => {
        return Promise.all([response.ok, response.json()]);
    })
    .then(([ok,data]) => {
        if (ok) {
            createNoteCard(data.note);
            console.log(JSON.stringify(data.note));
            document.getElementById('note-title').value = '';
            document.getElementById('note-content').value = '';
        } else {
            console.log(data);
        }
    });
}

function loadNotes() {
    const access_token = getCookie('access_token');
    console.log(access_token);
    fetch(SCRIPT_ROOT + '/api/note', {
        "method": "GET",
        "headers": {
            "Authorizaton": "Bearer " + access_token
        }
    })
        .then(response => response.json())
        .then(data => {
            data.forEach(note => {
                createNoteCard(note);
            });
    });
}

function deleteNote(noteId) {
    const access_token = getCookie('access_token');
    fetch(SCRIPT_ROOT + `/api/note/${noteId}`, {
        method: 'DELETE',
        "headers": {
            "Authorizaton": "Bearer " + access_token,
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        return Promise.all([response.json(), response.ok]);
    })
    .then(([data, ok]) => {
        if (ok) {
            const noteCard = document.querySelector(`.note-card[data-id='${noteId}']`);
            noteCard.remove();
        } else {
            console.log(data);
        }
    });
}
function editNote(noteId) {
    const noteCard = document.querySelector(`.note-card[data-id='${noteId}']`);
    const newTitle = noteCard.querySelector('h3').innerText;
    const newContent = noteCard.querySelector('p').innerText;
    const access_token = getCookie('access_token');
    console.log(newTitle, newContent);
    fetch(SCRIPT_ROOT + `/api/note/${noteId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            "Authorizaton": "Bearer " + access_token,
        },
        body: JSON.stringify({title: newTitle, content: newContent}),
    })
    .then(response => {
        if (!response.ok) {
            alert('Error editing note');
        }
    });
}

function createNoteCard(note) {
    // Create the outer note card div
    const noteCard = document.createElement('div');
    noteCard.classList.add('note-card');
    noteCard.dataset.id = note.id;

    // Create the delete button
    const deleteBtn = document.createElement('span');
    deleteBtn.classList.add('delete-btn');
    deleteBtn.innerHTML = '&times;';
    deleteBtn.onclick = function() { deleteNote(note.id); };

    // Create the title element
    const noteTitle = document.createElement('h3');
    noteTitle.contentEditable = true;
    noteTitle.innerText = note.title;
    noteTitle.onblur = function() { editNote(note.id); };

    // Create the content element
    const noteContent = document.createElement('p');
    noteContent.contentEditable = true;
    noteContent.innerText = note.content;
    noteContent.onblur = function() { editNote(note.id); };

    // Append the delete button, title, and content to the note card
    noteCard.appendChild(deleteBtn);
    noteCard.appendChild(noteTitle);
    noteCard.appendChild(noteContent);

    // Append the note card to the notes container
    document.getElementById('notes-container').appendChild(noteCard);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
