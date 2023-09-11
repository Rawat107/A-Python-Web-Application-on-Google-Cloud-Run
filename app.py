from flask import Flask, render_template, request, jsonify
from deepface import DeepFace
import os

app = Flask(__name__)

registered_faces = {}  # Initialize an empty dictionary

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    image = request.files['image']

    # Check if the image is already registered with the same name
    if name.lower() in registered_faces:
        return f"Face already registered with the name: {name}."
    
    # Build the path for saving the image in the 'uploads' folder
    image_path = os.path.join('uploads', f'{name.lower()}.jpg')
    image.save(image_path)
    
    registered_faces[name.lower()] = image_path
    
    return "Face registered successfully."


@app.route('/recognize', methods=['POST'])
def recognize():
    image = request.files['image']
    image_path = 'temp.jpg'
    image.save(image_path)
    
    recognized_name = None
    
    for name, path in registered_faces.items():
        try:
            recognized_face = DeepFace.verify(image_path, path, enforce_detection=False)
        except ValueError as e:
            continue
        
        if recognized_face and recognized_face['verified']:
            recognized_name = name
            break
    
    if recognized_name:
        result = f"Recognition complete: This is a picture of {recognized_name.capitalize()}."
    else:
        result = f"This is an image of a person."
    
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
