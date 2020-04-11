# import opencv
import cv2

# Create a VideoCapture object
# Pass the number signifying the camera into the function.
# 0 is the first camera, or only camera.
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if cap.isOpened() == False:
    print("Error opening video stream or file")


# Default resolutions of the frame are obtained.
# The default resolutions are system dependent.
# We convert the resolutions from float to integer.
# obtain width (3) and height (4) properties of cap.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.
# The output is stored in 'outpy.avi' file.
# Define the fps to be equal to 30. Also frame size is passed.
# the writing speed is faster than the cap reading speed so we divide by 2
fps = 30//2
out = cv2.VideoWriter(
    "output.avi",
    cv2.VideoWriter_fourcc("M", "J", "P", "G"),
    fps,
    (frame_width, frame_height),
)

# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if a frame is read successfully
    if ret == True:
        # Write the frame into the file 'output.avi'
        out.write(frame)
        # Display the resulting frame
        cv2.imshow("Frame", frame)

        # Press Q on keyboard to exit
        frames_delay = 1  # this is essentially the duration of delay between each frame display
        if cv2.waitKey(frames_delay) & 0xFF == ord("q"):
            break

    # Break the loop
    else:
        break

# the following lines are needed to quit the program successfully
# 1. When everything done, release the video capture object
cap.release()
out.release()
# 2. Closes all the frames
cv2.destroyAllWindows()
