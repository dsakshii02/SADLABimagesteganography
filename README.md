# Image Steganography Application

A powerful desktop application that allows you to hide secret text messages within images using steganography and encryption techniques.

## Features

- Hide text messages within PNG images
- Password-protected encryption for enhanced security
- Extract hidden messages from images
- User-friendly graphical interface
- Support for text file input/output
- Secure message embedding and extraction

## Requirements

- Python 3.x
- customtkinter
- cryptosteganography

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/steganography-app.git

Install required packages:
pip install customtkinter cryptosteganography

Run the application:
python DataSteganography.py

To hide a message:
Enter a password
Select an image file (PNG)
Select a text file containing your message
Click "Embed Text into Image"
Choose where to save the output image

To extract a message:
Enter the correct password
Select the image containing the hidden message
Click "Extract Text from Image"
Choose where to save the extracted text
Security Features
Password-based encryption
Secure message embedding
Error handling for incorrect passwords
Support for PNG image format

