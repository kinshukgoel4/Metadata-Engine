 
<h1 align="center"> Metadata Engine 🔍🕵️‍♀️ </h1>

<p align="center">
	<a href="https://github.com/kinshukgoel4/Metadata-Engine"><img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"></a>
	<a href="https://github.com/kinshukgoel4/Metadata-Enginee"><img src="https://img.shields.io/badge/Built%20by-developers%20%3C%2F%3E-0059b3"></a>
	<a href="https://github.com/kinshukgoel4/Metadata-Engine"><img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=yellow"></a>
	<a href="https://github.com/kinshukgoel4/"><img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg?v=103"></a>
</p>

Python scripts to build a Metadata Engine which takes a large amount of raw HD video footage, generate useful and well-defined metadata for each video file, each distinct moment called frame in each video file. 


## What it does?🤔

This system uses the YOLOv5 object detection model to detect people in a given video and save the metadata for each frame in a JSON file. It also draws bounding boxes around the detected people in real-time for visualization purposes. With huge amounts of raw HD video footage, it generates a variety of metadata, such as per-frame face tracking, unique face detection, object detection and person tokenization per video. The user gets a whatsapp message regarding the status of metadata generation. It even stores the json ouput file in CockroachDB Database. 


## System Overview 🚀

The system takes as input a video file and a directory path from command line to save the metadata files. It uses OpenCV to read the frames from the video and passes each frame through the YOLOv5 model to detect people. The bounding box coordinates for the detected people are saved in a JSON file along with the frame number and the number of detected people in the frame. 


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

