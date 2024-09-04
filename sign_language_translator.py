import cv2 as cv

def DisplayWindow():
    video = cv.VideoCapture(1)
    video.set(3,200)
    video.set(4,200)

    while(True):
        rect,frame = video.read()
        cv.imshow("frame", frame)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv.destroyAllWindows()
    
DisplayWindow()



