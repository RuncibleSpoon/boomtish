const ball = document.getElementById('ball');
const window_ = document.getElementById('window');
const answer = document.getElementById('answer');

ball.addEventListener('click', async () => {
  if (ball.classList.contains('shaking')) return;

  // Reset answer display
  answer.classList.remove('visible', 'positive', 'neutral', 'negative');
  window_.classList.remove('revealed');

  // Trigger shake
  ball.classList.add('shaking');

  try {
    const response = await fetch('/shake');
    const data = await response.json();

    // After shake ends (~600ms), reveal the answer
    setTimeout(() => {
      answer.textContent = data.answer;
      answer.classList.add(data.type);
      window_.classList.add('revealed');
      setTimeout(() => answer.classList.add('visible'), 100);
    }, 580);
  } catch (err) {
    console.error('Failed to fetch answer:', err);
  }

  // Re-enable clicking after animation
  ball.addEventListener('animationend', () => {
    ball.classList.remove('shaking');
  }, { once: true });
});
