#The MIT License (MIT)

# Copyright (c) 2018 Devin Adams <github.com/devinatoms/>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Randomly generated MemeBot
# By Devin A

from __future__ import print_function
from PIL import Image
import os
import random
import templates
import banners
import cv2
import numpy as np

class MemeBot:

    def allfiles(self, directory):
            allFiles = []
            for root, subfiles, files in os.walk(os.getcwd() + directory):
                    for names in files:
                            allFiles.append(os.path.join(root, names))
            return allFiles

    def readImg(self, img):
        img = Image.open(img)
        return img

    def getImgSize(self, img):
        img_w, img_h = img.size
        return img_w, img_h

    def getName(self, fname_path):
        if not os.path.exists(fname_path):
            return fname_path
        filename, file_extension = os.path.splitext(fname_path)
        i = 1
        new_fname = "{}-{}{}".format(filename, i, file_extension)
        while os.path.exists(new_fname):
            i += 1
            new_fname = "{}-{}{}".format(filename, i, file_extension)
        return new_fname

    def paste(self, template, source, template_name, source_name):
        Templates = templates.Templates()
        template_w, template_h = self.getImgSize(template)
        source_w, source_h = self.getImgSize(source)
        offset = Templates.getOffset(template_name)
        template.paste(source, offset)
        name = self.getName(self.OUT_DIRECTORY)
        template.save(name)
        print("Template: ", Templates.getNameFromPath(template_name), "Saved as: ", Templates.getNameFromPath(name))

    def getRandomSource(self):
        all_sources = self.allfiles("\\source\\")
        random_source = random.choice(all_sources)
        return random_source

    def getRandomTemplate(self):
        all_templates = self.allfiles("\\template\\")
        random_template = random.choice(all_templates)
        return random_template

    def loopThroughAllTemplates(self):
        all_templates = self.allfiles("\\template\\")
        offsets = {}
        resizes = {}
        Templates = templates.Templates()
        print("Generating data....")
        for template in all_templates:
            template_name = Templates.getNameFromPath(template)
            offset, resize = self.findTemplateRegion(template)
            offsets[template_name] = offset
            resizes[template_name] = resize
        print("\n")
        print("OFFSET VALUES - GOES IN TEMPLATES FILE")
        print("-------------------------------------------------------")
        print("\n")
        print(offsets)
        print("\n")
        print("RESIZE VALUES - ALSO GOES IN TEMPLATES FILE ")
        print("----------------------------------------------------------")
        print("\n")
        print(resizes)
        print("\n")
        print("Script is pre-configured with several hundred templates.")
        print("New template values for new templates must be added to the templates file before generation. Use the data above.")
        print("\n")



    def make_meme(self):
        Templates = templates.Templates()
        template = self.getRandomTemplate()
        source = self.getRandomSource()
        template_name = template
        source_name = source
        template = self.readImg(template)
        source = self.readImg(source)
        source = Templates.getResizeShape(source, template, source_name, template_name)
        self.paste(template, source, template_name, source_name)

    def findTemplateRegion(self, img):
        img = cv2.imread(img)

        #STEP1: get only red color (or the bounding box color) in the image
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # define range of red color in HSV
        lower_red = np.array([0,50,50])
        upper_red = np.array([0,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_red, upper_red)
        red_only = cv2.bitwise_and(img,img, mask= mask)

        #STEP2: find contour
        gray_img = cv2.cvtColor(red_only,cv2.COLOR_BGR2GRAY)
        _,thresh = cv2.threshold(gray_img,1,255,cv2.THRESH_BINARY)

        _,contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #max contour in the image is the box you want
        areas = [cv2.contourArea(c) for c in contours]
        sorted_areas = np.sort(areas)
        cnt=contours[areas.index(sorted_areas[-1])]
        r = cv2.boundingRect(cnt)

        offset = r[:len(r)//2]
        resize = r[len(r)//2:]

        cv2.rectangle(img,(r[0],r[1]),(r[0]+r[2],r[1]+r[3]),(0,255,0),3)
        return offset, resize

    def populateTemplates(self):
        self.getRandomTemplate()

    def mainLoop(self):
        bannerz = banners.Banners()# create retarded banner class instance

        print("""

                Random Meme Generator


                    """)

        printThoseBanners = bannerz.printBanners() # print stupid ascii banners
        generateDimensions = str(input("Do you wish to find all template dimensions? (Not needed unless using new templates): yes/no "))
        if generateDimensions.lower() == "yes":
            self.loopThroughAllTemplates()
        else:
            pass
        print("\n")
        amt = int(input("How many memers do you want to make?: "))

        print("""

        Generating""", amt, """memes..""")

        amt = amt + 1
        while amt > 0:
            self.make_meme()
            amt = amt - 1
        if amt == 0:
            print("\nDone!")

    def __init__(self):
      self.OUT_DIRECTORY = input("Enter the output directory: ") + "meme.png"#"C://Users//Devin//Desktop//MemeBot//out//meme.png" # CHANGE TO YOUR OUTPUT DIRECTORY! END IT WITH THE FILE NAME!'
      self.mainLoop()

MEMER = MemeBot()
