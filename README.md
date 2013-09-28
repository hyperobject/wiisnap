WiiSnap v2.0
========

A block module and local server for Snap! to interface with a Nintendo Wiimote

#Changelog
* Added support for Classic Controller/Rock Band controllers
* Updated to snapext framework
* Added cake

#Requirements
* A Wiimote
* Python 2.6+
* The `cwiid` module for Python.
* the `snapext` module (`pip install snapext`)

#Getting Started
* Load Snap! in your browser window.
* Import the wiisnap.xml file.
* In a command line, navigate to the directory where you are storing these files.
* Type `python wiisnap.py`.
* Follow the instructions onscreen.
* The program should print something like `serving on port 1280. Go ahead and launch Snap! in your browser window.`
* **Enjoy!**


#Credits
* Thanks to @blob8108 for developing the snapext framework
* Based upon the Python CORS server here: https://gist.github.com/2904124
* Thanks to the Snap! team for making this fairly easy to do
