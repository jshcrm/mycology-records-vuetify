/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{vue, js,ts,jsx,tsx}"],
  theme: {
    container: {
      center: true,
      padding: {
        sm: "20px",
        md: "20px",
        lg: "20px",
        xl: "70px",
        "2xl": "70px",
      },
    },
    extend: {
      screens: {
        sm: "428px",
        md: "834px",
        lg: "1024px",
        xl: "1280px",
        "2xl": "1536px",
      },
    },
  },
  plugins: [],
};
