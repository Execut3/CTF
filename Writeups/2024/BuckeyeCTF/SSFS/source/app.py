from flask import Flask, request, render_template, send_file
from uuid import uuid4
import os
import hashlib

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 # 1MB

file_exts = {}

@app.route('/')
def index():
    return render_template('index.html')

def clear_uploads():
    upload_dir = 'uploads'
    if not os.path.exists(upload_dir):
        os.mkdir(upload_dir)

    files = os.listdir(upload_dir)
    if len(files) > 50:
        for file in files:
            os.remove(os.path.join(upload_dir, file))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    ext = file.filename.split('.')[-1]

    if not file:
        return {'status': 'error', 'message': 'No file uploaded'}
    
    if ext not in ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp']:
        return {'status': 'error', 'message': 'Invalid file type'}
    
    clear_uploads()

    file_id = str(uuid4())
    file_exts[file_id] = ext

    os.makedirs('uploads', exist_ok=True)
    
    with open(f'uploads/{file_id}', 'wb') as f:
        f.write(file.read())

    return {'status': 'success', 'message': 'File uploaded successfully', 'id': file_id}

@app.route('/search/<path:file_id>')
def search(file_id):
    print('uploads/' + file_id)
    if not os.path.exists('uploads/' + file_id):
        return {'status': 'error', 'message': 'File not found'}, 404

    return {'status': 'success', 'message': 'File found', 'id': file_id}

def filter_file_id(file_id : str):
    if len(file_id) > 36: # uuid4 length
        return None
    
    return file_id

@app.route('/download/<path:file_id>')
def download(file_id):
    file_id = filter_file_id(file_id)

    if file_id is None:
        return {'status': 'error', 'message': 'Invalid file id'}, 400

    if not os.path.exists('uploads/' + file_id):
        return {'status': 'error', 'message': 'File not found'}, 404
    
    if not os.path.isfile('uploads/' + file_id):
        return {'status': 'error', 'message': 'Invalid file id'}, 400

    return send_file('uploads/' + file_id, download_name=f"{file_id}.{file_exts.get(file_id, 'UNK')}")

if __name__ == '__main__':
    app.run(debug=True)