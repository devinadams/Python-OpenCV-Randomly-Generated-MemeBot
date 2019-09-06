# Python-Randomly-Generated-Meme-Bot
This script randomly generates memes from a scraped source image and scraped template. All sources and templates are scraped from shitpostbot5000.com.

This script uses computer vision(OpenCV) to analyze scraped templates and determine the correct dimensions needed to place the source image. There are tons of possible combinations in this version of the script. Currently the script only recognizes red scraped rectangles from templates where as some templates have multiple places to place memes that are not defined by red rectangles but by green or blue or some other color. In the future I might fix this but for now we just delete any scraped templates that don't work.

Templates must be preconfigured before they will work. The script can configure them for you but the template must have a red rectangle(only one for now) where the source image will be placed.

All the preconfigured templates can be found here: https://drive.google.com/open?id=10eshWzTeDLYYxl3i9cok-k8nmbFav7U4

And a bunch of useable source images can be found here but anything works: https://drive.google.com/open?id=1QIMCjejYn_NCVaF4lHuc8J5KyHHMG4dh

Here's an example of output: ![output](https://raw.githubusercontent.com/devinadams/Python-OpenCV-Randomly-Generated-MemeBot/master/out-23.png)

Requires OpenCV
