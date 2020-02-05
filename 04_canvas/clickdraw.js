const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

ctx.fillStyle = 'green';
ctx.fillRect(10, 10, 150, 100);

funcion clearrect() {

  const context = canvas.getContext('2d');

  context.clearRect(0, 0, canvas.width, canvas.height);
}
