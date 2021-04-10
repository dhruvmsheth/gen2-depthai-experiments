import cv2
import numpy as np
import depthai as dai

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
    global img
    while True:
        inRgb = qRgb.get()  # blocking call, will wait until a new data has arrived

        # Retrieve 'bgr' (opencv format) frame
        img = inRgb.getCvFrame()
        #cv2.imshow("bgr", inRgb.getCvFrame())

        if img is not None:
        

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            gray = np.float32(gray)
            dst = cv2.cornerHarris(gray,2,3,0.04)

            #result is dilated for marking the corners, not important
            dst = cv2.dilate(dst,None)

            # Threshold for an optimal value, it may vary depending on the image.
            img[dst>0.01*dst.max()]=[0,0,255]

            cv2.imshow('dst',img)
            
        if cv2.waitKey(1) == ord('q'):
            break


