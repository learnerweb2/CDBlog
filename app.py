from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Serve the static index.html file
@app.route('/')
def home():
    return send_from_directory(os.getcwd(), 'index.html')

# Serve images from the main folder (e.g., image1.jpg, image2.jpg)
@app.route('/<path:filename>')
def serve_image(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == '__main__':
    app.run(debug=True)
