#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# In[11]:


import gradio as gr
import pytesseract
from PIL import Image
import re
import os
import sys

# Set Tesseract path if needed (uncomment and modify if Tesseract is not in PATH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image):
    try:
        # Ensure the image is in RGB mode
        image = image.convert('RGB')
        # Perform OCR with Tesseract (supports both English and Hindi)
        text = pytesseract.image_to_string(image, lang='eng+hin')
        return text
    except Exception as e:
        return f"OCR Error: {str(e)}"

def search_text(text, keyword):
    if not keyword:
        return "Please enter a keyword to search."
    
    # Perform case-insensitive search
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    matches = pattern.finditer(text)
    
    # Highlight matches and get surrounding context
    results = []
    for match in matches:
        start = max(0, match.start() - 20)
        end = min(len(text), match.end() + 20)
        context = text[start:end]
        highlighted = pattern.sub(f"<mark>{match.group()}</mark>", context)
        results.append(f"...{highlighted}...")
    
    if results:
        return "<br><br>".join(results)
    else:
        return "No matches found."

def process_image(image, keyword):
    if image is None:
        return "Please upload an image.", ""
    
    extracted_text = ocr_image(image)
    search_results = search_text(extracted_text, keyword) if "OCR Error" not in extracted_text else ""
    
    return extracted_text, search_results

# Debug information
print(f"Python version: {sys.version}")
print(f"Tesseract version: {pytesseract.get_tesseract_version()}")
print(f"Tesseract path: {pytesseract.pytesseract.tesseract_cmd}")

# Create the Gradio interface
iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(label="Search Keyword")
    ],
    outputs=[
        gr.Textbox(label="Extracted Text"),
        gr.HTML(label="Search Results")
    ],
    title="OCR and Keyword Search",
    description="Upload an image with English text, and optionally provide a keyword to search within the extracted text."
)

# Launch the app
iface.launch(share=True)

