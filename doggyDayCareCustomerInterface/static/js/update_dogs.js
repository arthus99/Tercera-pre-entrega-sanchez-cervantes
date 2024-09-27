document.addEventListener('DOMContentLoaded', function() {
    const ownerSelect = document.getElementById('id_owner');
    const dogSelect = document.getElementById('id_dog');
   
    ownerSelect.addEventListener('change', function() {
        const ownerId = this.value;
        
        // Asegúrate de que la URL sea correcta
        const dogApiUrl = `/api/get_dogs/?owner_id=${ownerId}`;
        fetch(dogApiUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                dogSelect.innerHTML = '';  // Limpia los perros existentes
                const defaultOption = document.createElement('option');
                defaultOption.value = '';
                defaultOption.text = 'Seleccionar perro';
                dogSelect.add(defaultOption);

                data.forEach(dog => {
                    const option = document.createElement('option');
                    option.value = dog.id;
                    option.text = dog.name;
                    dogSelect.add(option);
                });
            })
            .catch(error => console.error('Error fetching dogs:', error));
    });
});