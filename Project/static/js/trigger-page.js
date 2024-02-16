const Alert = function ({ icon = '', title = '', text = '', darkMode = false, showCancelButton = false, CancelButtonText = 'NO', ConfirmButtonText = 'Okay', dismissButton = true, input = false, inputPlaceholder = '' }) {

    let modal = document.createElement('div');
    modal.setAttribute('class', 'nova-modal');
    document.body.append(modal);
    let alert = document.createElement('div');
    alert.setAttribute('class', 'nova-alert')

    modal.appendChild(alert);
    var svg;

    if (darkMode == true) {
        alert.classList.add('nova-dark-mode');
    }
icon = 'success';
    svg = `<svg class="circular yellow-stroke">
    <circle class="path" cx="75" cy="75" r="50" fill="none" stroke-width="5" stroke-miterlimit="10"/>
</svg>
<svg class="alert-sign yellow-stroke">
    <g transform="matrix(1,0,0,1,-615.516,-257.346)">
        <g transform="matrix(0.56541,-0.56541,0.56541,0.56541,93.7153,495.69)">
            <path class="line" d="M634.087,300.805L673.361,261.53" fill="none"/>
        </g>
        <g transform="matrix(2.27612,-2.46519e-32,0,2.27612,-792.339,-404.147)">
            <circle class="dot" cx="621.52" cy="316.126" r="1.318" />
        </g>
    </g>
</svg>`;
    var icon_template = ` <div class="nova-icon">
       <div class="svg-box">
         ${svg}
       </div>
   </div>`;
    var title_and_text = `
   <h3 class="nova-title">
      ${title}
   </h3>
   <p class="nova-text">
    ${text}
   </p>
   `;

    if (showCancelButton == true) {
        var buttons =
            `
   <div class="nova-btns">
   <a class="accept">
      ${ConfirmButtonText}
   </a>
   <a class="reject">
    ${CancelButtonText}
   </a>
   </div>
   `;
    } else {
        var buttons =
            `
   <div class="nova-btns">
   <a class="accept">
    ${ConfirmButtonText}
   </a>
   </div>
   `;
    }
    if (dismissButton == true) {

        var dismissButton = `<a class="dismissButton">
   X
   </a>`;
    } else {
        var dismissButton = `<a class="dismissButton hidden">
   X
   </a>`;
    }


    if (input == true) {
        var __input = `<input class="nova-input-alert" placeholder='${inputPlaceholder}'>`;
    } else {
        var __input = '';
    }


    var $content = icon_template + title_and_text + __input + buttons + dismissButton;


    alert.innerHTML = $content;

    document.querySelector('.nova-alert .reject  , .nova-alert .accept').onclick = closeNova;
    document.querySelector('.dismissButton').onclick = closeNova;


    function closeNova() {

        alert.remove();
        modal.remove();

    }


    this.then = function (callback) {


        document.querySelector('.nova-alert .accept').onclick = accept;

        function accept() {
            if (input == true) {
                var inputValue = document.querySelector('.nova-input-alert');
                var val = inputValue.value;
                closeNova();
                callback(e = true, val);
            } else {
                closeNova();
                callback(e = true);
            }
            // Redirecting to specific path here:
            window.location.href = '/templates/image.html';
        }
        

        document.querySelector('.nova-alert .reject').onclick = reject;
        function reject() {
            closeNova();
            callback(e = false);
        }
    }
}

new Alert({
    title: 'Alert !!',
    text: 'Ecolog_1 got triggerd. Fire Detected!',
    icon: 'success',
    dismissButton: false,
    darkMode: false,
    ConfirmButtonText: 'Go To Live Page',

});

