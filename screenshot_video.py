import cv2
import os

# --- Configuration ---
VIDEO_FILENAME = "momika_vi_video_1.mp4"  # <--- IMPORTANT: Change this to your video's exact filename
TIMESTAMP_MINUTES = 1
TIMESTAMP_SECONDS = 8
total_seconds = (TIMESTAMP_MINUTES * 60) + TIMESTAMP_SECONDS

#open video file
video_path = os.path.abspath(VIDEO_FILENAME)

if not os.path.exists(VIDEO_FILENAME):
    print(f"Error: The video file '{VIDEO_FILENAME}' was not found.")
else:
    # Create a video capture object
    video_capture = cv2.VideoCapture(VIDEO_FILENAME)

    # Check if the video opened successfully
    if not video_capture.isOpened():
        print(f"Error: Could not open video file '{VIDEO_FILENAME}'.")
    else:
        print(f"Successfully opened '{VIDEO_FILENAME}'!")

    
        fps = video_capture.get(cv2.CAP_PROP_FPS)
        print(f"Frames per second: {fps}")exit
        target_frame_number = int(total_seconds * fps) #verify total secons
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, target_frame_number) #set the frame position using playhead
        success, frame = video_capture.read()
        if success:
            screenshot_filename = f"screenshot_at_{TIMESTAMP_MINUTES}m{TIMESTAMP_SECONDS}s.png"
            cv2.imwrite(screenshot_filename, frame)
            print(f"Screenshot saved as '{screenshot_filename}'")
        else:
            print(f"Error: Could not read frame at {TIMESTAMP_MINUTES}m{TIMESTAMP_SECONDS}s.")

        # Release the video capture object
        video_capture.release()
        print("Video released.")

