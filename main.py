import os
from pathlib import Path
import imageio.v3 as iio
from utils import extract_frames

in_path = Path('./data/raw/')
out_path = Path('./data/processed/')

if __name__ == '__main__':
    extract_frames(in_path,out_path)