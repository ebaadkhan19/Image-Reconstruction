# Image Reconstructor

## Overview
This project implements an Image Reconstructor using Python, TensorFlow, and Streamlit. The model reconstructs images, specifically aimed at improving or restoring the quality of uploaded images. Users can upload images through a web interface and receive a reconstructed output.

## Features
- **Image Reconstruction**: Restores uploaded images to their intended quality.
- **User-Friendly Interface**: Built with Streamlit for easy image uploads and results display.
- **Grayscale Conversion**: Processes images by converting them to grayscale before reconstruction.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries:
  ```bash
  pip install streamlit tensorflow pillow numpy
Installation
Clone the repository:
git clone https://github.com/your-username/image-reconstructor.git
cd image-reconstructor
Ensure you have your trained model saved in the specified directory (model/mnist_reconstructor).
Usage
To run the Streamlit application, execute the following command in your terminal:
streamlit run app.py
Performance Evaluation
The effectiveness of the image reconstructor can be qualitatively assessed by comparing the original and reconstructed images. Further improvements may involve adding quantitative metrics for evaluation.
License
This project is licensed under the MIT License - see the LICENSE file for details.
