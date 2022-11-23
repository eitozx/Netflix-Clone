module.exports = {
  content: [
    "./templates/**/*html",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

// npx tailwindcss -i ./templates/assets/css/input.css -o ./templates/assets/css/style.css --watch