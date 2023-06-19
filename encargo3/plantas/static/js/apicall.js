const mainB = document.querySelector('.mainB');

async function getData() {
  const res = await fetch('https://jsonplaceholder.typicode.com/photos');
  const photos = await res.json();
  photos.forEach(p => {
    const card = document.createElement('div');
    card.className = 'card';

    const img = document.createElement('img');
    img.src = p.url;

    const title = document.createElement('h5');
    title.textContent = p.title;

    card.append(img, title);
    mainB.append(card);
  });
}

getData();
