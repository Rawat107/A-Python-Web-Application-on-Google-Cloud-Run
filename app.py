from flask import Flask

app = Flask(__name__)

registered_faces = {
    "male": "faces/man_face.jpg",
    "female": "faces/female_face.jpg",
    "crowd": "faces/crowd.jpg"
    # Add more registered faces here
}


@app.route('/')
def hello():
  return "Hello, this is the face recoginition app!"


@app.route('/register', methods=['POST'])
def register_face():
    name = request.form.get('name')
    image_path = request.form.get('image_path')
    
    registered_faces[name] = image_path
    return f"Face for {name} registered successfully."


@app.route('/recognize', methods=['POST'])
def recognize_face():
    image_path = request.form.get('image_path')
    
    recognized = False
    for name, registered_image_path in registered_faces.items():
        result = DeepFace.verify(image_path, registered_image_path)
        if result['verified']:
            recognized = True
            return f"Recognized: {name}"
    
    if not recognized:
        return "Face not recognized."

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port=8080)
