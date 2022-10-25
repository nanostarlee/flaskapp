function deleteNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.Stringify({ noteId: noteId })
    }).then((_res) => {
        window.location.href = "/";
    });
}