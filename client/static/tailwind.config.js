/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  purge: ['../static/**/*.{js,jsx,ts,css,tsx,html}'],
  content: ['../static/**/*.{js,jsx,ts,css,tsx,html}'],
  theme: {
    extend: {},
  },
  plugins: [],
}

// npx tailwindcss -i ./css/base.css -o ./css/styles.css --watch