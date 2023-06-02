#Import necessary libraries
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
        self.video_path = video_path
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.vidcap = cv2.VideoCapture(self.video_path)
        self.fps = self.vidcap.get(cv2.CAP_PROP_FPS)
        self.num_frames = int(self.vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.width = int(self.vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.codec = cv2.VideoWriter_fourcc(*'mp4v')
        self.metadata_list = []
        self.labels = self.model.module.names if hasattr(self.model, 'module') else self.model.names
        self.metadata_dir = metadata_dir

    def detect_person_and_objects_in_frame(self):
        for i in tqdm(range(self.num_frames)):
            success, image = self.vidcap.read()
            if not success:
                break
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            results = self.model(image, size=640)
            boxes = results.xyxy[0][:, :4].cpu().numpy().tolist()
            num_objects = len(boxes)
            metadata = {
                "frame_number": i + 1,
                "boxes": boxes,
                "num_objects": num_objects,
                "frame_width": self.width,
                "frame_height": self.height,
                "fps": self.fps,
                "codec": self.codec
            }
            class_ids = results.xyxy[0][:, 5].cpu().numpy().tolist()
            objects_metadata = []
            for j, box in enumerate(boxes):
                x1, y1, x2, y2 = box
                obj_class = self.labels[int(class_ids[j])]
                obj_conf = round(float(results.xyxy[0][j][4]), 2)
                obj_metadata = {
                    "object_id": j + 1,
                    "object_class": obj_class,
                    "object_confidence": obj_conf,
                    "bounding_box": [x1, y1, x2, y2]
                }
                objects_metadata.append(obj_metadata)
            metadata["num_objects"] = len(objects_metadata)
            metadata["objects_data"] = objects_metadata
            self.metadata_list.append(metadata)

    def run(self):
        # Runs the detect_person_and_objects_in_frame method to detect person and objects in the video frames and save metadata for each frame
        self.detect_person_and_objects_in_frame()
        # Combines all metadata dictionaries into a single dictionary
        combined_metadata = {
            "num_frames": self.num_frames,
            "metadata": self.metadata_list
        }
        # Saves the combined metadata dictionary to a json file
        metadata_file = os.path.join(self.metadata_dir, "metadata.json")
        with open(metadata_file, 'w') as outfile:
            json.dump(combined_metadata, outfile)

        return metadata_file
   
