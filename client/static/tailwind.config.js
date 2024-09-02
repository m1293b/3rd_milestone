/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  // purge: ['../static/**/*.{js,jsx,ts,css,tsx,html}'],
  content: ['../static/**/*.{js,jsx,ts,css,tsx,html}'],
  theme: {
    screens: {
    'tablet': '640px',
    // => @media (min-width: 640px) { ... }

    'laptop': '1024px',
    // => @media (min-width: 1024px) { ... }

    'desktop': '1280px',
    // => @media (min-width: 1280px) { ... }
    },
    extend: {},
  },
  plugins: [],
}

// npx tailwindcss -i ./css/base.css -o ./css/styles.css --watch