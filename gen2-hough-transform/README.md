
This example demonstrates how to run Background subtraction (BS) using Gen2 Pipeline Builder.
- Background subtraction (BS) is a common and widely used technique for generating a foreground mask (namely, a binary image containing the pixels belonging to moving objects in the scene) by using static cameras.
- As the name suggests, BS calculates the foreground mask performing a subtraction between the current frame and a background model, containing the static part of the scene or, more in general, everything that can be considered as background given the characteristics of the observed scene.


## Demo

### Camera
![2021-04-13-195501_848x480_scrot](https://user-images.githubusercontent.com/67831664/114571781-8b3c2680-9c94-11eb-90d4-23ff9d1b2f30.png)


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
