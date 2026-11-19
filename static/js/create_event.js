// Handles AJAX submission to keep the page responsive. Backend should return JSON {registered, spots_left, message} on success.
(function () {
    const form = document.getElementById('create-form');
    if (!form) return;
    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        const data = new FormData(form);
        try {
            const res = await fetch(form.action, {
                method: (form.method || 'POST'),
                body: data,
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });
            responseText = await res.text()
            if (responseText == "SUCCES") {
                console.log("SUCCES")
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