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
