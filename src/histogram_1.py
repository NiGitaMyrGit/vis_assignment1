#!/usr/bin/env python3
import os
print(os.getcwd())
import sys
sys.path.append(".")
import numpy as np
import cv2
import csv
import fnmatch

# Set the main directory 'flower_dir' where the files are located
flower_dir = os.path.join("in", "flowers")

# Set the target image
target_filename = os.path.join("in", "flowers", "image_1305.jpg")
target_image = cv2.imread(target_filename)
#calculating the histogram for the target image
target_hist = cv2.calcHist([target_image], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

# Create a list to store the distances between the target histogram and each image histogram
distances = []

# Loop over every image in the flower_dir and calculate the histogram
for filename in os.listdir(flower_dir):
    # Check if the filename is the same as the target filename
    if filename == os.path.basename(target_filename):
        continue  # skip this image and continue with the next one
    if not fnmatch.fnmatch(filename, "*.jpg"):
        continue
    # Read the image
    image = cv2.imread(os.path.join(flower_dir, filename))
    # Calculate the histogram of the image
    hist = cv2.calcHist([image], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    
    # Calculate the distance between the target histogram and the image histogram
    # using Bhattacharyya distance, in order to measure the “overlap” between the two histograms:
    distance= cv2.compareHist(target_hist, hist, cv2.HISTCMP_BHATTACHARYYA)
    
    # Add the filename and distance to the distances list
    distances.append((filename, distance))

# Sort the distances list by distance in ascending order
distances.sort(key=lambda x: x[1])

# Create a list to store the top 5 images
top_5 = []

# Add the target_image to the top 5 list with a distance of 0.0 (since it's the same)
top_5.append((os.path.basename(target_filename), 0.0))

# Loop over the 5 images with the smallest distance and add them to the top 5 list
for i in range(5):
    filename, distance = distances[i]
    top_5.append((filename, distance))

# Save the top 5 list to a CSV file
with open("similar_images.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Filename", "Distance"])
    for item in top_5:
        writer.writerow(item)

''' I have tried meddling with the bin count. 
One of the datatables in the outfolder showcases the results
with an adjusted bin-count of 36 bins instead of the 256
I must admit I with my human eyes at least, cannot really tell apart how similiar each image is or not.
A promising thing is that the exact same picture (image_) '''

'''Furthermore, I wish to understand the functions, I'll get there:
took me a while to understand what was even meant by making functions xD'''

# Help sources:
# Bhattacharyya distance:
# https://pyimagesearch.com/2014/07/14/3-ways-compare-histograms-using-opencv-python/
# fnmatch: https://docs.python.org/3/library/fnmatch.html
# something about lambda functions and very basic lambda calculus:
# https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
# https://www.youtube.com/watch?v=d0yEXKas8xE