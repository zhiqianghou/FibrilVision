
# FibrilVision

## Description
An automated software for analyzing transmission electron microscope images of cross-sectioned materials with fibril structures. The software extracts fibril length and density and generates an interactive dashboard to visualize data trends over time with customizable daily or weekly updates.

## Features
- Import images from customer's AWS cloud database
- Image processing using computer vision techniques
- Extract fibril length and density from 50,000X magnification images
- NLP to obtain lot number from file names
- Interactive dashboard for data visualization with daily or weekly updates

## Data

The dataset used in this project is obtained from the EMPIAR with full name of Eelectron Microscopy Public Image Archive.[EMPIAR-11418](https://www.ebi.ac.uk/empiar/EMPIAR-11418/). 
The original 5.8GB cell images are in .tif format and each with size of 24MB, here to save my hard drive and with aim to show the computational pipeline, I personally only manually downloaded 7 images and converted into .jpeg format. The image names are reformated with time and lot number for future Dashboard visualizaiton purpose.


## AWS Connection and Image Downloading

I have a Python script to connect to an AWS S3 bucket and download images. The script is located in the `src/aws_connection` directory with name download_images_from_s3.py



## Installation
(Provide instructions on setting up the project environment, including any necessary dependencies or libraries.)

## Usage
(Provide a step-by-step guide on how to use the software, including input data requirements, configuration settings, and any available options.)

## Contributing
(Guide contributors on how to report issues, submit pull requests, or help improve the project.)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for the full license text.

Copyright (c) 2023 Mark-Hou


 # FibrilVision
An automated software for analyzing transmission electron microscope images of cross-sectioned materials with fibril structures. The software extracts fibril length and density, and generates an interactive dashboard to visualize data trends over time with customizable daily or weekly updates
