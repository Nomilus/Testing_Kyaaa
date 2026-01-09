from flask import Flask, request
import os
from io import BytesIO

app = Flask(__name__)


a = 'uploads/Kisaki_00.png'

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file', 400
    
    input_file = BytesIO(file.read())

    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    # file.seek(0)
    file.save(filename)

    return 'File successfully uploaded and saved', 200

if __name__ == '__main__':
    app.run(debug=True)
