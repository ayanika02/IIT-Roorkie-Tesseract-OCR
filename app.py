import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import gradio as gr
import pytesseract
from PIL import Image
import re
import os
import sys

def ocr_image(image):
    try:
        image = image.convert('RGB')
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

print(f"Python version: {sys.version}")
print(f"Tesseract version: {pytesseract.get_tesseract_version()}")
print(f"Tesseract path: {pytesseract.pytesseract.tesseract_cmd}")

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

iface.launch(share=True)

