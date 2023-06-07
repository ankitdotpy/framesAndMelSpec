import os
import multiprocessing
from pathlib import Path
import imageio.v3 as iio
from utils import extract_frames,extract_melspec

frames_in = Path('./data/frames/raw/')
frames_out = Path('/media/ankitd/Windows-SSD/Users/Ankit/Desktop/FrameDataset/processed')

audio_in = Path('./data/audio/raw/')
audio_out = Path('/media/ankitd/Windows-SSD/Users/Ankit/Desktop/FrameDataset/processed')

if __name__ == '__main__':
    pass