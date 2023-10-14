let modal = document.getElementById("modal");
let btn = document.getElementById("showModalBtn");
let span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting immediately

    // Hide the modal
    document.getElementById('modal').style.display = 'none';

    // Display the loading bar
    document.getElementById('loadingIndicator').style.display = 'block';

    // Submit the form after a short delay to ensure loading bar is visible
    setTimeout(function() {
        document.querySelector('form').submit();
    }, 500);  // Delay for half a second
});
