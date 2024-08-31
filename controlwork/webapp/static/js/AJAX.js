document.addEventListener('DOMContentLoaded', function() {
    const favoriteButton = document.querySelector('.favorite-button');

    if (favoriteButton) {
        favoriteButton.addEventListener('click', function() {
            const entityId = this.getAttribute('data-id');
            const entityType = this.getAttribute('data-type');
            const isAdding = this.textContent.trim() === 'Добавить в избранное';
            const url = `/api/favorites/${isAdding ? 'add' : 'remove'}/${entityType}/${entityId}/`;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok.');
                }
                return response.json();
            })
            .then(data => {
                if (isAdding) {
                    favoriteButton.textContent = 'Удалить из избранного';
                    favoriteButton.classList.remove('btn-primary');
                    favoriteButton.classList.add('btn-danger');
                } else {
                    favoriteButton.textContent = 'Добавить в избранное';
                    favoriteButton.classList.remove('btn-danger');
                    favoriteButton.classList.add('btn-primary');
                }
            })
            .catch(error => {
                console.error('Ошибка:', error);
            });
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
