// JavaScript function to get cookie by name; retrieved from https://docs.djangoproject.com/en/3.1/ref/csrf/
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


// JavaScript wrapper function to send HTTP requests using Django's "X-CSRFToken" request header
function sendHttpAsync(path, method, body) {
    let props = {
        method: method,
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        mode: "same-origin",
    }

    if (body !== null && body !== undefined) {
        props.body = JSON.stringify(body);
    }

    return fetch(path, props)
        .then(response => {
            return response.json()
                .then(result => {
                    console.log("then1-1-1");
                    return {
                        ok: response.ok,
                        body: result
                    }
                });
        })
        .then(resultObj => {
            return resultObj;
        })
        .catch(error => {
            throw error;
        });
}

const newsletterForm = document.querySelector('.newsletter-form');

/**
 * What to do when NL form is a success
 */
const nlFormAftermath = () => {
    const inputFields = Array.from(newsletterForm.querySelectorAll('input:not([type=submit])'));
    const closeFormButton = document.querySelector('.close.close-nl-form');
    const submitButton = newsletterForm.querySelector('input[type=submit]');
    inputFields.forEach( input => {
        input.disabled = true;
        input.style.opacity = "0.5";
    });
    submitButton.value = "OK";
    submitButton.addEventListener('click', (event) => {
        event.preventDefault();
        closeFormButton.click();
    })
}

if (newsletterForm) {
    newsletterForm.addEventListener('submit', event => {
        event.preventDefault();

        if (!event.target.querySelector('#id_basket_subscription').checked &&
            !event.target.querySelector('#id_aai_subscription').checked
        ) {
            newsletterForm.classList.add('so-what');
            return;
        }

        let requestBody = {
            "firstname": event.target.querySelector('#id_firstname').value,
            "lastname": event.target.querySelector('#id_lastname').value,
            "email": event.target.querySelector('#id_email').value,
            "basket_subscription": event.target.querySelector('#id_basket_subscription').checked,
            "aai_subscription": event.target.querySelector('#id_aai_subscription').checked
        };

        sendHttpAsync(`${window.location.origin}/panier/subscription-endpoint`, "POST", requestBody)
            .then(response => {
                if (response.body.success) {
                    newsletterForm.classList.remove('so-what');
                    newsletterForm.classList.add('success');
                    nlFormAftermath();
                } else {
                    newsletterForm.classList.add('error');
                }
            });
    });
}


window.addEventListener("DOMContentLoaded", (event) => {
    // console.log("DOM entièrement chargé et analysé");

    if (window.location.hash === "#garden-form") {
        document.getElementById('garden-form').classList.add('open');
    }
    const nlForm = document.getElementById('newsletter-form');

    document.addEventListener('click', (event) => {
        const element = event.target;

        if (element.classList.contains('call-nl-form')) {
            event.preventDefault();
            if (nlForm) {
                nlForm.classList.toggle('visible');
            }
        } else if (element.classList.contains('close-nl-form')) {
            event.preventDefault();
            // console.log('close-nl-form fired!');
            if (nlForm) {
                nlForm.classList.toggle('visible');
            }
        }
    });
});