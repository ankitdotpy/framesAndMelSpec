import cv2
import subprocess
import imageio.v3 as iio

def extract_frames(in_path,out_path,size=None):
    '''
    TODO
    Resolve output path
    Extract frames from in_path(video path)
    store extarcted frames in reolved output path
    '''

    for path in in_path.iterdir():
        video_id = 1
        total_files = len(list(path.glob('*')))
        for video in path.iterdir():
            frame_id = 1
            for frame in iio.imiter(video,plugin='pyav'):
                frame_path = out_path/f'{path.name}/frame{video_id}_{frame_id}.jpg'
                try:
                    iio.imwrite(frame_path,frame)
                    frame_id+=1
                except:
                    print(f'Something went wrong writing {video} to the disk.')
            print(f'Finished Processing {video.parent/video.name}\nRemaining From Folder {total_files-video_id}\n')
            video_id+=1
    pass

def resize(image,size):
    image = cv2.resize(image,size)
    return image

def extract_audio(in_path,out_path):
    command = ['ffmpeg', '-i', in_path, '-vn', '-acodec', 'copy', out_path]
    subprocess.call(command)