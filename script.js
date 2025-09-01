document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.input-group input');

    inputs.forEach(input => {
        input.addEventListener('focus', () => input.classList.add('active'));
        input.addEventListener('blur', () => {
            if (!input.value) input.classList.remove('active');
        });
    });
});