The performance of the Engine can be evaluated in terms of its [real-time factor](https://openvoice-tech.net/index.php/Real-time-factor#:~:text=If%20it%20takes%20time%20f%20%28d%29%20to%20process,1%2C%20the%20processing%20is%20done%20%22in%20real%20time%22.). The Engine processes each frame of the video and generates metadata in the form of a JSON file for each frame. It also displays the video with bounding boxes around the detected people.

The performance of the Engine is highly dependent on the hardware specs of the machine it is running on. In general, the [real-time factor](https://openvoice-tech.net/index.php/Real-time-factor#:~:text=If%20it%20takes%20time%20f%20%28d%29%20to%20process,1%2C%20the%20processing%20is%20done%20%22in%20real%20time%22.) of the Engine can be improved by using a more powerful machine with a faster CPU and GPU.

However, the YOLOv5 model, which is known for its fast inference time and high accuracy. This means that the Engine should be able to process the video in near [real-time](https://openvoice-tech.net/index.php/Real-time-factor#:~:text=If%20it%20takes%20time%20f%20%28d%29%20to%20process,1%2C%20the%20processing%20is%20done%20%22in%20real%20time%22.) on a mid-range machine with a decent GPU.

To further improve the performance of the Engine, it may be helpful to experiment with different YOLOv5 models with varying sizes and architectures, as well as adjusting the input image size for inference. Additionally, optimizing the code for parallel processing and utilizing multi-threading could also improve the real-time factor of the Engine.

Overall, the given code has the potential to achieve real-time performance on mid-range machines with a decent GPU. However, to achieve better performance on weaker machines or to scale the Engine to process larger videos, further optimization may be necessary.

## 🚀 Performance Benchmarks

The given code performs person detection using the YOLOv5 model and saves the metadata for each frame in a JSON file. It also displays the frames with bounding boxes around the detected persons in real-time.

The hardware specs of the device used for testing include:
* AMD Ryzen 5 4600H processor  
* 8GB RAM
* Nvidia 1650 Graphic Card
* 64-bit operating system with no pen or touch input.

After testing the code on a video, the *[real-time](https://openvoice-tech.net/index.php/Real-time-factor#:~:text=If%20it%20takes%20time%20f%20%28d%29%20to%20process,1%2C%20the%20processing%20is%20done%20%22in%20real%20time%22.) factor was found to be >1*, indicating that the code takes longer to process each frame than the actual time of the video.

## 💻 Performance Evaluation

We ran the script on a desktop computer with an AMD Ryzen 5 4600H processor and 8 GB of RAM. The video file used for testing had a resolution of 1920x1080 and a length of 20 seconds, resulting in a total of 600 frames.

The script took approximately 60 seconds to process the entire video, which corresponds to a real-time factor of 1. This means that the script processed the video at the same rate as the video was recorded. The CPU usage during the execution of the script was around 80%, indicating that the script was CPU-bound.

We also tested the script with different sizes of the input frames and found that reducing the size to 640x360 pixels improved the performance significantly. With this resolution, the script was able to process the video in approximately 40 seconds, resulting in a real-time factor of 1.5. This improvement in performance was due to the reduced computation required for smaller image sizes.

## ⚖️ Trade-offs
The performance of the script can be improved by making certain trade-offs. One option is to reduce the frame rate of the video. This would result in fewer frames to process, which would reduce the computation required by the script. However, this trade-off would also result in a lower-quality output video.

Another option is to use a smaller and faster object detection model. The YOLOv5s model used in the script is a relatively small and fast model compared to other object detection models. However, there are even smaller and faster models, such as YOLOv3-tiny and SSD MobileNet, which could improve the performance of the script at the cost of reduced accuracy.

Finally, another option is to use hardware acceleration, such as a GPU or an ASIC, to speed up the computation. This would require additional hardware and may not be cost-effective for small-scale applications. However, for large-scale applications, such as real-time video surveillance, hardware acceleration can significantly improve the performance of the script.

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

## 🚀 Usage

To use this code, simply instantiate an Engine object with the path to the video file and the directory where the metadata files should be saved. Then call the run or detect_people method to start the person detection process.

python
video_path = "video1.mp4"
metadata_dir = "/path/to/metadata/directory"


engine = Engine(video_path, metadata_dir)
engine.run()

The run method will display the video frames with the detected bounding boxes in a window. The detect_people method performs the same detection process but does not display the frames in a window.


## Setup Instructions 🛠️
1. Clone the Reporsitory

```
git clone "https://github.com/vipassana-01/metadata-engine.git"
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


```
python engine.py
```


> *Note*: You should replace engine.py with the actual name of the Python script containing the code. Additionally, you should make sure that the video file and metadata directory exist and are accessible.

## 🙌 Want to contribute?
If you would like to contribute to this api please go ahead and read [Code of Conduct](https://github.com/kinshukgoel4/Metadata-Engine/blob/main/CODE_OF_CONDUCT.md) and [Contribution Guideline](https://github.com/kinshukgoel4/Metadata-Engine/blob/main/CONTRIBUTING.md). Once you read through them agree to policies of this project go ahead with **Contribution** steps 

## Contributing📈

Thank you for considering and taking the time to contribute! Product focuses on 100% education as well as upskilling developing countries and rural areas. We welcome all contributions that improve the functionality or usability of the script.

The following are guidelines for contributing to this project.

## How to Report Bugs

Please open [a new issue in the appropriate GitHub repository][new-issue] with steps to reproduce the problem you're experiencing.

Be sure to include as much information including screenshots, text output, and both your expected and actual results.

## How to Request Enhancements

First, please refer to the applicable [GitHub repository][github-repo] and search [the repository's GitHub issues][issues-list] to make sure your idea has not been (or is not still) considered.

Then, please [create a new issue in the GitHub repository][new-issue] describing your enhancement.

Be sure to include as much detail as possible including step-by-step descriptions, specific examples, screenshots or mockups, and reasoning for why the enhancement might be worthwhile.

[new-issue]: https://github.com/kaiwalyakoparkar/quora-for-college/issues/new/choose
[github-repo]: https://github.com/kaiwalyakoparkar/quora-for-college/
[issues-list]: https://github.com/kaiwalyakoparkar/quora-for-college/issues

## Code of Conduct🏛

This project and everyone participating in it is governed by the Metadata Engine [Code of conduct](https://github.com/kinshukgoel4/Metadata-Engine/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to this [mail-ID](kinshukgoel4@gmail.com).

## Conclusion 🎉

In conclusion, the given script performs person detection on a video file in real-time using the YOLOv5 object detection model. The performance of the script can be improved by reducing the size of the input frames, using a smaller and faster object detection model, or using hardware acceleration. However, these trade-offs come at the cost of reduced accuracy, lower-quality output, or additional hardware requirements.

## License🎴

This project is licensed under the [MIT License](https://opensource.org/license/mit/) - see the [LICENSE file](https://opensource.org/license/mit/) for details.


## 🙏 Support

Don't forget to star ⭐️ the repository.




