
This example demonstrates how to run Feature extraction and Mapping, termed ORB (Oriented FAST and Rotated BRIEF) using Gen2 Pipeline Builder. ORB is basically a fusion of FAST keypoint detector and BRIEF descriptor with many modifications to enhance the performance. First it use FAST to find keypoints, then apply Harris corner measure to find top N points among them. It also use pyramid to produce multiscale-features. 

## Demo

### Camera
![ORB](https://user-images.githubusercontent.com/67831664/114745585-6c10c800-9d6c-11eb-8548-48b96c428fbc.png)



## Pre-requisites

1. Purchase a DepthAI model (see [shop.luxonis.com](https://shop.luxonis.com/))
2. Install requirements
   ```
   python3 -m pip install -r requirements.txt
   ```

## Usage


To use DepthAI 4K RGB camera run - 

```
python3 main.py
``` 
