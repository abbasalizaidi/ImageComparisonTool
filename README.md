# ImageComparisonTool

A Python tool to compare images listed in a CSV file and calculates similarity score of two images.

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




