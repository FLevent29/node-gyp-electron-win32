const electronPackager = require('electron-packager');

electronPackager({
  dir: '.',
  name: 'node-gyp-electron',
  ignore: /^\/(?!(src|node_modules|package\.json|build))/,
  overwrite: true,
  platform: 'win32',
}).catch(console.error);
