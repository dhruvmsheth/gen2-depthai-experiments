#!/usr/bin/env python3

import cv2
import depthai as dai
import numpy as np

# Start defining a pipeline
pipeline = dai.Pipeline()

# Define a source - color camera
camRgb = pipeline.createColorCamera()
camRgb.setPreviewSize(300, 300)
camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)

# Create output
xoutRgb = pipeline.createXLinkOut()
xoutRgb.setStreamName("rgb")
camRgb.preview.link(xoutRgb.input)

# Pipeline defined, now the device is connected to
with dai.Device(pipeline) as device:
    # Start pipeline
    device.startPipeline()

    # Output queue will be used to get the rgb frames from the output defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)

    while True:
        inRgb = qRgb.get()  # blocking call, will wait until a new data has arrived

        img = inRgb.getCvFrame()

        if img is not None:
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
              
            # Apply edge detection method on the image
            edges = cv2.Canny(gray,50,150,apertureSize=3)
              
            # This returns an array of r and theta values
            lines = cv2.HoughLines(edges,1,np.pi/180, 200)

            if lines is not None:
                  
                # The below for loop runs till r and theta values 
                # are in the range of the 2d array
                for r,theta in lines[0]:
                      
                    # Stores the value of cos(theta) in a
                    a = np.cos(theta)
                  
                    # Stores the value of sin(theta) in b
                    b = np.sin(theta)
                      
                    # x0 stores the value rcos(theta)
                    x0 = a*r
                      
                    # y0 stores the value rsin(theta)
                    y0 = b*r
                      
                    # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
                    x1 = int(x0 + 1000*(-b))
                      
                    # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
                    y1 = int(y0 + 1000*(a))
                  
                    # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
                    x2 = int(x0 - 1000*(-b))
                      
                    # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
                    y2 = int(y0 - 1000*(a))
                      
                    # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
                    # (0,0,255) denotes the colour of the line to be 
                    #drawn. In this case, it is red. 
                    cv2.line(img,(x1,y1), (x2,y2), (238, 238, 15),2)
            cv2.imshow("Hough", img)
                      

        if cv2.waitKey(1) == ord('q'):
            break
