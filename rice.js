const fs = require('fs');
const path = require('path');

const HOME = process.env.HOME;
const files = [
  HOME + '/.Xresources',
  HOME + '/.xinitrc'
]


const rice = {
  backupTo: (directory) => {
    console.log("Backing up to ", directory);

    for (let fileIndex = 0; fileIndex < files.length; fileIndex++) {
      copyFile(files[fileIndex], directory + '/' + path.basename(files[fileIndex]));

      console.log("Copied ", files[fileIndex], " to ", directory + '/' + path.basename(files[fileIndex]));
    }

  },
}



function copyFile(from, to) {
  fs.createReadStream(from).pipe(fs.createWriteStream(to));
}


module.exports = rice;
