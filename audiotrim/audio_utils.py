# audiotrim/audio_utils.py
import audioread
import soundfile as sf
import numpy as np

def load_audio(path_in):
    # Function to load audio file
     
    with audioread.audio_open(path_in) as f:
        sample_rate = f.samplerate
        audio = np.concatenate([np.frombuffer(buf, dtype=np.int16) for buf in f])
    return audio,sample_rate

def save_audio(path_out, audio_data, sample_rate):
    # Function to save audio file
    sf.write(path_out, audio_data, sample_rate)
    return True

def trim_audio(audio_data, sample_rate, time_start, time_end):
    # Function to trim audio
    
    # Define start and end times in seconds
    print(f"Cut: {time_start} sec to {time_end} sec")
    #sampled values
    time_start = int(time_start * sample_rate)
    time_end = int(time_end * sample_rate)
    

    # Trim the audio
    trimmed_audio = audio_data[time_start:time_end]
    return trimmed_audio 

