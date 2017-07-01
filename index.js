const fs = require('fs');
const path = require('path');
const program = require('commander');
const rice = require('./rice');

const defaultLocation = process.env.HOME + '/.config/rice/';

// rice save
program.command('save [config]')
  .description('Safe current rice')
  .action((env, options) => {
    const saveName = options.config || 'default';

    // Make directories for .config/rice/saveName
    const saveDirectory = defaultLocation + saveName;

    if (!fs.existsSync(defaultLocation)) {
      console.log("Creating directory " + defaultLocation);
      fs.mkdirSync(path.dirname(defaultLocation));
    }
    if (!fs.existsSync(saveDirectory)) {
      console.log("Creating directory " + saveDirectory);
      fs.mkdirSync(saveDirectory);
    }

    rice.backupTo(saveDirectory);
  });










  program.parse(process.argv);
