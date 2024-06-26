var warningMessages = document.getElementsByClassName('alert_warning');
var successMessages = document.getElementsByClassName('alert_success');
for (var i = 0; i < successMessages.length; i++) {
    (function(i) {
        
        setTimeout(function() {    
            successMessages[i].style.display = 'none';
        }, 3000);
    })(i);
}
for (var i = 0; i < warningMessages.length; i++) {
    (function(i) {
        
        setTimeout(function() {       
            warningMessages[i].style.display = 'none';
        }, 3000);
    })(i);
}

window.addEventListener("beforeunload", function (event) {
    navigator.sendBeacon('/account/logout/');
});

let password=document.getElementById('id_password')
let confirm=document.getElementById('id_confirm')
let eyeSee=document.createElement('i')
eyeSee.className='fa-solid fa-eye'
if (eyeSee && eyeSee.parentElement) {
    password.parentElement.append(eyeSee)
}

eyeSee.addEventListener('click', () => {
    const currentType = password.getAttribute('type');
    eyeSee.previousElementSibling.setAttribute('type', currentType === 'password' ? 'text': 'password');
    currentType==='password'?eyeSee.className="fa-solid fa-eye-slash":eyeSee.className='fa-solid fa-eye'
});

let eyeSee2=document.createElement('i')
eyeSee2.className='fa-solid fa-eye'
if (eyeSee2 && eyeSee2.parentElement) {
    confirm.parentElement.append(eyeSee2)
}


eyeSee2.addEventListener('click', () => {
    const currentType = confirm.getAttribute('type');
    eyeSee2.previousElementSibling.setAttribute('type', currentType === 'password' ? 'text': 'password');
    currentType==='password'?eyeSee2.className="fa-solid fa-eye-slash":eyeSee2.className='fa-solid fa-eye'
});


let mybutton = document.getElementById("up_icon");
let myicon = document.getElementById("up_i");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 120 || document.documentElement.scrollTop > 120 ||  document.documentElement.scrollTop) {
    mybutton.style.display = "block";
    
  } 
  else {
    mybutton.style.display = "none";
  }
}

scrollFunction()
mybutton.addEventListener('click',()=>{
  document.body.scrollTop = 0; 
  document.documentElement.scrollTop = 0;
})

