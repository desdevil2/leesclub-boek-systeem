// Handles AJAX submission to keep the page responsive. Backend should return JSON {registered, spots_left, message} on success.
(function () {
    const form = document.getElementById('create-form');
    if (!form) return;
    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        const data = new FormData(form);
        document.getElementById("register-btn").disabled=true;
        document.getElementById("loading").src = "/static/images/loading.gif";
        document.getElementById("registering").innerHTML = "Registering...";
        try {
            const res = await fetch(form.action, {
                method: ('POST'),
                body: data,
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });
            responseText = await res.text()
            if (responseText == "SUCCES") {
                console.log("SUCCES");
                form.reset();
            }
            else {
                console.log("Something went wrong");
            }

            
        } catch (err) {
            console.log(err)
        }
                document.getElementById("loading").src = "";
        document.getElementById("register-btn").disabled=false;
        document.getElementById("registering").innerHTML = "";
    });
})();


document.addEventListener("DOMContentLoaded", () => {
    var logoutBtn = document.getElementById("logout");
    logoutBtn.addEventListener("click", logout)});



async function logout(){
    var res = await fetch("/logout", {
        method: "POST",
        headers : {
            "X-Requested_With" : "XMLHTTPRequest"
        }
    });
    var text = await res.text();
    if (text == "SUCCES") {
        window.location.replace("/login")
    }
    else {
        console.log(text);
    }
}

