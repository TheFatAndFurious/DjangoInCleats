document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.getElementById('theme-toggle');
    const togglTxt = document.getElementById('togglTxt')
    let storedTheme = localStorage.getItem('theme') || 'cyberpunk';
    document.documentElement.setAttribute('data-theme', storedTheme);

    toggleBtn.addEventListener('click', () => {
      // Switch theme between light and dark
      storedTheme = (storedTheme === 'cupcake') ? 'business' : 'cupcake';
      document.documentElement.setAttribute('data-theme', storedTheme);
      localStorage.setItem('theme', storedTheme);
      if (storedTheme === 'cupcake') {
        togglTxt.innerHTML = 'Dark'
      } else {
        togglTxt.innerHTML = 'Light'
      }
    });
  });