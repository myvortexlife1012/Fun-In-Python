
# import VIDEO as video
# video.save200FramesFromVideo()
# video.saveAllFramesFromVideo()

#----------------------


# import VIDEO as video
# video.save200FramesFromVideo()

# 18sec video = 540 frames/images
def save200FramesFromVideo():
    import cv2  # pip install opencv-python
    import ImageSAVER as saver #does the img resize

    # Opens the Video file
    video_filename = "C:\\Users\\myvor\\PycharmProjects\\pythonProject\\z-Frames\\beach_with_rocks.mp4"
    cap = cv2.VideoCapture(video_filename)
    i = 0
    while (cap.isOpened()):
        print (f"In Loop - {i}")
        ret, frame = cap.read()
        if ret == False:
            break
        imageFilePath = 'z-Frames/beach_with_rocks/frame-' + str(i) + '.jpg'
        #saves the big version - full frame size
        cv2.imwrite(imageFilePath, frame)

        #resize - and lower jpg quality
        # import ImageSAVER as saver
        saver.imageResize(imageFilePath, 1920, 70) # width = 1920, jpgQuality=70
        #
        i += 1
        #stop at 200
        if i==200:
            break

    cap.release()
    cv2.destroyAllWindows()



# 18sec video = 540 frames/images
def saveAllFramesFromVideo():
    import cv2  # pip install opencv-python

    # Opens the Video file
    cap = cv2.VideoCapture('C:/Users/myvor/Videos/!Video Backgrounds/!play.mp4')
    i = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite('frames/frame-' + str(i) + '.jpg', frame)
        i += 1

    cap.release()
    cv2.destroyAllWindows()


