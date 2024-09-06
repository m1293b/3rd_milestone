/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  // purge: ['../static/**/*.{js,jsx,ts,css,tsx,html}'],
  content: ['../static/**/*.{html,js,jsx,ts,css,tsx}', '../templates/**/*.{html,js,jsx,ts,css,tsx}'],
  theme: {
    colors: {
      'transparent': 'transparent',
      'current': 'currentColor',
      'black': 'colors.black',
      'white': 'colors.white',
      'gray': 'colors.gray',
      'emerald': 'colors.emerald',
      'indigo': 'colors.indigo',
      'yellow': 'colors.yellow',
      'main-text': '#d2d6db',
      'main-bg': '#334155',
      'golden': '#fbbf24',
    },
    screens: {
    'tablet': '707px',
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