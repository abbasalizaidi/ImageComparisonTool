'''This program compares and calculates
the difference (score) between two images
input - csv file and output - csv file'''
import argparse
import csv
import math
import sys
import time
from PIL import Image, ImageChops

# pylint: disable=C0103,R0914

def calculate_rms(im1, im2):  ## calculate rms
    """Calculate the root-mean-square difference between two images"""
    diff = ImageChops.difference(im1, im2)
    histogram = diff.histogram()
    square = (value * ((idx % 256) ** 2) for idx, value in enumerate(histogram))
    sum_of_squares = sum(square)
    rms = math.sqrt(sum_of_squares / float(im1.size[0] * im1.size[1]))
    return rms


def image_comparison(src_file, dest_file):
    """Compare the images listed in input csv file
        and outputs the score,elapsed time along with it
        into the output csv file"""
    try:
        with open(str(src_file), mode='r') as f, open(str(dest_file), mode="w") as csv_file:
            fieldnames = ["Image1", "Image2", "Similar", "Elapsed"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            reader = csv.reader(f)
            image_list = list(reader)
            for item in range(1, len(image_list)):
                src = Image.open(image_list[item][0])
                dest = Image.open(image_list[item][1])
                start_time = time.time()
                score = calculate_rms(src, dest)
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 4)
                writer.writerow({"Image1": image_list[item][0], "Image2": image_list[item][1],
                                 "Similar": score, "Elapsed": elapsed_time})
    except IOError as exception:
        if exception.strerror == "No such file or directory":
            print(f"Please check the file exists or not - {exception.strerror}")
        else:
            print(f"Here is the Error - {exception.strerror}")


if __name__ == "__main__":
    # Argument Parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", type=str, help="Path to source file")
    parser.add_argument("--dest", type=str, help="Path for destination file")
    args = parser.parse_args()
    if len(sys.argv) < 5:
        print("Too few Arguments!!")
        print("Check the usage using --help flag")
        sys.exit(1)
    else:
        image_comparison(args.src, args.dest)
