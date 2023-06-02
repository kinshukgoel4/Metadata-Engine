#Import necessary libraries including engine.py
from flask import Flask, render_template, request, send_file
import os
from engine import Engine

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-video', methods=['POST'])
def process_video():
    # Check if a video file was uploaded
    if 'video' not in request.files:
        return 'No video file uploaded.', 400

    video_file = request.files['video']
    if video_file.filename == '':
        return 'Invalid video file.', 400

    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
    video_file.save(video_path)

    # Process the video and generate metadata
    engine = Engine(video_path, app.config['UPLOAD_FOLDER'])
    engine.run()

    metadata_file = os.path.join(app.config['UPLOAD_FOLDER'], 'metadata.json')

    return f'Video processing complete. Metadata generated.'

@app.route('/download-metadata')
def download_metadata():
    metadata_file = os.path.join(app.config['UPLOAD_FOLDER'], 'metadata.json')

    # Check if the metadata file exists
    if not os.path.exists(metadata_file):
        return 'Metadata file not found.', 404

    # Send the metadata file as a response for download
    return send_file(metadata_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
