function updateDogs() {
    const ownerSelect = document.getElementById('id_owner');
    const dogSelect = document.getElementById('id_dog');

    ownerSelect.addEventListener('change', function() {
        const ownerId = this.value;
        const dogApiUrl = `/admin/api/get_dogs/?owner_id=${ownerId}`;

        fetch(dogApiUrl)
            .then(response => response.json())
            .then(data => {
                dogSelect.innerHTML = '';  // Limpia los perros existentes
                data.forEach(dog => {
                    const option = document.createElement('option');
                    option.value = dog.id;
                    option.text = dog.name;
                    dogSelect.add(option);
                });
            })
            .catch(error => console.error('Error fetching dogs:', error));
    });
}