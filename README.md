## Preliminaries:
in the command line make sure you are located in the main folder. From here start by running bash setup.sh
afterwards direct to the folder "in" (by using cd in/) and unzip the dataset by running "unzip flowers.zip"

This assignment is using ```OpenCV``` to design a simple image search algorithm.


The dataset is a collection of over 1000 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford, and full details of the data can be found [here](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/).


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

|Filename|Distance]
|---|---|
|target|0.0|
|filename1|---|
|filename2|---|

## Objective

This assignment is designed to test the ability to:

1. Working with larger datasets of images
2. Extract structured information from image data using ```OpenCV```
3. Quantaitively compare images based on these features, performing *distant viewing*
