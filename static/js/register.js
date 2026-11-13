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


function updateRegistered(){
    registered = document.getElementById("registered-count")
    registered.innerHTML = parseInt(registered.innerHTML) + 1
    spotsLeft = document.getElementById("spots-left")
    spotsLeft.innerHTML = parseInt(spotsLeft.innerHTML) - 1
}