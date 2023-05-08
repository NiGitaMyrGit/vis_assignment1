# load packages
import os
import sys
sys path.append(".")
import numpy as np
import cv2 as cv 
import csv


# load data, remember to unzip the dataset first
Def load_data():
    flower_dir = os.path.join("assignment1-simple-image-search-NiGitaMyrGit", "in", "flowers")
    # Set the target image
    target_filename = os.path.join(flower_dir, "image_1305.jpg")
    target_image = cv.imread(target_filename)
    return flower_dir, target_image

def make_histograms(target_image, flower_dir):
    # Calculate the histogram of the target image
    target_hist = cv.calcHist([target_image], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    # Create a list to store the distances between the target histogram and each image histogram
    distances = []
    # Loop over every image in the flower_dir and calculate the histogram
    for filename in os.listdir(flower_dir):
        # Check if the filename is the same as the target filename
        if filename == os.path.basename(target_filename):
            continue  # skip this image and continue with the next one
        # Read the image
        image = cv.imread(os.path.join(flower_dir, filename))
        # Calculate the histogram of the image
        hist = cv.calcHist([image], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
        
        # Calculate the distance between the target histogram and the image histogram
        # using the Bhattacharyya distance
        distance = cv.compareHist(target_hist, hist, cv.HISTCMP_BHATTACHARYYA)
        
        # Add the filename and distance to the distances list
        distances.append((filename, distance))

    # Sort the distances list by distance in ascending order
    distances.sort(key=lambda x: x[1])
    return distance, distances

# save data
def top5_list(distance, distances):
    # Create a list to store the top 5 images
    top_5 = []

    # Add the target image to the top 5 list with a distance of 0.0
    top_5.append((os.path.basename(target_filename), 0.0))

    # Loop over the 5 images with the smallest distance and add them to the top 5 list
    for i in range(5):
        filename, distance = distances[i]
        top_5.append((filename, distance))
    return top_5



def main():
    #load data
    flower_dir, target_image = load_data()
    #vectorize
    distance, distances = make_histograms(target_image, flower_dir)
    # run classifier
    y_pred, classifier = logreg_model(X_train_feats, X_test_feats, y_train)


    with open("similar_images.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Filename", "Distance"])
            for item in top_5:
                writer.writerow(item)
    
# calling main function
if __name__== "__main__":
    main()