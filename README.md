# Mass Image Cropper For Computer Vision
Created by Jean-Thomas MUYL

### Introduction

**Mass Image Cropper For Computer Vision** is an ad-hoc approach at extracting many smaller images from a large number of images.
For example, this would be a very good tool to extract all the faces from a collection of pictures into a set of small images, all being crops from the images in the input set.


### License

This software is released under the MIT License (refer to the LICENSE file for details).

### Creating the JSON file to save progress
The process of extracting sub-images can take many hours as the initial dataset can contain many thousands of files.
This script comes with a resume function.
To create this file you need to run the script createJson.py with two arguments : the data folder (-i) and the json file name (-o)

```Shell
python createJson.py -i data/ -o progress.json
```

### Running the script

The script takes a few arguments :

```Shell
python massCropperForCV.py -h
   Usage: massCropperForCV.py [options]

   Options:
     -h, --help            show this help message and exit
     -i INPUT, --input-folder=INPUT
                           input folder
     -o OUTPUT, --output-folder=OUTPUT
                           output folder
     -j JSONFILENAME, --jsonfile=JSONFILENAME
                           Json file. See Readme for more details
     -p PREFIX, --prefix=PREFIX
                           the prefix used for every output file. Default =
                           'cropped'
```
For example :

```Shell
python massCropperForCV.py -i data/ -o outputFolder -j progress.json -p dogs
```

###Controls

Once the first image pops up, draw a rectangle on it with your mouse and release the button : a green rectangle appears.
You then have 4 possible controls :

- *"space bar"* will crop the image, save it, and reset the image for a second crop
- *"w"* will crop the image, save it, and display the next image in the input folder
- *"p"* will crop the image, save it, and will tell the program to save the progress and exit
- *"r"* will reset the current image without saving the current crop.

You can easily change these by looking at the clickandcrop.py file.



