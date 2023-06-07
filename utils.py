import cv2
import librosa
import moviepy.editor as mp
import imageio.v3 as iio
import numpy as np

def resize(image,size):
    image = cv2.resize(image,size)
    return image


def extract_frames(in_path,out_path,size=None):
    '''
    Extracts frames from videos and stores them as images
    '''

    for path in in_path.iterdir():
        assert path.is_dir()

        video_id = 1
        total_files = len(list(path.glob('*')))
        frames_path = out_path/f'{path.name}'

        if not frames_path.exists():
            frames_path.mkdir()

        for video in path.iterdir():
            frame_id = 1
            for frame in iio.imiter(video,plugin='pyav'):
                frame_path = frame_path/f'/frame{video_id}_{frame_id}.jpg'
                try:
                    iio.imwrite(frame_path,frame)
                    frame_id+=1
                except Exception as exp:
                    print(f'Something went wrong writing {video} to the disk.\nException - {exp}')
            print(f'Finished Processing {video.parent.name/video.name}\nRemaining From Folder {total_files-video_id}\n')
            video_id+=1

def extract_melspec(in_path,out_path):
    '''
    Extracts melspec from input videos and saves them as images
    '''
    for path in in_path.iterdir():
        if not path.is_dir():
            continue
        
        assert path.is_dir()
        spec_id = 1
        spec_dirpath = out_path/f'{path.name}'
        if not spec_dirpath.exists():
            spec_dirpath.mkdir()

        for vid in path.iterdir():
            video = mp.VideoFileClip(str(vid))
            audio = video.audio.to_soundarray()

            audio_mono = audio.mean(axis=1)

            mel_spec = librosa.feature.melspectrogram(y=audio_mono,sr=None)

            mel_spec_db = librosa.power_to_db(mel_spec,ref=np.max)

            try:
                spec_path = spec_dirpath/f'mspec_{spec_id}.jpg'
                iio.imwrite(spec_path,mel_spec_db)
                print(f'Finished processing {spec_path}\n')
            except Exception as exp:
                print(f'Error saveing MelSpec for {path.parent.name/path.name}\nException occured - {exp}\n')
            
            spec_id+=1