document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const sortSelect = document.getElementById('sortSelect');

    searchInput.addEventListener('input', () => {
        window.location.href = `?search=${searchInput.value}&sort_by=${sortSelect.value}`;
    });

    sortSelect.addEventListener('change', () => {
        window.location.href = `?search=${searchInput.value}&sort_by=${sortSelect.value}`;
    });
});
