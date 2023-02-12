import io
import numpy as np
import torch
torch.set_num_threads(1)
import torchaudio
import matplotlib
import matplotlib.pylab as plt
torchaudio.set_audio_backend("soundfile")
import pyaudio

def __init__(self,
             PA_manager,
             rate,
             channels,
             format,
             input=False,
             output=False,
             input_device_index=None,
             output_device_index=None,
             frames_per_buffer=1024,
             start=True,
             input_host_api_specific_stream_info=None,
             output_host_api_specific_stream_info=None,
             stream_callback=None):
    import pyaudio
import numpy as np
import wave
#vad.py
def Monitor_MIC(th, filename):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    WAVE_OUTPUT_FILENAME = filename + ".wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("* recording")
    frames = []

    while (True):
        #print("ready for recording" + str(time.localtime(time.time()).tm_sec))
        for i in range(0, 5):
            data = stream.read(CHUNK)
            frames.append(data)
        audio_data = np.fromstring(data, dtype=np.short)
        temp = np.max(audio_data)
        print(temp)
        if temp > th :
            print("detected a signal")
            print('current threshold：',temp)
            less = []
            frames2 = []
            while (True):
                print("recording")
                for i in range(0, 30):
                    data2 = stream.read(CHUNK)
                    frames2.append(data2)
                audio_data2 = np.fromstring(data2, dtype=np.short)
                temp2 = np.max(audio_data2)
                print(temp2)
                if temp2 < th:
                    less.append(-1)
                    print("below threshold, counting: ", less)
                    #如果有连续2个循环的点，都不是声音信号，就认为音频结束了
                    if len(less) == 2:
                        print("end")
                        break
                else:
                    less = []
            break
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames2))
    wf.close()
