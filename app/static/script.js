document.getElementById('dog-btn').addEventListener('click', function() {
    fetch('/dog')
        .then(response => response.json())
        .then(data => {
            const img = document.getElementById('dog-img');
            if (data.url) {
                img.src = data.url;
                img.style.display = 'block';
            } else {
                img.style.display = 'none';
                alert('No dog image found!');
            }
        })
        .catch(() => {
            alert('Error fetching dog image!');
        });
});
