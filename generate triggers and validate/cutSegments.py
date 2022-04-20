# copy ffmpeg to the Python env where python.exe is (see more on that: https://stackoverflow.com/questions/45131495/the-system-cannot-find-the-file-specified-with-ffmpeg )
# ffmpeg.org/download.html

# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from genericpath import exists
import os
from shutil import which
from moviepy.editor import *
# import scipy.fftpack
from scipy.fft import fft
# import soundfile as sf
import pylab
import matplotlib
# import sys
import pandas as pd

##
import librosa
# import matplotlib.pyplot as plt
import numpy as np

import ffmpeg


def addPath(path):
    import sys
    sys.path.append(path)


def ltb_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


# get the current directory
dirpath = os.getcwd()

# data dirs
data_dir_vid = dirpath + '\\data\\videos'
data_dir_aud = data_dir_vid + '\\audio_only'

ltb_dir(data_dir_vid)
ltb_dir(data_dir_aud)

# extract file names
video_names = list(filter(lambda x: x.endswith(
    '.mp4'), os.listdir(data_dir_vid)))

audio_names = list(filter(lambda x: x.endswith(
    '.wav'), os.listdir(data_dir_aud)))


def skipper_bob(name_list, name2search):
    skip_write = False
    for n in name_list:
        if name2search in n:
            skip_write = True
            print(name2search + ' - BTDT')
    return skip_write


# loop over video files and extract audio if need be
for ni, name in enumerate(video_names):
    skip_write = skipper_bob(audio_names, name[0:-3])

    if not skip_write:
        video = VideoFileClip(os.path.join(data_dir_vid, video_names[ni]))
        audio = video.audio

        audio_name = os.path.join(data_dir_aud, video_names[ni][0:-4])+".wav"
        audio.write_audiofile(audio_name)  # fps = audio.fps data_dir_aud,

if 'video' in locals():
    video.close()

txt_names = list(filter(lambda x: x.endswith(
    '.txt'), os.listdir(data_dir_aud)))


def dsearchnn(x, v):
    return np.where(np.abs(x-v) == np.abs(x-v).min())[0]


audio_names = list(filter(lambda x: x.endswith(
    '.wav'), os.listdir(data_dir_aud)))

for dat_name in audio_names:
    skip_write = skipper_bob(txt_names, dat_name[0:4])
    if not skip_write:
        # load sounds and find event info
        y, sr = librosa.load(os.path.join(data_dir_aud, dat_name), mono=True)
        participant = dat_name[0:5]
        t = np.linspace(0, (y.size/sr)*1000, y.size)  # 1/sr

        # Initialize video data file

        filename = participant + 'videoData' + '.txt'

        # Prepare marker data file
        with open(os.path.join(data_dir_aud, filename), 'a') as file_object:
            file_object.write('participant' + ';' + 'event_id' +
                              ';' + 'full_name' + ';' + 'out_name' + ';' + 'trigger' + ';' + 'time' + '\n')

        event = abs(y) > 0.1
        event_idx = list()
        for num, e in enumerate(event):
            if e:
                event[num+1:num+sr] = False
                event_idx.append(num)
        # plot raw data with triggers
        # change this to control the plotting 'back end'
        # matplotlib.use('Qt5Agg')
        # pylab.figure(1, figsize=(10, 8))

        # pylab.plot(t, y, alpha=0.5)
        # pylab.xlabel("Time")
        # pylab.ylabel(" ... ")
        # pylab.stem(t[event_idx], np.zeros(len(event_idx))+0.3, 'y')

        # trigger frex
        trig_frex = [110, 333, 554, 784, 1046]

        # define the duration of the trigger marker, 1 s by default for convenience - the trigger dur itself is much shorter (0.1 s)
        dur = int(sr)
        hz = np.linspace(0, int(sr-1), dur)
        id_count = 1
        for inum, ind in enumerate(event_idx):  # iterating through the events
            dat = y[ind:ind+dur]
            fftCoefs = np.abs(fft(dat, len(dat)))
            # plot fourier
            # pylab.figure(2, figsize=(10, 8))
            # pylab.stem(hz[2:int(len(hz)/2)], fftCoefs[2:int(len(hz)/2)])

            # find triggers
            raw_trig = fftCoefs[2:int(len(hz)/2)] > 40
            raw_trig = np.where(raw_trig)[0]

            marker_idx = [0]*len(raw_trig)
            for numi, f_ind in enumerate(raw_trig):
                idx = dsearchnn(trig_frex, hz[f_ind])
                if trig_frex[int(idx)] - hz[f_ind] < 20:
                    marker_idx[numi] = int(idx)

            marker_idx = list(np.unique(marker_idx))
            trigger = np.zeros(5)
            trigger[marker_idx] = 1
            trigger = 't-'+''.join([str(int(i)) for i in trigger])

            full_name = participant
            out_name = participant

            full_name = full_name + 'position_'
            if 0 in marker_idx:
                full_name = full_name + 'start-'
            else:
                full_name = full_name + 'end-'

            full_name = full_name + 'eType_'
            if 1 in marker_idx:
                full_name = full_name + 'fb-'
            else:
                full_name = full_name + 'brush-'

            full_name = full_name + 'difficulty_'
            out_name = out_name + 'difficulty_'
            if 2 in marker_idx:
                full_name = full_name + '1-'  # difficult
                out_name = out_name + '1-'  # difficult
            else:
                full_name = full_name + '0-'  # easy
                out_name = out_name + '0-'  # easy

            full_name = full_name + 'outlier_'
            out_name = out_name + 'outlier_'
            if 3 in marker_idx and 4 in marker_idx:
                full_name = full_name + '1'  # greater
                out_name = out_name + '1'  # greater
            elif 3 in marker_idx:
                full_name = full_name + '-1'  # less
                out_name = out_name + '-1'  # less
            elif 4 in marker_idx:
                full_name = full_name + '0'  # same
                out_name = out_name + '0'  # same
            print(full_name)

            with open(os.path.join(data_dir_aud, filename), 'a') as file_object:
                file_object.write(participant[0:-1] + ';' +
                                  str(id_count) + ';' + full_name + ';' + out_name + ';' + trigger + ';' + str(t[ind]) + '\n')

            if 'end' in full_name and 'fb' in full_name:
                id_count += 1

