import cv2
import os
import argparse

def main():
    """
    take command line arguments input for the absolute paths of both the location of video and directory to store frames

    arguments:
        none
    """
    parser = argparse.ArgumentParser(description='processing some video.') # necessary for implementing command-line
    parser.add_argument('input_video_path', type=str, help='path to video') # adds argument input_video_path to the parser
    parser.add_argument('output_dir', type=str, help='directory to store frames') # adds argument output_dir to the parser

    args = parser.parse_args() # allows us to use the arguments in the parser (args.argument_name)

    video_to_frames(args.input_video_path, args.output_dir) 
    
def video_to_frames(input_video_path, output_dir):
    """
    extract frames from a video file and save them as separate images in some directory (file)

    arguments:
        input_video_path (str): path to video file
        output_dir (str): directory to save frames (path to folder)
    """

    os.makedirs(output_dir, exist_ok=True) # create the directory IF it doesnt exist
    video = cv2.VideoCapture(input_video_path)
    filename = os.path.basename(input_video_path)
    filename = filename.replace(".mp4","",4)

    if not video.isOpened():
        print(f"Error opening video file {input_video_path}")
        return

    count_total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range (count_total_frames): # loop for every frame
        counter = i + 1
        check, frame = video.read()
    
        if not check: # if check is false, then frame was not read
            print(f"Frame {counter} failed to save")
            continue

        frame_name = os.path.join(output_dir, f"{filename}_frame_{counter}.png")
        cv2.imwrite(frame_name, frame) # save current frame in specified directory with name and format
        print(f"Saved frame {counter} to {frame_name}")

    video.release() # fclose basically for video

    print(f"Extracted {count_total_frames} frames from {input_video_path}")

if __name__ == '__main__':
    main()