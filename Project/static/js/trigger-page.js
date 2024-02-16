const Alert = function ({ title = '', text = '', ConfirmButtonText = 'Okay', input = false, inputPlaceholder = '' }) {
    let modal = document.createElement('div');
    modal.setAttribute('class', 'nova-modal');
    document.body.append(modal);

    let alert = document.createElement('div');
    alert.setAttribute('class', 'nova-alert');
    modal.appendChild(alert);

    var title_and_text = `
        <h3 class="nova-title">${title}</h3>
        <p class="nova-text">${text}</p>
    `;

    var buttons = `
        <div class="nova-btns">
            <a class="accept">${ConfirmButtonText}</a>
        </div>
    `;

    var __input = input ? `<input class="nova-input-alert" placeholder='${inputPlaceholder}'>` : '';

    var $content = title_and_text + __input + buttons;
    alert.innerHTML = $content;

    document.querySelector('.nova-alert .accept').onclick = function() {
        closeNova();

        if (input) {
            var inputValue = document.querySelector('.nova-input-alert');
            var val = inputValue.value;
            window.location.href = '/templates/image.html';  // Replace with your desired path
        }
    };

    function closeNova() {
        alert.remove();
        modal.remove();
    }

    this.then = function (callback) {
        document.querySelector('.nova-alert .accept').onclick = function() {
            closeNova();
            callback(true);
        };
    };
};

new Alert({
    title: 'Alert !!',
    text: 'Ecolog_1 got triggered. Fire Detected!',
    ConfirmButtonText: 'Go To Live Page',
    input: false,  // Set to true if you want an input field
    inputPlaceholder: ''
});
