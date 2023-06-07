import os
import multiprocessing
from pathlib import Path
import imageio.v3 as iio
from utils import extract_frames,extract_melspec

def get_video_frames(in_path,out_path,skip=None):
    for path in in_path.iterdir():
        if path.is_dir():
            video_id = 1
            out_dir = out_path/f'{in_path.name}/{path.name}'
            if not out_dir.exists():
                out_dir.mkdir()

            for video in path.iterdir():
                name = f'frame{video_id}'
                extract_frames(video,out_dir,skip,name)
                video_id+=1

def get_mel_spec(in_path,out_path):
    id = 1
    for path in in_path.iterdir():
        if path.is_dir():
            video_id = 1
            out_dir = out_path/f'{in_path.name}/{path.name}'
            if not out_dir.exists():
                out_dir.mkdir()

            for video in path.iterdir():
                name = f'melspec_{video_id}'
                extract_melspec(video,out_dir,name)
                video_id+=1
            

if __name__ == '__main__':
    frames_in = Path('./data/frames/raw/').resolve()
    frames_out = Path('/media/ankitd/Windows-SSD/Users/Ankit/Desktop/ProcessedData/frames_processed')

    audio_in = Path('./data/audio/raw/').resolve()
    audio_out = Path('/media/ankitd/Windows-SSD/Users/Ankit/Desktop/ProcessedData/spec_processed')

    skip = 1

    p1 = multiprocessing.Process(target=get_video_frames,args=(frames_in,frames_out,skip))
    p2 = multiprocessing.Process(target=get_video_frames,args=(audio_in,audio_out))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Completed processing...\nProgram exited...\n')