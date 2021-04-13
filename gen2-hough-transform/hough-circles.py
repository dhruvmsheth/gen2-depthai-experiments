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


            # Convert to gray-scale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Blur the image to reduce noise
            img_blur = cv2.medianBlur(gray, 5)
            # Apply hough transform on the image
            circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, img.shape[0]/64, param1=200, param2=10, minRadius=5, maxRadius=30)
            # Draw detected circles
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    # Draw outer circle
                    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    # Draw inner circle
                    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
                    cv2.imshow("Hough Transform", img)

        # Retrieve 'bgr' (opencv format) frame
        #cv2.imshow("bgr", inRgb.getCvFrame())

        if cv2.waitKey(1) == ord('q'):
            break
