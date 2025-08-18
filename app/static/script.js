document.getElementById('dog-btn').addEventListener('click', function() {
    const loadingBar = document.getElementById('loading-bar');
    const img = document.getElementById('dog-img');
    loadingBar.style.display = 'flex';
    img.style.display = 'none';
    fetch('/dog')
        .then(response => response.json())
        .then(data => {
            loadingBar.style.display = 'none';
            if (data.url) {
                img.src = data.url;
                img.style.display = 'block';
            } else {
                img.style.display = 'none';
                alert('No dog image found!');
            }
        })
        .catch(() => {
            loadingBar.style.display = 'none';
            alert('Error fetching dog image!');
        });
});
