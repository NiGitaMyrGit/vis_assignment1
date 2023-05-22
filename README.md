# Building a simple image search algorithm

## 1. Contributions
Help sources:
Bhattacharyya distance: https://pyimagesearch.com/2014/07/14/3-ways-compare-histograms-using-opencv-python/
fnmatch: https://docs.python.org/3/library/fnmatch.html
something about lambda functions and very basic lambda calculus:
https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
https://www.youtube.com/watch?v=d0yEXKas8xE

## 2. Assignment description
For this assignment, you'll be using OpenCV to design a simple image search algorithm.
The dataset is a collection of over 1000 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford, and full details of the data can be found here.
For this exercise, you should write some code which does the following:
Define a particular image that you want to work with
For that image
Extract the colour histogram using OpenCV
Extract colour histograms for all of the *other images in the data
Compare the histogram of our chosen image to all of the other histograms
For this, use the cv2.compareHist() function with the cv2.HISTCMP_CHISQR metric
Find the five images which are most similar to the target image
Save a CSV file to the folder called out, showing the five most similar images and the distance metric:
|Filename|Distance]
|---|---|
|target|0.0|
|filename1|---|
|filename2|---|

### Additional comments
Your code should include functions that you have written wherever possible. Try to break your code down into smaller self-contained parts, rather than having it as one long set of instructions.
For this assignment, you are welcome to submit your code either as a Jupyter Notebook, or as .py script. If you do not know how to write .py scripts, don't worry - we're working towards that!
Lastly, you are welcome to edit this README file to contain whatever information you like. Remember - documentation is important!

### Objective
This assignment is designed to test that you can:
- Work with larger datasets of images
- Extract structured information from image data using OpenCV
- Quantaitively compare images based on these features, performing distant viewing
### Some notes
You'll need to first unzip the flowers before you can use the data!

### Additional comments 
This assignment is designed to test that you can:
Work with larger datasets of images
Extract structured information from image data using OpenCV
Quantaitively compare images based on these features, performing distant viewing
Some notes
You'll need to first unzip the flowers before you can use the data!
Additional comments
Your code should include functions that you have written wherever possible. Try to break your code down into smaller self-contained parts, rather than having it as one long set of instructions.
For this assignment, you are welcome to submit your code either as a Jupyter Notebook, or as .py script. If you do not know how to write .py scripts, don't worry - we're working towards that!
Lastly, you are welcome to edit this README file to contain whatever information you like. Remember - documentation is important!




The code in the python script '''histograms_comparison.py''' does the following:

- Define a particular image thar will be worked with. I have chosen image_1305.jpg, but this can be changed
- For that image
  - Extracts the colour histogram using ```OpenCV```
- Extract colour histograms for all of the *other* images in the data 
- Compare the histogram of our chosen image to all of the other histograms 
  - by using the ```cv2.compareHist()``` function with the ```cv2.HISTCMP_CHISQR``` metric
  - the distance between the target image's histogram and all other histograms is calculated by using the Bhattacharyya distance. This ditance 
- Finds the five images which are most simlar to the target image
  - Saves a CSV file to the folder called ```out```, showing the five most similar images and the distance metric:


### 2.2 Objective

This assignment is designed to test the ability to:

1. Working with larger datasets of images
2. Extract structured information from image data using ```OpenCV```
3. Quantaitively compare images based on these features, performing *distant viewing*

## 3. Methods
This assignment is using ```OpenCV``` to design a simple image search algorithm.

## 4. Usage
### 4.1 extract data
in the command line make sure you are located in the main folder. From here start by running bash setup.sh
afterwards direct to the folder "in" (by using cd in/) and unzip the dataset by running "unzip flowers.zip"

### 4.2 install packages
the dataset is a collection of over 1000 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford, and full details of the data can be found [here](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/).



## 5. Results - discussion
I have tried meddling with the bin count. 
One of the datatables in the outfolder showcases the results
with an adjusted bin-count of 36 bins instead of the 256
I must admit I with my human eyes at least, cannot really tell apart how similiar each image is or not.
A promising thing is that the exact same picture (image_)