// solicitar_frete.js

const mapboxToken = 'pk.eyJ1Ijoid3Vlc2xleW1heCIsImEiOiJjbWk4MmFxZnYwN210Mmxvc2Y4b25kaDdkIn0.KlU45qR_UwafsiKxPy2y_A';

function autocomplete(inputId, listId) {
  const input = document.getElementById(inputId);
  const list = document.getElementById(listId);

  input.addEventListener('input', async () => {
    const query = input.value;

    if (query.length < 3) {
      list.innerHTML = '';
      return;
    }

    const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${encodeURIComponent(query)}.json?access_token=${mapboxToken}&autocomplete=true&types=address&country=br&limit=5`;

    const res = await fetch(url);
    const data = await res.json();

    list.innerHTML = '';

    data.features.forEach(feature => {
      const div = document.createElement('div');
      div.textContent = feature.place_name;
      div.style.padding = '10px';
      div.style.cursor = 'pointer';

      div.addEventListener('click', () => {
        input.value = feature.place_name;
        list.innerHTML = '';
      });

      list.appendChild(div);
    });
  });

  // Fecha a lista ao clicar fora
  document.addEventListener('click', e => {
    if (e.target !== input) {
      list.innerHTML = '';
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  autocomplete('endereco_coleta', 'autocomplete-list-coleta');
  autocomplete('endereco_entrega', 'autocomplete-list-entrega');
});
