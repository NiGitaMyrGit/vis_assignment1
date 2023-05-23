# Building a simple image search algorithm
The portfolio exam for **Visual Analytics S22** consists of 4 projects; three class assignments and one self-assigned project. This is the repository for the **first assignment** in the portfolio.
## 1. Contributions
**Help sources**:
*Bhattacharyya distance*: https://pyimagesearch.com/2014/07/14/3-ways-compare-histograms-using-opencv-python/
*fnmatch*: https://docs.python.org/3/library/fnmatch.html
*lambda functions* and very basic lambda calculus:
https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
https://www.youtube.com/watch?v=d0yEXKas8xE

## 2. Initial assignment description by instructor
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

### 2.1 Additional comments
Your code should include functions that you have written wherever possible. Try to break your code down into smaller self-contained parts, rather than having it as one long set of instructions.
For this assignment, you are welcome to submit your code either as a Jupyter Notebook, or as .py script. If you do not know how to write .py scripts, don't worry - we're working towards that!
Lastly, you are welcome to edit this README file to contain whatever information you like. Remember - documentation is important!

### 2.2 Objective
This assignment is designed to test that you can:
- Work with larger datasets of images
- Extract structured information from image data using OpenCV
- Quantaitively compare images based on these features, performing distant viewing
### 2.3 Some notes
You'll need to first unzip the flowers before you can use the data!


## 3. Methods
The code in the python script '''histograms_comparison.py''' does the following:
Uses```OpenCV``` to design a simple image search algorithm. The script produces histograms of the target image and of all the remaining data. I have chosen image_1305.jpg as my target image. The histograms will not be stored, since the task is to find the most similar images to the target image, by using the ```cv2.compareHist()``` function with the ```cv2.HISTCMP_CHISQR``` metric.
This calculates the distance between the target image's histogram and all other histograms by using the Bhattacharyya distance. The top five images most similar to the target image are stored as a CSV-file in the folder called ```out```alongside the distance metric.

## 4. Usage
This script was made using python 3.10, make sure this is your python version you run the script in. 
### 4.1 Installing packages
From the command line:
Clone this repository to your console by running the command `git clone https://github.com/NiGitaMyrGit/vis_assignment1.git`. This will copy the repository to the location you are currently in.
Then make sure you are located in the main folder, location can be changed by using the command `cd path\to\vis_assignment1`'. From here run the command `bash setup.sh` which will install all the required packages in order to run the script.

### 4.2 Dataset
direct to the folder ```in``` by using  the comman `cd in`(if located  and unzip the dataset by running "unzip flowers.zip"
The dataset is a collection of over 1000 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford, and full details of the data can be found [here](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/).

### 4.3
Still located in the main folder run the script with the command `python3 src\histograms_comparison.py`
## 5. Results - discussion
The CSV-file in the folder `out` contains a data-table with the top-5 most similiar images with the bin-count set to 16. The first image in the file is the target_image itself, which logically has the accuracy of 0.0
I tried meddling with the bin count to get a higher accuracy-rate. Initially I tried with 256, but it gave me better results to go lower. 16 bins ended up giving me the highest accuracy rate. With my human eyes I must admit I cannot tell apart how similiar each image is or not, except for image_1322.jpg which is the closest to the target_image with an accuracy score of 0.21808996400965. This makes sense, since the image is the same, with the only difference being that image_1322.jpg has a logo placed on top of it.

