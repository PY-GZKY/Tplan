module.exports = {
  presets: [
    '@vue/app'
  ],
  sourceType: 'unambiguous',
  env: {
    development: {
      plugins: ['dynamic-import-node']
    }
  }
}
