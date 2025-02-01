module.exports = {
  content: [
    '../news/templates/**/*.html', // Django templates
    '../static/js/**/*.js',   // Custom JS files
    './src/**/*.{js,ts,jsx,tsx}', // Vite source files
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ['cyberpunk', 'business'],
  }
};
