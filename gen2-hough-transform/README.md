
This example demonstrates how to run Hough Transform Circles and Lines using Gen2 Pipeline Builder.


## Demo
### Hough Transform Lines - (Uses less computation)
> Here, there are many false negatives, so it detects only those lines which are continuous
![hough](https://user-images.githubusercontent.com/67831664/114593829-2ab7e400-9caa-11eb-8ba9-bf4256638a3b.jpg)

### Hough Transform Circles - (Uses more computation)
> Here, there are many false negatvives, so make sure image has only those circular objects required -
![Hough](https://user-images.githubusercontent.com/67831664/114595124-a9f9e780-9cab-11eb-8056-a536ad3699ed.jpg)



## Pre-requisites

1. Purchase a DepthAI model (see [shop.luxonis.com](https://shop.luxonis.com/))
2. Install requirements
   ```
   python3 -m pip install -r requirements.txt
   ```

## Usage


To use DepthAI 4K RGB camera run - 

```python
python3 hough-circles.py
```

Or 

```python
python3 hough-lines.py
```
