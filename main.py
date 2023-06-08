import os
import multiprocessing
from pathlib import Path
import imageio.v3 as iio
from utils import extract_frames,extract_melspec

def get_video_frames(in_path,out_path,skip=None):
    for path in in_path.iterdir():
        if path.is_dir():
            video_id = 1
            total_files = len(list(path.glob('*')))
            out_dir = out_path/path.name
            if not out_dir.exists():
                out_dir.mkdir()

            for video in path.iterdir():
                name = f'frame{video_id}'
                extract_frames(video,out_dir,skip,name)
                print(f'FRM: Processed {video}\nRemaining - {total_files-video_id}/{total_files}\n')
                video_id+=1

def get_mel_spec(in_path,out_path):
    id = 1
    for path in in_path.iterdir():
        if path.is_dir():
            video_id = 1
            total_files = len(list(path.glob('*')))
            out_dir = out_path/path.name
            if not out_dir.exists():
                out_dir.mkdir()

            for file in path.iterdir():
                # name = f'melspec_{video_id}'
                extract_melspec(file,out_dir)
                print(f'MEL: Processed {file}\nRemaining - {total_files-video_id}/{total_files}\n')
                video_id+=1
            

if __name__ == '__main__':
    frames_in = Path('./data/frames/raw/').resolve()
    frames_out = Path('/media/ankitd/Windows-SSD/Users/Ankit/Desktop/ProcessedData/frames_data')

    audio_in = Path('./data/audio/raw/').resolve()
    audio_out = Path('/media/ankitd/Windows-SSD/Users/Ankit/Desktop/ProcessedData/spec_processed')

    skip = 1

    p1 = multiprocessing.Process(target=get_video_frames,args=(frames_in,frames_out,skip))
    p2 = multiprocessing.Process(target=get_mel_spec,args=(audio_in,audio_out))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Program exited...\n')

    get_mel_spec(audio_in,audio_out)