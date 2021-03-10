# Vue.js framework installation 

## Installation

Step 1: Make sure you have Node.js (LTS) installed (if not, install it from here: https://nodejs.org/en/download/)

Step 2: Install the vue-cli with 'npm install -g @vue/cli' (This will install the CLI globally so you have to do it just once)

Step 3: Run the following command to create the new folder of the project: vue create frontend

Step 4: Navigate with the arrows to 'Manually select features' and press 'Enter"

Step 5: Select 'Babel' (might be already selected), 'Router', 'Vuex', and 'Linter' by pressing space. When done, press 'Enter'

Step 6: Select the 2.x version and press 'Enter'

Step 7: Put 'n' for the history mode and press 'Enter'

Step 8: Select the first ESLint and press 'Enter'

Step 9: Place your config files in package.json and press 'Enter'

Step 10: Put 'n' if you don't want to save all the previous commands as a preset and press 'Enter'

Step 11: Navigate into your project: cd frontend

Step 12: Run the following command to create the 'Vuetify' plugin: vue add vuetify

Step 13: Choose the 'Default' preset

Step 12: Run the following command to install axios, vue-session and vuex: npm install --save axios vue-session vuex

Step 14: Start the local server with this command: npm run serve

Step 15: Either enter 'http://localhost:8080/' in your browser or directly click it in your command prompt

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
