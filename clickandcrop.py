# (c) Jean-Thomas MUYL
# jeanthomasmuyl@gmail.com
# MIT License
#
#
# Part of this code (essentially the click_and_crop function) is Adrian Rosebrock work.
# You can find the tutorial it's coming from there : http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
# If you're at all interested in Computer Vision and Python his blog is an abolute must-read.
from __future__ import division

import cv2
from utils import randomID


# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	#grab references to the global variables
	global refPt, cropping

	#if the left mouse button was clicked, record the starting
	#(x, y) coordinates and indicate that cropping is being
	#performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	#check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		#record the ending (x, y) coordinates and indicate that
		#the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		#draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)

def cropper(imgfilename,prefix,inputfolder,outfolder,data):
    global image
    filepath = inputfolder + imgfilename
    image = cv2.imread(filepath)
    clone = image.copy()

    screen_res = 800, 600
    scale_width = screen_res[0] / image.shape[1]
    scale_height = screen_res[1] / image.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(image.shape[1] * scale)
    window_height = int(image.shape[0] * scale)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', window_width, window_height)

    cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback("image", click_and_crop)
    interrupt = False
    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF


        if key == 32: #crop save and stay with the same image
            if len(refPt) == 2:
                roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                outfilename = outfolder + prefix + "_" + randomID() + ".jpg"
                cv2.imwrite(outfilename,roi)
                #cv2.waitKey(0)
                image = clone.copy()

        elif key == ord("w"): #crop save and go to the next image
            if len(refPt) == 2:
                roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                outfilename = outfolder + prefix + "_" + randomID() + ".jpg"
                cv2.imwrite(outfilename,roi)
                break
        elif key == ord("p"): #crop save and save state for later run
            if len(refPt) == 2:
                roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                outfilename = outfolder + prefix + "_" + randomID() + ".jpg"
                cv2.imwrite(outfilename,roi)
                interrupt = True
                break
        elif key == ord("a"): #go to next image
            break

        elif key == ord("r"): #reset this rectangle
            image = clone.copy()

    cv2.destroyAllWindows()
    data[imgfilename]["processed"] = "1"
    return (data,interrupt)


def main():
    cropper('img.jpg','testPreffix_','data/','testOutput')


if __name__ == '__main__':
    main()