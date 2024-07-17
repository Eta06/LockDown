fetch('/language_data')
  .then(response => {
    if (!response.ok) { // Check if the fetch was successful
      throw new Error('Could not fetch language data');
    }
    return response.json();
  })
  .then(app_files => {
    // Stylized console output
    console.log('%cLockDown\n', 'font-weight: bold; font-size: 50px; color: red; text-shadow: 0px 3px 3px rgb(217,31,38), 0px 6px 6px rgb(226,91,14), 0px 9px 9px rgb(245,221,8), 0px 12px 12px rgb(5,148,68), 0px 15px 15px rgb(2,135,206), 0px 18px 18px rgb(4,77,145), 0px 21px 21px rgb(42,21,113)');
    console.log('%c Web UI\n', 'font-weight: bold; font-size: 50px; color: red; text-shadow: 0px 3px 3px rgb(217,31,38), 0px 6px 6px rgb(226,91,14), 0px 9px 9px rgb(245,221,8), 0px 12px 12px rgb(5,148,68), 0px 15px 15px rgb(2,135,206), 0px 18px 18px rgb(4,77,145), 0px 21px 21px rgb(42,21,113)');
    console.error("============================================");

    // Output app config data
    console.log('%cVersion: ' + app_files.config.app_version, 'font-weight: bold; font-size: 20px');
    console.log('%cAuthor: ' + app_files.config.app_author, 'font-weight: bold; font-size: 20px');
    console.log('%cLanguage: ' + app_files.config.app_language, 'font-weight: bold; font-size: 20px');

    // Check if infotext properties exist before logging
    if (app_files.lang.infotext1 && app_files.lang.infotext2 && app_files.lang.infotext3 && app_files.lang.infotext4 && app_files.lang.infotext5) {
      console.warn(
        app_files.lang.infotext1 + "\n" +
        app_files.lang.infotext2 + "\n" +
        app_files.lang.infotext3 + "\n" +
        app_files.lang.infotext4 + "\n" +
        app_files.lang.infotext5
      );
    } else {
      console.warn(app_files.lang.missingtranslations);
    }
  })
  .catch(error => {
    console.error('Error:', error); // Handle errors gracefully
  });
