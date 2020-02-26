# ImageComparisonTool

A Python CLI tool to compare images listed in a CSV file and calculates similarity score of two images along with elapsed time.

## How this tool can be useful?

If you have programmatically find out similar images out of N set of images present whose paths are mentioned in a form of a csv file.

And your file looks like this

|  Image1           | Image2            |
|-------------------|-------------------|
| images/file1.jpg  | images/file2.jpg  |
| images/file3.jpg  | images/file4.jpg  |
| images/file5.png  | images/file6.png  |
| images/file8.png  | images/file9.png  |
| images/file10.gif | images/file11.gif |
| images/file3.jpg  | images/file4.jpg  |

Note : Path can be anywhere on your disk.

The script by default creates a file in the current working directory with name output.csv if not specified explicitly.

| Image1            | Image2            | Similar           | Elapsed |
|-------------------|-------------------|-------------------|---------|
| images/file1.jpg  | images/file2.jpg  | 38.3941134213051  | 0.019   |
| images/file3.jpg  | images/file4.jpg  | 0.0               | 0.0439  |
| images/file5.png  | images/file6.png  | 65.16600491471311 | 0.0843  |
| images/file8.png  | images/file9.png  | 66.34622945969112 | 0.0731  |
| images/file10.gif | images/file11.gif | 13.29321011760659 | 0.0007  |
| images/file3.jpg  | images/file4.jpg  | 0.0               | 0.0445  |


## Installation

### Prerequisites

#### Setup Python Virtual Env

You need to install python virtualenv to make this program run in an isolated environment with its own version of modules.

For instructions setting up the same on (MacOs/Windows/Linux), please follow the link below

https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

#### Clone the repository and activate virtual environment using commands below

-  ``` git clone https://github.com/abbasalizaidi/ImageComparisonTool/ ```
-  ``` virtualenv ImageComparisonTool ```
-  ``` cd ImageComparisonTool/ ```
-  ``` source bin/activate ```

#### Install the requirements using the requirement files
-  ``` pip3 install -r requirements.txt ```

## Design 

#### How can I possibly compare the image without seeing it?

Yes, you can! Actually images are essentially bitmaps and bitmaps are stored in the form of pixels in the computers memory. So, if we are able to make some computation around the pixels, then we can play around with pictures with the help of computer programming.

#### Say No to Checksums when it comes to images
We can use the checksums to compare the images but we can cannot know how similar these two images are with that approach.

#### RMSE to the Rescue (Root Mean Square Error)

A blog post actually described, calculating root mean square error value can help in identfying images which are not similar and those which aren't on how much similar they are.

                         Lower the value of RMSE ----> More similar images are!

Note :- Similar images has RMSE value as 0.

So lets take two images, Image1 and Image2. If we can serialize these images into a format on which we can calculate the RMSE value, we can calculate the score of the images.

Pillow is a python library which has modules named Image and ImageChops. Further, these modules contains methods which can take images as arguments and can calculate the difference between the images. For more information 
  
  - https://pillow.readthedocs.io/en/stable/

So, all we need to do is to process the csv files and extracts the paths and process the images to calculate the root mean square value.

Keeping all these things in mind, I designed a python cli script which takes two arguments --src and --dest (for source and destination csv files respectively) and outputs a file with a score column containing the level of similarity between two images.

#### Add-on
Tool also calculates the elapsed time in comparing the two images. This can help in quantifying the efforts.

## Usage

Prerequisite : Please follow the installation steps

After you have followed the installation steps, you are ready to run the application.

``` python3 image_comparison.py --src image_database.csv --dest output.csv```

The above command will create a file named output.csv which has the following structure

| Image1            | Image2            | Similar           | Elapsed |
|-------------------|-------------------|-------------------|---------|
| images/file1.jpg  | images/file2.jpg  | 38.3941134213051  | 0.019   |
| images/file3.jpg  | images/file4.jpg  | 0.0               | 0.0439  |
| images/file5.png  | images/file6.png  | 65.16600491471311 | 0.0843  |
| images/file8.png  | images/file9.png  | 66.34622945969112 | 0.0731  |
| images/file10.gif | images/file11.gif | 13.29321011760659 | 0.0007  |
| images/file3.jpg  | images/file4.jpg  | 0.0               | 0.0445  |

Note : The elapsed time is in seconds

You can also type --help to check the usage of the command

```
   python3 image_comparison.py --help
   
   usage: image_comparison.py [-h] [--src SRC] [--dest DEST]
   optional arguments:
  -h, --help   show this help message and exit
  --src SRC    Path to source file
  --dest DEST  Path for destination file
```
#### Note:Master branch contains the stable code always!
