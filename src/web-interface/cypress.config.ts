const { defineConfig } = require('cypress');
const vitePreprocessor = require('@cypress/vite-dev-server');

module.exports = defineConfig({
  component: {
    devServer: {
      framework: 'react',
      bundler: 'vite',
    },
    specPattern: 'src/**/*.cy.{js,jsx,ts,tsx}', // Adjust this pattern to match your test files
  },
  e2e: {
    setupNodeEvents(on, config) {
      on('dev-server:start', (options) => vitePreprocessor(options));
      return config;
    },
    baseUrl: 'http://localhost:3000',
  },
});
