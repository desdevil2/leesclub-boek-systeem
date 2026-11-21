document.addEventListener("DOMContentLoaded",() => {
    form = document.getElementById("login_form");
    form.addEventListener("submit", submitHandler);
})


async function submitHandler(e) {
    e.preventDefault()
    form = document.getElementById("login_form");
    const data = new FormData(form);
    const res = await fetch(form.action, {
                method: ('POST'),
                body: data,
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });
    response = await res.text();
    if (response == "SUCCES") {
        window.location.replace("/create_event");
    }
    else {
        console.log(response);
    }
}