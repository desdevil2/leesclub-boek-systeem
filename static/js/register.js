// Handles AJAX submission to keep the page responsive. Backend should return JSON {registered, spots_left, message} on success.
(function () {
    const form = document.getElementById('register-form');
    if (!form) return;
    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        const msgEl = document.getElementById('message');
        msgEl.textContent = '';
        const data = new FormData(form);
        try {
            const res = await fetch(form.action, {
                method: (form.method || 'POST'),
                body: data,
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });
            responseText = await res.text()
            if (responseText == "SUCCES") {
                const json = await res.json().catch(() => ({ success: true, message: 'Registered' }));
                msgEl.classList.remove('error');
                msgEl.textContent = json.message || 'Registered successfully';
                if (json.registered != null) {
                    document.getElementById('registered-count').textContent = json.registered;
                }
                if (json.spots_left != null) {
                    document.getElementById('spots-left').textContent = json.spots_left;
                }
                updateRegistered()
            }
            else if (responseText == "FULL") {
                msgEl.classList.add('error');
                msgEl.textContent = "Registration failed, event is full!"
            }
            else if (responseText == "DUPLICATE") {
                msgEl.classList.add('error');
                msgEl.textContent = "You are already registered!"
            }
            else {
                msgEl.classList.add('error');
                msgEl.textContent = "Error while trying to register!";
            }

            form.reset();
        } catch (err) {
            msgEl.classList.add('error');
            msgEl.textContent = 'Network error, try again.';
            console.log(err)
        }
    });
})();


document.addEventListener("DOMContentLoaded", () => {

    const eventItems = document.querySelectorAll(".event-item");

    const bookImage = document.getElementById("book-image");
    const bookTitle = document.getElementById("book-title");
    const bookDescription = document.getElementById("book-description");

    const registeredCount = document.getElementById("registered-count");
    const spotsLeft = document.getElementById("spots-left");

    const eventDate = document.getElementById("event-date");
    const eventTime = document.getElementById("event-time");
    const eventLocation = document.getElementById("event-location");

    const eventId = document.getElementById("event-id");
    eventItems.forEach(item => {

        item.addEventListener("click", () => {

            // Remove active styling from previous selection
            eventItems.forEach(event => {
                event.classList.remove("active");
            });

            // Highlight selected event
            item.classList.add("active");

            // Read event information
            const data = item.dataset;

            // Update book information
            bookTitle.textContent = data.title;
            bookDescription.textContent = data.description;


            console.log(data.image.length)
            if (data.image.length != 4){
                bookImage.src = `data:image/jpeg;base64,${data.image}`;
            }
            else {
                bookImage.src = "/static/images/default-book.jpg";
            }
            
            bookImage.alt = data.title;

            // Update registration statistics
            const registered = Number(data.registered) || 0;

            registeredCount.textContent = registered;

            if (data.capacity !== "") {
                spotsLeft.textContent =
                    Number(data.capacity) - registered;
            } else {
                spotsLeft.textContent = "—";
            }

            // Update event information
            eventDate.textContent = data.date;
            eventTime.textContent = data.time;
            eventLocation.textContent = data.location;

            // Update hidden registration ID
            eventId.value = data.id;

            // Clear previous messages
            document.getElementById("message").textContent = "";

        });

    });

});

function updateRegistered() {
    registered = document.getElementById("registered-count")
    registered.innerHTML = parseInt(registered.innerHTML) + 1
    spotsLeft = document.getElementById("spots-left")
    spotsLeft.innerHTML = parseInt(spotsLeft.innerHTML) - 1

    eventId = document.getElementById("event-id").value;
    const eventItems = document.querySelectorAll(".event-item");
    eventItems.forEach(element => {
        if (element.dataset.id == eventId) {
            element.dataset.registered = String(Number(element.dataset.registered) + 1);
        }
    });
}