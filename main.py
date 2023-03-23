# Import necessary libraries
import cv2
import torch
from tqdm import tqdm
from PIL import Image
import numpy as np
import json
# Define a class called Engine to process the video and detect people
class Engine:
    
    def __init__(self, video_path, metadata_dir):
        # Initialize the path of the video and directory to save metadata
        self.video_path = video_path
        self.metadata_dir = metadata_dir
        # Load the YOLOv5 model from ultralytics hub
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        # Open the video and get the frame rate and number of frames
        self.vidcap = cv2.VideoCapture(self.video_path)
        self.fps = self.vidcap.get(cv2.CAP_PROP_FPS)
        self.num_frames = int(self.vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Method to detect people in each frame of the video and save metadata
    def detect_people(self):
        # Loop through each frame of the video
        for i in tqdm(range(self.num_frames)):
            # Read the frame from the video
            success, image = self.vidcap.read()
            if not success:
                break
            # Convert the image to a PIL Image and run it through YOLOv5 model
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            results = self.model(image, size=640)
            # Get the bounding boxes of detected people and save the metadata in a dictionary
            boxes = results.xyxy[0][:, :4].cpu().numpy().tolist()
            metadata = {
                "frame_number": i,
                "boxes": boxes,
                "num_object": len(boxes)
            }
            # Save the metadata in a json file for each frame
            metadata_file = self.metadata_dir[:-5] + f"_frame_{i}.json"
            with open(metadata_file, 'w') as outfile:
                json.dump(metadata, outfile)

    # Method to run the detection process
    def run(self):
        self.detect_people()
