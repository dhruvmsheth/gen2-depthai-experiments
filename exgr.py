import cv2
import depthai as dai
import numpy as np


max_lowThreshold = 255
ratio = 3
kernel_size = 3
threshold = 50


# Start defining a pipeline
pipeline = dai.Pipeline()

# Define a source - color camera
cam_rgb = pipeline.createColorCamera()
cam_rgb.setPreviewSize(540, 300)
cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)
cam_rgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
cam_rgb.setInterleaved(False)
cam_rgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)


# Create output
xout_rgb = pipeline.createXLinkOut()
xout_rgb.setStreamName("rgb")
cam_rgb.preview.link(xout_rgb.input)





# Pipeline defined, now the device is connected to
with dai.Device(pipeline) as device:
    # Start pipeline
    device.startPipeline()

    # Output queue will be used to get the rgb frames from the output defined above
    q_rgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)

    while True:
        in_rgb = q_rgb.get()  # blocking call, will wait until a new data has arrived
        src = in_rgb.getCvFrame()

        if src is not None:

            img =  cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
            blue = img[:,:,2]
            green = img[:,:,1]
            red = img[:,:,0]
            exg = 2*green - red - blue
            img = np.where(exg < 0, 0, exg).astype('uint8')
            img = img.astype(np.uint8)

            exr = 1.4*red - green
            exr = np.where(exr < 0, 0, exr).astype('uint8')
            exr = exr.astype(np.uint8)
            exgr = exg - exr
            exgr = np.where(exgr < 25, 0, exgr).astype('uint8')
            exgr = exgr.astype(np.uint8)
            
            cv2.imshow('exr', exr)

            cv2.imshow('img', img)
            cv2.imshow('exgr', exgr)
            
        if cv2.waitKey(1) == ord('q'):
            break
