"""Module for parsing data directory and concatenation GoPro videofiles"""
__author__ = 'Mykhailo Voitashevskyi'

import glob
import os
import sys
import subprocess
import collections


def get_files_dict(directory):
    """Function will parse directory and create an ordered dictionary
    with all GoPro video files"""
    os.chdir(directory)
    list_mp4_files = glob.glob("*.MP4")
    dict_mp4_files = {}

    for mp4_file in list_mp4_files:
        mp4_file_prefix = mp4_file[0:4]
        mp4_file_number = int(mp4_file[4:-4])
        if mp4_file_prefix == 'GOPR':
            dict_index = 0
        elif mp4_file_prefix[0:2] == 'GP':
            dict_index = int(mp4_file_prefix[-2:])
        else:
            print("Wrong dict_index")
            sys.exit(-1)
        file_dict = dict_mp4_files.setdefault(mp4_file_number, {})
        file_dict[dict_index] = mp4_file
    dict_mp4_files = collections.OrderedDict(sorted(dict_mp4_files.items()))
    return dict_mp4_files



def create_ffmpeg_input_file(dict_mp4_files, directory):
    """Function will create input file for ffmpeg from ordered dictionary"""
    input_filename = os.path.join(directory, 'ffmpeg_input')
    with open(input_filename, 'w') as ffmpeg_input_file:
        for files_item in dict_mp4_files.items():
            for file_name in files_item[1].values():
                ffmpeg_input_file.writelines("file '" + os.path.join(directory, file_name) + "'\n")
    return input_filename


def run_ffmpeg_concat(input_filename):
    """run ffmpeg for concatenation MP4 files from input_filename file"""
    result = subprocess.run(
        ['ffmpeg',
         '-f',
         'concat',
         '-safe',
         '0',
         '-i',
         input_filename,
         '-c',
         'copy',
         'GOPR9999.MP4'],
        stdout=subprocess.PIPE)
    return result.returncode

data_directory = "/data/"
mp4_files = get_files_dict(data_directory)
ffmpeg_filename = create_ffmpeg_input_file(mp4_files, data_directory)
run_ffmpeg_concat(ffmpeg_filename)
