document.addEventListener('DOMContentLoaded', function() {
    var navLinks = document.querySelectorAll('.navbar-nav .nav-link, .navbar-nav .btn-link');
    var buttons = document.querySelectorAll('.btn-primary-custom, .btn-secondary-custom');

    navLinks.forEach(function(link) {
        link.addEventListener('mouseover', function() {
            link.style.backgroundColor = '#e9ecef';
            link.style.color = '#000';
            link.style.border = '1px solid #000';
        });

        link.addEventListener('mouseout', function() {
            link.style.backgroundColor = '';
            link.style.color = '';
            link.style.border = '';
        });
    });

    buttons.forEach(function(button) {
        button.addEventListener('mouseover', function() {
            button.style.backgroundColor = '#e9ecef';
            button.style.color = '#000';
            button.style.border = '1px solid #000';
        });

        button.addEventListener('mouseout', function() {
            button.style.backgroundColor = '';
            button.style.color = '#000';
            button.style.border = '1px solid #000';
        });
    });
});
