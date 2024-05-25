import cv2
import os
import argparse

def video_to_frames(input_video_path, output_dir):
    """
    extract frames from a video file and save them as separate images in some directory (file)

    arguments:
        input_video_path (str): path to video file
        output_dir (str): directory to save frames (path to folder)
    """

    os.makedirs(output_dir, exist_ok=True) # create the directory IF it doesnt exist
    video = cv2.VideoCapture(input_video_path)

    if not video.isOpened():
        print(f"Error opening video file {input_video_path}")
        return

    count_total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range (count_total_frames): # loop for every frame
        check, frame = video.read()
    
        if not check: # if check is false, then frame was not read
            print(f"Frame {i} failed to save")
            continue

        frame_name = os.path.join(output_dir, f"frame_{i:04d}.jpg") # only 4 digits? usability
        cv2.imwrite(frame_name, frame) # save current frame in specified directory with name and format
        print(f"Saved frame {i} to {frame_name}")

    video.release() # fclose basically for video

    print(f"Extracted {count_total_frames} frames from {input_video_path}")

def main():
    """
    take command line arguments input for the absolute paths of both the location of video and directory to store frames

    arguments:
        none
    """
    parser = argparse.ArgumentParser(description='processing some video.')
    parser.add_argument('input_video_path', type=str, help='absolute path to video')
    parser.add_argument('output_dir', type=str, help='directory to store frames')

    args = parser.parse_args()

    video_to_frames(args.input_video_path, args.output_dir)

if __name__ == '__main__':
    main()