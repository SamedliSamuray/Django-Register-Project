var warningMessages = document.getElementsByClassName('alert_warning');
var successMessages = document.getElementsByClassName('alert_success');
    for (var i = 0; i < successMessages.length; i ++) {
        // Set display attribute as !important, neccessary when using bootstrap
        successMessages[i].style.display('none');
    }

window.addEventListener("beforeunload", function (event) {
    
    navigator.sendBeacon('/account/logout/');
});

let password=document.getElementById('id_password')
let confirm=document.getElementById('id_confirm')
let eyeSee=document.createElement('i')
eyeSee.className='fa-solid fa-eye'
password.parentElement.append(eyeSee)
eyeSee.addEventListener('click', () => {
    const currentType = password.getAttribute('type');
    eyeSee.previousElementSibling.setAttribute('type', currentType === 'password' ? 'text': 'password');
    currentType==='password'?eyeSee.className="fa-solid fa-eye-slash":eyeSee.className='fa-solid fa-eye'
});

let eyeSee2=document.createElement('i')
eyeSee2.className='fa-solid fa-eye'
confirm.parentElement.append(eyeSee2)

eyeSee2.addEventListener('click', () => {
    const currentType = confirm.getAttribute('type');
    eyeSee2.previousElementSibling.setAttribute('type', currentType === 'password' ? 'text': 'password');
    currentType==='password'?eyeSee2.className="fa-solid fa-eye-slash":eyeSee2.className='fa-solid fa-eye'
});

