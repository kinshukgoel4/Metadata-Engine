# Import necessary libraries
import cv2
import torch
from tqdm import tqdm
from PIL import Image
import numpy as np
import json
import os


# Define a class called Engine to process the video and detect people
class Engine:
    
    def __init__(self, video_path, metadata_dir):
        # Initializes the Engine class with the video path and metadata directory
        self.video_path = video_path
        self.metadata_dir = metadata_dir
        # Loads the yolov5s model from the ultralytics hub and sets the object to self.model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        # Initializes the VideoCapture object with the video path and sets the object to self.vidcap
        self.vidcap = cv2.VideoCapture(self.video_path)
        # Gets the frame rate of the video and sets it to self.fps
        self.fps = self.vidcap.get(cv2.CAP_PROP_FPS)
        # Gets the number of frames in the video and sets it to self.num_frames
        self.num_frames = int(self.vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        # Gets the width of the frames and sets it to self.width
        self.width = int(self.vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # Gets the height of the frames and sets it to self.height
        self.height = int(self.vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # Sets the codec used for the video to self.codec
        self.codec = cv2.VideoWriter_fourcc(*'mp4v')

     # Method to detect people in each frame of the video and save metadata
     def detect_people(self):
        # Loops through each frame in the video
        for i in tqdm(range(self.num_frames)):
            # Reads the frame from the video and converts it to a PIL Image object
            success, image = self.vidcap.read()
            if not success:
                break
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            # Runs the yolov5s model on the image and gets the bounding boxes for each detected object
            results = self.model(image, size=640)
            boxes = results.xyxy[0][:, :4].cpu().numpy().tolist()
            num_objects = len(boxes)
            # Creates a dictionary to store metadata for the current frame
            metadata = {
                "frame_number": i,
                "boxes": boxes,
                "num_objects": num_objects,
                "frame_width": self.width,
                "frame_height": self.height,
                "fps": self.fps,
                "codec": self.codec
            }
            # Saves the metadata dictionary to a json file
            metadata_file = os.path.join(self.metadata_dir, f"metadata_{i}.json")
            with open(metadata_file, 'w') as outfile:
                json.dump(metadata, outfile)

    def run(self):
        # Runs the detect_people method to detect objects in the video frames and save metadata for each frame
        self.detect_people()

# Define a list of video paths and metadata directories

#Please define the appropriate video paths as per below given example
video_paths = ["path\to\video1.mp4", "path\to\video2.mp4", "path\to\video3.mp4"]

#Please mention the appropriate directories to save metadata as per below given example
metadata_dirs = [r"path\to\metadata1",r"path\to\metadata1",r"path\to\metadata1"]

# Loop through each video path and run the detection process using the Engine class
for video_path, metadata_dir in zip(video_paths, metadata_dirs):
    # Creates the metadata directory if it doesn't exist
    metadata_dir = os.path.join(os.getcwd(), metadata_dir)
    os.makedirs(metadata_dir, exist_ok=True)
    # Creates an instance of the Engine class and runs it
    engine = Engine(video_path, metadata_dir)
    engine.run()

