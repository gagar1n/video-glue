import glob
import os
import subprocess

def get_files_dict(directory):
    os.chdir(directory)
    list_mp4_files = glob.glob("*.MP4")
    dict_mp4_files = {}

    for mp4_file in list_mp4_files:
        mp4_file_prefix = mp4_file[0:4]
        mp4_file_number = int(mp4_file[4:-4])
        mp4_file_suffix = mp4_file[-4:]
        if mp4_file_prefix == 'GOPR':
            dict_index = 0
        elif mp4_file_prefix[0:2] == 'GP':
            dict_index = int(mp4_file_prefix[-2:])
        else:
            print("Wrong dict_index")
            exit -1
        file_dict = dict_mp4_files.setdefault(mp4_file_number, {})
        file_dict[dict_index] = mp4_file
    
    return dict_mp4_files


def create_ffmpeg_input_file(dict_mp4_files, directory):
    input_filename = directory + 'ffmpeg_input'
    ffmpeg_input_file = open(input_filename, 'w')

    for files_item in dict_mp4_files.items():
        for file_name in files_item[1].values():
            ffmpeg_input_file.writelines('file \'' + directory + file_name + '\'\n')
    
    ffmpeg_input_file.close()
    return input_filename


def run_ffmpeg_concat(input_filename):
    result = subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', '/data/ffmpeg_input', '-c', 'copy', 'GOPR9999.MP4'], stdout=subprocess.PIPE)
    print(result.stdout)

data_directory = "/data/"
dict_mp4_files = get_files_dict(data_directory)
input_filename = create_ffmpeg_input_file(dict_mp4_files, data_directory)
run_ffmpeg_concat(input_filename)
