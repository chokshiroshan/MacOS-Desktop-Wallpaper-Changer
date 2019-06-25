# MacOS Desktop Wallpaper Changer

After trying multiple background apps for the Mac I finally decided to build my own. This is a Python script which connects to the Pexels API, grabs a HD pictures from pexels and changes your background.

## How do I use it?

Before you can use this amazing script you will need to [Register with Pexels](https://www.pexels.com/login/) and then generate API Key. Once you've created an API key copy the API key and insert it into the pyton script under the API Key section.  

Make a directory on your Mac and clone this project into this folder. 

Run below script to install required libraries:

     pip install -r requirements.txt

To run the script:

    python changer.py


## What's it doing?

The script is calling the Pexels API for a picture and copies the picture to /Images on your Mac. It then uses applescript osascript to set the background.

