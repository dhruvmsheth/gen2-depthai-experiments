
This example demonstrates how to run Background subtraction (BS) using Gen2 Pipeline Builder.
- Background subtraction (BS) is a common and widely used technique for generating a foreground mask (namely, a binary image containing the pixels belonging to moving objects in the scene) by using static cameras.
- As the name suggests, BS calculates the foreground mask performing a subtraction between the current frame and a background model, containing the static part of the scene or, more in general, everything that can be considered as background given the characteristics of the observed scene.


## Demo

### Camera
![Image](https://user-images.githubusercontent.com/67831664/114411404-c58cc180-9bc9-11eb-8a84-c469c4dca0b6.png)


## Pre-requisites

1. Purchase a DepthAI model (see [shop.luxonis.com](https://shop.luxonis.com/))
2. Install requirements
   ```
   python3 -m pip install -r requirements.txt
   ```

## Usage

```
usage: main.py [--algo] [KNN/MOG2)

optional arguments:
  --algo            Define the Background subtraction algorithm to be used

```


To use DepthAI 4K RGB camera with KNN algorithm run - 

```
python3 main.py --algo KNN
``` 


To use DepthAI 4K RGB camera with MOG2 algorithm run - 

```
python3 main.py --algo MOG2
``` 
