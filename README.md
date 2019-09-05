# Python-Randomly-Generated-Meme-Bot
Python randomly generated meme bot. Randomly generates memes from a scraped source image and scraped template. All sources and templates are scraped from shitpostbot5000.

This script uses OpenCV to analyze scraped templates and determine the correct dimensions needed to place the source image. There are millions of possible combinations in this version of the script. Currently the script only recognizes red scraped rectangles from templates where as some templates have multiple places to place memes that are not defined by red rectangles but by green or blue. In the future I might fix this but for now we just delete any scraped templates that don't work.

Requires OpenCV
