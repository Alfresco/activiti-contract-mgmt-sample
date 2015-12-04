Case Management Sample App for Activiti
=======================================

This project provides an example application which can be easily imported into Activiti to demonstrate a basic case management process.

Building
--------

Maven will build a ZIP file which can be imported into Activiti

    mvn clean package

After building the ZIP file can be found in the `target` directory.

Usage
-----

Log in as the Activiti admin user. After deploying the app you should be able to create a new process of type _Case Management_ from the _Case Management_ app on the home screen.
