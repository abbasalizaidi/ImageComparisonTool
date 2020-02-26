'''This program compares and calculates
the difference (score) between two images
input - csv file and output - csv file'''
import csv
import math
import time
import argparse
from PIL import Image, ImageChops


# pylint: disable=C0103

def image_comparison(im1, im2):
    """Calculate the root-mean-square difference between two images"""
    diff = ImageChops.difference(im1, im2)
    histogram = diff.histogram()
    square = (value * ((idx % 256) ** 2) for idx, value in enumerate(histogram))
    sum_of_squares = sum(square)
    rms = math.sqrt(sum_of_squares / float(im1.size[0] * im1.size[1]))
    return rms


if __name__ == "__main__":
    # Open the files to read and write
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", type=str, help="Path to source file", default = "image_database.csv")
    parser.add_argument("--dest", type=str, help="Path for destination file", default="output.csv")
    args = parser.parse_args()
    try:
        with open(str(args.src), mode='r') as f, open(str(args.dest), mode="w") as csv_file:
            fieldnames = ["Image1", "Image2", "Similar", "Elapsed"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            reader = csv.reader(f)
            image_list = list(reader)
            for item in range(1, len(image_list)):
                src = Image.open(image_list[item][0])
                dest = Image.open(image_list[item][1])
                start_time = time.time()
                score = image_comparison(src, dest)
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 4)
                writer.writerow({"Image1": image_list[item][0], "Image2": image_list[item][1],
                                 "Similar": score, "Elapsed": elapsed_time})
    except IOError as exception:
        if exception.strerror == "No such file or directory":
            print(f"Please check the file exists or not! - {exception.strerror} ")
