# OCR and Keyword Search Web Application

This web application performs Optical Character Recognition (OCR) on uploaded images containing text in both Hindi and English, 
and provides a keyword search functionality.

## Setup

1. Install the required dependencies:
   pip install -r requirements.txt
   This contains crucial libraries like transformers, gradio, pillow, tesseract, pytesseract

2. Install Tesseract OCR:
  For Windows,
  Download and install from https://github.com/UB-Mannheim/tesseract/wiki   

3. Update the tesseract path in script (this was not needed while deploying to Hugging Face Space but had to use it while running it locally on my machine)

## Running Locally

To run the application locally:
python app.py

## Deployment

To deploy on Hugging Face Spaces:

1. Created a new Space on Hugging Face.
2. While creating space, I set the Space SDK to Gradio
3. Upload the `app.py` file and created `requirements.txt` and `packages.txt` for libraries and packages respectively

## Usage

1. Upload an image containing Hindi and English texts.
2. Enter a keyword to search within the extracted text.
3. The application will display the extracted text and search results.

Note: The OCR accuracy may vary depending on the image quality. Might get incorrect readings if the image has hazy words.
