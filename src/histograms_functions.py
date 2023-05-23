#!/usr/bin/env python3
import os
import sys
import numpy as np
import cv2
import csv
import fnmatch

def make_histograms():
    #load and preprocess data
    flower_dir = os.path.join("in", "flowers")
    target_filename = os.path.join("in", "flowers", "image_1305.jpg")
    # Set the target image
    target_image = cv2.imread(target_filename)
    #calculating the histogram for the target image
    target_hist = cv2.calcHist([target_image], [0, 1, 2], None, [16, 16, 16], [0, 256, 0, 256, 0, 256])
    # Create a list to store the distances between the target histogram and each image histogram
    distances = []
    # Loop over every image in the flower_dir and calculate the histogram
    for filename in os.listdir(flower_dir):
        if not fnmatch.fnmatch(filename, "*.jpg"):
            continue
        # Read the image
        image = cv2.imread(os.path.join(flower_dir, filename))
        # Calculate the histogram of the image
        hist = cv2.calcHist([image], [0, 1, 2], None, [16, 16, 16], [0, 256, 0, 256, 0, 256])
        
        # Calculate the distance between the target histogram and the image histogram
        # using Bhattacharyya distance, in order to measure the “overlap” between the two histograms:
        distance = cv2.compareHist(target_hist, hist, cv2.HISTCMP_BHATTACHARYYA)
        
        # Add the filename and distance to the distances list
        distances.append((filename, distance))
    # Sort the distances list by distance in ascending order
    distances.sort(key=lambda x: x[1])
    # Create a list to store the top 5 images
    top_5 = []
    # Loop over the 5 images with the smallest distance and add them to the top 5 list
    for i in range(6):
        filename, distance = distances[i]
        top_5.append((filename, distance))
    with open(os.path.join("out", "similar_images_bins16.csv"), "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Filename", "Distance"])
        for item in top_5:
            writer.writerow(item)
        
# calling main function
if __name__== "__main__":
    make_histograms()