import cv2
import numpy as np
import depthai as dai

MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15

pipeline = dai.Pipeline()


# Define a source - color camera
camRgb = pipeline.createColorCamera()
camRgb.setPreviewSize(220, 349)
camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)

# Create output
xoutRgb = pipeline.createXLinkOut()
xoutRgb.setStreamName("rgb")
camRgb.preview.link(xoutRgb.input)



if __name__ == '__main__':

  # Read reference image
  refFilename = "wmmc3.jpg"
  imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)

with dai.Device(pipeline) as device:
    # Start pipeline
    device.startPipeline()

    # Output queue will be used to get the rgb frames from the output defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)

    while True:
        inRgb = qRgb.get()  # blocking call, will wait until a new data has arrived
        im = inRgb.getCvFrame()

        if im is not None:
            im1Gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            im2Gray = cv2.cvtColor(imReference, cv2.COLOR_BGR2GRAY)
            # Detect ORB features and compute descriptors.
            orb = cv2.ORB_create(MAX_FEATURES)
            keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
            keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)
            # Match features.
            matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
            matches = matcher.match(descriptors1, descriptors2, None)
            # Sort matches by score
            matches.sort(key=lambda x: x.distance, reverse=False)
            # Remove not so good matches
            numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
            matches = matches[:numGoodMatches]
            # Draw top matches
            imMatches = cv2.drawMatches(im, keypoints1, imReference, keypoints2, matches, None)
            cv2.imshow("matches", imMatches)
            

        if cv2.waitKey(1) == ord('q'):
            break
