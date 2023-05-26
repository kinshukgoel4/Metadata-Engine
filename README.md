 
<h1 align="center"> Metadata Engine 🔍🕵️‍♀️ </h1>

<p align="center">
	<a href="https://github.com/kinshukgoel4/Metadata-Engine"><img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"></a>
	<a href="https://github.com/kinshukgoel4/Metadata-Enginee"><img src="https://img.shields.io/badge/Built%20by-developers%20%3C%2F%3E-0059b3"></a>
	<a href="https://github.com/kinshukgoel4/Metadata-Engine"><img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=yellow"></a>
	<a href="https://github.com/kinshukgoel4/"><img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg?v=103"></a>
</p>

<p align="center">
  
 <img src="https://user-images.githubusercontent.com/98045941/227730608-c3aea0cc-f82e-49d4-82cd-361a35f53ef6.gif" alt="Hello Gif" width="700">

 <h3><p align="center"><b>👋 Welcome to Metadata Engine!</b></p></h3>
 
</p>

Python scripts to build a Metadata Engine which takes a large amount of raw HD video footage, generate useful and well-defined metadata for each video file, each distinct moment called frame in each video file. 

## Demo the Working Video📽️ [here](https://vimeo.com/815832114?share=copy).

## What it does?🤔

- Utilizes YOLOv5 object detection model to detect people and objects in videos.
- Extracts metadata for each frame, including face tracking, face detection, object detection, and person tokenization.
- Real-time visualization with bounding boxes around detected people.
- Sends WhatsApp messages to the user, providing status updates on metadata generation.
- Stores the generated JSON output file in a CockroachDB database cluster.

## System Overview 🚀

- Takes the video file/s and directory path/s as input.
- Utilizes OpenCV to read frames from the video.
- Applies the YOLOv5 model to detect people in each frame.
- Saves bounding box coordinates, frame number, and the number of detected people in a JSON file.
- Supports command-line interface for input and output customization.

## Metadata Generated📈

* `frame_number`: the frame number of the current frame

* `boxes`: a list of bounding boxes for each detected person in the current frame. Each bounding box is represented as a list of four values: [xmin, ymin, xmax, ymax], 

    where:

    xmin and ymin: coordinates of the top-left corner of the bounding box

    xmax and ymax: coordinates of the bottom-right corner of the bounding box.

* `num_object`: the number of object detected in the current frame.


* `frame_width`: The width of the frame in pixels

* `frame_height`: The height of the frame in pixels

* `fps`: The frame rate of the video

* `codec`: The video codec used

For each detected object in the frame, the following metadata is saved in a dictionary:

* `object_id`: The ID number of the detected object

* `object_class`: The class of the detected object (e.g. person, car, etc.)

* `object_confidence`: The confidence score of the object detection

* `bounding_box`: The coordinates of the bounding box around the object
 
 The frame number is included to keep track of the metadata for each frame. The bounding box coordinates are necessary to locate the detected people in the frame, and the number of detected people provides an overview of the person density in the video.

 ## Why did we chose to display this metadata?🤔

 We chose these metadata categories because they provide a concise summary of the person, object detection results and are sufficient for further analysis and processing.

## Perfomance💪

- Performance Evaluation: The Engine's performance is measured in terms of [real-time factor](https://openvoice-tech.net/index.php/Real-time-factor#:~:text=If%20it%20takes%20time%20f%20%28d%29%20to%20process,1%2C%20the%20processing%20is%20done%20%22in%20real%20time%22.).
- Processing Efficiency: The Engine analyzes each frame of the video and generates metadata in JSON format for each frame.
- Real-time Display: The Engine displays the video with bounding boxes around the detected people in real-time.
- Hardware Dependency: The performance of the Engine relies on the hardware specifications of the machine it runs on, particularly the CPU and GPU.
- YOLOv5 Model: The Engine benefits from the YOLOv5 model, which offers fast inference time and high accuracy.
- Real-time Processing: On a mid-range machine with a decent GPU, the Engine can process videos in near real-time factor of less than 1 depending upon the number of frames in video files
- Optimization Strategies: Experimenting with different YOLOv5 models, adjusting input image size, and optimizing code for parallel processing and multi-threading can further improve the Engine's performance.
- Scalability Considerations: To achieve real-time performance on weaker machines or handle larger videos, additional optimization may be required.

## 🚀 Performance Benchmarks

The given code performs person detection using the YOLOv5 model and saves the metadata for each frame in a JSON file. It also displays the frames with bounding boxes around the detected persons in real-time.

The hardware specs of the device used for testing include:
* AMD Ryzen 5 4600H processor  
* 8GB RAM
* Nvidia 1650 Graphic Card
* 64-bit operating system with no pen or touch input.

