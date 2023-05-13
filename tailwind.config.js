/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    content: ["./**/*.{html,js}"],
    theme: {
      extend: {
        typography: {
          DEFAULT: {
            css: {
              maxWidth: '75ch', // add required value here
              pre: {
                padding: "0",
                color: "#1F2933",
                backgroundColor: "#F3F3F3"
              },
              code: {
                padding: "0.2em 0.4em",
                backgroundColor: "#F3F3F3",
                color: "#DD1144",
                fontWeight: "400",
                "border-radius": "0.25rem"
              },
              "code::before": false,
              "code::after": false,
              "blockquote p:first-of-type::before": false,
              "blockquote p:last-of-type::after": false,
            },
          },
        },
        fontFamily: {
          sans: ['Inter var', ...defaultTheme.fontFamily.sans],
        },
      },
    },
    plugins: [
      require('@tailwindcss/typography'),
    ],
  }