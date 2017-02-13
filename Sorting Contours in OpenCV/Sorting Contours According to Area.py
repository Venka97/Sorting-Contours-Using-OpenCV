{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "image  = cv2.imread(\"C:\\Users\\Venkatesh\\Desktop\\shapes.png\")\n",
    "\n",
    "original = image.copy()\n",
    "#Converting the image to grayscale\n",
    "\n",
    "gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)\n",
    "#Creating a blank image with the same dimesions as out original image\n",
    "blank_image = np.zeros((image.shape[0],image.shape[1],3))\n",
    "\n",
    "#Edge detection \n",
    "edged = cv2.Canny(gray,20,120)\n",
    "\n",
    "#Finding Contours\n",
    "contour,heirarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)\n",
    "\n",
    "\n",
    "sorted_contour = sorted(contour ,key = cv2.contourArea , reverse = True)\n",
    "\n",
    "#for drawing contour according to areas in descending order\n",
    "\n",
    "\n",
    "#Sorting according to area\n",
    "for c in sorted_contour:\n",
    "    cv2.drawContours(blank_image,[c],-1,(0,255,0),3)\n",
    "    cv2.waitKey()\n",
    "    cv2.imshow(\"Black Image\",blank_image)\n",
    "    \n",
    "for cnt in sorted_contour:\n",
    "    cv2.drawContours(original,[cnt],-1,(0,255,0),3)\n",
    "    cv2.waitKey()\n",
    "    cv2.imshow(\"Black Image\",original)\n",
    "    \n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