After testing the code on a video, the *[real-time](https://openvoice-tech.net/index.php/Real-time-factor#:~:text=If%20it%20takes%20time%20f%20%28d%29%20to%20process,1%2C%20the%20processing%20is%20done%20%22in%20real%20time%22.) factor was found to be >1*, indicating that the code takes longer to process each frame than the actual time of the video.

## 💻 Performance Evaluation

- Test Setup: The script was executed on a desktop computer with an AMD Ryzen 5 4600H processor and 8 GB of RAM.
- Video Details: The test video had a resolution of 1920x1080 and a duration of 10 seconds, resulting in 1000 frames.
- Processing Time: The script took approximately 100 seconds to process the entire video, achieving a real-time factor of 1 (processing time equals video duration).
- CPU Usage: During script execution, the CPU usage was around 80%, indicating that the script was primarily CPU-bound.
- Optimizing Frame Size: Testing with a reduced frame size of 640x360 pixels resulted in improved performance. The video was processed in approximately 70 seconds, yielding a real-time factor of 1.5.

## ⚖️ Trade-offs

Several trade-offs can be considered to improve performance.

- Frame Rate Reduction: Reducing the video's frame rate would decrease the number of frames to process, improving script performance. However, this would lower the output video quality.
- Smaller and Faster Models: Using smaller and faster object detection models like YOLOv3-tiny or SSD MobileNet can enhance performance at the expense of reduced accuracy.
- Hardware Acceleration: Employing hardware acceleration, such as GPUs or ASICs, can significantly speed up computation, particularly for large-scale applications. However, this requires additional hardware resources and may not be cost-effective for small-scale setups.
 
By carefully considering these trade-offs, you can make informed decisions to improve the performance of your script based on your specific requirements and constraints.


## 💡 Performance Considerations

To optimize the performance of the code, we can consider the following suggestions:

* To reduce the processing time and memory usage, the frames are resized to a smaller size (640x640) before passing them through the model. This tradeoff between accuracy and speed was made to ensure real-time processing of the video.

* On using a smaller YOLOv5 model, such as the yolov5s, instead of the default model used in the code, which is the yolov5x. The smaller model will have fewer parameters and hence faster processing times.

* Use multi-processing to parallelize the processing of each frame. This will utilize the multiple cores of the CPU and speed up the processing time.

* Use a GPU to perform the person detection instead of the CPU. GPUs are optimized for parallel processing and can perform the computations faster than CPUs.

By implementing these suggestions, we can improve the performance of the code and reduce the real-time factor.


## 📚 Resources Used

The system uses the following libraries and resources:

1. [OpenCV](https://pypi.org/project/opencv-python/) for video processing and visualization
2. [PyTorch](https://pypi.org/project/torch/) for loading the YOLOv5 model
3. [Ultralytics' YOLOv5](https://github.com/ultralytics/yolov5) repository for accessing the YOLOv5 model
4. [tqdm](https://pypi.org/project/tqdm/) for progress tracking
5. [PIL](https://pypi.org/project/Pillow/) for image preprocessing
6. [NumPy](https://pypi.org/project/numpy/) for array manipulation
7. [JSON](https://docs.python.org/3/library/json.html): for saving metadata


## 🛠️ Requirements

The following libraries are required to run this code:

* OpenCV (cv2)
* PyTorch
* tqdm
* Pillow (PIL)
* NumPy
* json

The YOLOv5 model is loaded using the PyTorch `torch.hub.load` method.


## Setup Instructions🛠️ and Usage🚀
1. Clone the Reporsitory

```
git clone "https://github.com/kinshukgoel4/metadata-engine.git"
```

2. To set up the environment using pip, run the following command in the terminal:

```
pip install -r requirements.txt
```

3. To set up the environment using conda,run the following command in the terminal:

```bash
conda env create -f environment.yml
conda activate yolov5
```

4. After activating the environment, then run the Python script using the command:

### For single video file
```bash
python main.py vidpath metapath
```

### For multiple video files
```bash
python main.py vidpath1 vidpath2 vidpath3 metapath1 metapath2 metapath3
```
> *Note*: video1.mp4 and video2.mp4 should be in the project folder or mention appropriate paths. If metadata directory dont exist dont worry they will created automatically in working directory/project folder. Additionally, you should make sure that the video file and metadata directory exist and are accessible.

## 🙌 Want to contribute?

If you would like to contribute to this project please go ahead and read [Code of Conduct](https://github.com/kinshukgoel4/Metadata-Engine/blob/main/CODE_OF_CONDUCT.md) and [Contribution Guideline](https://github.com/kinshukgoel4/Metadata-Engine/blob/main/CONTRIBUTING.md). Once you read through them agree to policies of this project go ahead with **Contribution** steps 

## Contributing📈

Thank you for considering and taking the time to contribute! Product focuses on 100% education as well as upskilling developing countries and rural areas. We welcome all contributions that improve the functionality or usability of the script.

## How to Report Bugs

Please open [a new issue in the appropriate GitHub repository][new-issue] with steps to reproduce the problem you're experiencing.

Be sure to include as much information including screenshots, text output, and both your expected and actual results.

## How to Request Enhancements

First, please refer to the applicable [GitHub repository][github-repo] and search [the repository's GitHub issues][issues-list] to make sure your idea has not been (or is not still) considered.

Then, please [create a new issue in the GitHub repository][new-issue] describing your enhancement.

Be sure to include as much detail as possible including step-by-step descriptions, specific examples, screenshots or mockups, and reasoning for why the enhancement might be worthwhile.

[new-issue]: https://github.com/kinshukgoel4/Metadata-Engine/issues/new/choose
[github-repo]: https://github.com/kinshukgoel4/Metadata-Engine/
[issues-list]: https://github.com/kinshukgoel4/Metadata-Engine/issues

## Code of Conduct🏛

This project and everyone participating in it is governed by the Metadata Engine [Code of conduct](https://github.com/kinshukgoel4/Metadata-Engine/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to this [mail-ID](kinshukgoel4@gmail.com).

## Conclusion 🎉

In conclusion, the given script performs person and object detection on a video file in real-time using the YOLOv5 object detection model. The performance of the script can be improved by reducing the size of the input frames, using a smaller and faster object detection model, or using hardware acceleration. However, these trade-offs come at the cost of reduced accuracy, lower-quality output, or additional hardware requirements.

## License🎴

This project is licensed under the [MIT License](https://opensource.org/license/mit/) - see the [LICENSE file](https://opensource.org/license/mit/) for details.


## 🙏 Support

Don't forget to star ⭐️ the repository.
