/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  // purge: ['../static/**/*.{js,jsx,ts,css,tsx,html}'],
  content: [
    "../static/**/*.{html,js,jsx,ts,css,tsx}",
    "../templates/**/*.{html,js,jsx,ts,css,tsx}",
  ],
  theme: {
    colors: {
      transparent: "transparent",
      current: "currentColor",
      red: "#EF0107",
      "main-text": "#d2d6db",
      "main-bg": "#334155",
      golden: "#fbbf24",
    },
    screens: {
      tablet: "720px",
      // => @media (min-width: 720px) { ... }

      laptop: "1024px",
      // => @media (min-width: 1024px) { ... }

      desktop: "1280px",
      // => @media (min-width: 1280px) { ... }
    },
    extend: {},
    container: {
      center: true,
    },
  },
  plugins: [],
};

// npx tailwindcss -i ./css/base.css -o ./css/styles.css --watch
