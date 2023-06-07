import cv2
import librosa
import moviepy.editor as mp
import imageio.v3 as iio
import numpy as np

def resize(image,size):
    image = cv2.resize(image,size)
    return image


def extract_frames(in_path,out_dir,skip=None,name=None):
    '''
    Extracts frames from videos and stores them as images
    '''

    '''
    args:
    in_path: path to video file
    out_path: path to save output
    skip: number of frames to skip after each save
    name: name of the save file
    '''

    frame_id = 1
    skip_cnt = skip or 0
    for frame in iio.imiter(in_path,plugin='pyav'):
        if skip_cnt == 0:
            path = out_dir/f'{name or "frame"}_{frame_id}.png'
            try:
                iio.imwrite(path,frame)
            except Exception as exp:
                print(f'FRM: Error processing {in_path}\nException occured - {exp}\n')
                return
            skip_cnt = skip or 0
        else:
            skip_cnt-=1
        
        
        

def extract_melspec(in_path,out_dir,name=None):
    '''
    Extracts melspec from input videos and saves them as images
    '''

    '''
    in_path: path to audio/video file
    out_path: path to save output melspectrogram
    name: name of the save file
    '''
    audio = None

    if str(in_path).endswith(('.mp3','.wav','.ogg','.flac','.m4a')):
        audio,_ = librosa.load(in_path,sr=None)
    else:
        video = mp.VideoFileClip(str(in_path))
        audio = video.audio.to_soundarray()
        audio = audio.mean(axis=1) # Mono Audio
    
    mel_spec = librosa.feature.melspectrogram(audio,sr=None)
    mel_spec_db = librosa.power_to_db(mel_spec,ref=np.max)

    path = out_dir/f'{name or f"melspec_{in_path.stem}"}.png'

    try:
        iio.imwrite(path,mel_spec_db)
    except Exception as exp:
        print(f'MEL: Error Processing {in_path}\nException occured - {exp}\n')
        return



