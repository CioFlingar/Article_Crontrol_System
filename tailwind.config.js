// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './static/**/*.js'
    ],
    theme: {
        extend: {
            boxShadow: {
                underline: "inset 0 -2px 0 0"
            }
        },
    },
    plugins: [
        require("@tailwindcss/forms"),
        require("@tailwindcss/typography"),
    ],
};