# segment videos

data_dir_segm = data_dir_vid + '\\segments_out'
ltb_dir(data_dir_segm)

txt_names = list(filter(lambda x: x.endswith(
    '.txt'), os.listdir(data_dir_aud)))

for txt in txt_names:
    times_and_names = pd.read_csv(os.path.join(
        data_dir_aud, txt), sep=';')

    segm_names = list(filter(lambda x: x.endswith(
        '.mp4'), os.listdir(data_dir_segm)))

    v_index = [video_names.index(i) for i in video_names if txt[0:4] in i]

    if 'v_index' in locals() and len(v_index):
        name = video_names[v_index[0]]
        stream = ffmpeg.input(os.path.join(data_dir_vid, name))
        # loop over video files and extract segments if need be
        for ne, event in enumerate(times_and_names.full_name):
            out_name = times_and_names.out_name[ne]
            if 'fb' in event and 'start' in event:
                # skip_write_ki = skipper_bob(segm_names, name[0:4])
                skip_write = skipper_bob(segm_names, out_name)
                if not skip_write:
                    print(ne)
                    print(event)
                    print(
                        'start: ' + str(times_and_names.time[ne+1]-times_and_names.time[ne]/1000))
                    v_start = times_and_names.time[ne]/1000
                    e_id = times_and_names.event_id[ne]
                    out_name = os.path.join(
                        data_dir_segm, out_name+'-id_' + str(e_id) + ".mp4")
                    # ffmpeg_extract_subclip(os.path.join(
                    #     data_dir_vid, name), v_start, v_start+8.5, targetname=out_name)  # event+
                    # crop("00:07:09","00:09:12",os.path.join(data_dir_vid, name),out_name)

                    clip = stream.trim(start=v_start+0.5, duration=8).filter(
                        'setpts', 'PTS-STARTPTS')
                    # aud = stream.trim(start = v_start+0.5, end = 8).filter('asetpts', 'PTS-STARTPTS')
                    # joined = ffmpeg.concat(vid, aud, v=1, a=1).node
                    # output = ffmpeg.output(joined[0], joined[1], 'out.mp4')
                    # output.run()

                    out = ffmpeg.output(clip, out_name)
                    ffmpeg.run(out)


# pylab.show()


# audio.close()
# video.close()

# # FFT

# fCoefsF = scipy.fftpack.fft(audio)
