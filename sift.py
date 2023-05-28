import numpy as np
import cv2
import pysift
from matplotlib import pyplot as plt
import logging
logger = logging.getLogger(__name__)

MIN_MATCH_COUNT = 4

template = cv2.imread('eyes.png', 0)  # template
print("type = ", (template.shape))
#template_gray = cv2.cvtColor(np.float32(template), cv2.COLOR_BGR2GRAY)

vid = cv2.VideoCapture(0)

while True:
    # Capture the video frame by frame
    ret, frame = vid.read()
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
    frame = cv2.cvtColor(np.float32(frame), cv2.COLOR_BGR2GRAY)
    
    # Compute SIFT keypoints and descriptors
    kp1, des1 = pysift.computeKeypointsAndDescriptors(template)
    kp2, des2 = pysift.computeKeypointsAndDescriptors(frame)
    print("created keypoints")

    # Initialize and use FLANN
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    print("Completed knn")

    # Lowe's ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    if len(good) > MIN_MATCH_COUNT:
        # Estimate homography between template and scene
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        M = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)[0]
        print("Found Homographs!")

        # Draw detected template in scene image
        h, w = template.shape
        pts = np.float32([[0, 0],
                        [0, h - 1],
                        [w - 1, h - 1],
                        [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M)

        #frame = cv2.cvtColor(np.float32(frame), cv2.COLOR_GRAY2RGB)
        frame = cv2.polylines(frame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
        print("Drew template on scene")


        # cv2.imshow('Frame With Template Found', frame)
        # # The 'q' button is set as the quitting button you may use any desired button of your choice
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        plt.imshow(frame)
        plt.show()
    else:
        print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))

vid.release()
# Destroy all the windows
cv2.destroyAllWindows()