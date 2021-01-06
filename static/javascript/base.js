    function initMap() {
        const baker_street = { lat: 51.886790, lng: -8.589785 };
        const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 16,
            center: baker_street,
        });
        const label = 'Baker Street Escape Rooms'
        const marker = new google.maps.Marker({
            position: baker_street,
            map: map,
            label: label,
        });
    }