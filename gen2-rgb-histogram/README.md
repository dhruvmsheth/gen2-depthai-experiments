This example demonstrates how to extract and plot RGB channels from OAK-D in the form of a histogram using Gen2 Pipeline Builder. You can consider histogram as a graph or plot, which gives you an overall idea about the intensity distribution of an image. It is a plot with pixel values (ranging from 0 to 255, not always) in X-axis and corresponding number of pixels in the image on Y-axis.

It is just another way of understanding the image. By looking at the histogram of an image, you get intuition about contrast, brightness, intensity distribution etc of that image. Almost all image processing tools today, provides features on histogram.

## Demo

### Camera
![2021-05-08-215900_848x480_scrot](https://user-images.githubusercontent.com/67831664/117546623-f33e1c80-b048-11eb-94c1-598bfe17f817.png)


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
