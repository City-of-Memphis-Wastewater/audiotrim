"""
Author: Clayton Bennett
Title: audiotrim.py
Created: 2025 02-February 19
Purpose: Audio Trimming
"""
# audiotrim/__main__.py

# Prepare libraries
import argparse
import audiotrim.gui as gui
import audiotrim.audio_utils as audio_utils
import audiotrim.config_utils as config_utils

def script(path_in,path_out,time_start, time_end):
    
    # Load the audio file
    audio_data, sample_rate = audio_utils.load_audio(path_in)
    
    # Trim the audio
    trimmed_audio = audio_utils.trim_audio(audio_data, sample_rate, time_start, time_end)

    # Save the trimmed file
    audio_utils.save_audio(path_out, trimmed_audio, sample_rate)

    # Confirmation messaging
    print("Success.")

def main():
    defaults = config_utils.load_defaults('config.toml')
    
    parser = argparse.ArgumentParser(description="Trim an audio file.")
    parser.add_argument("-i", "--input_file", type=str, default=defaults['input_file'], help="Path to the input audio file")
    parser.add_argument("-o", "--output_file", type=str, default=defaults['output_file'], help="Path to the output audio file")
    parser.add_argument("-s", "--start_time", type=float, default=float(defaults['start_time']), help="Start time in seconds")
    parser.add_argument("-e", "--end_time", type=float, default=defaults['end_time'], help="End time in seconds")
    parser.add_argument("--gui", action="store_true", help="Launch the GUI")
    
    args = parser.parse_args()
    if args.gui:
        gui.create_gui(vars(args), script)
    else:
        script(args.input_file, args.output_file, args.start_time, args.end_time)

if __name__ == "__main__":
    main()

"""Powershell:
$dir_track = "C:\\Users\\george.bennett\\Downloads\\"
$path_in = $dir_track+"Act IV - 2025 remastered.wav"
$path_out = $dir_track+"Act IV - 2025 remastered2.wav"
$time_start = 94
$time_end = 54+2*60
python audiotrim.py $path_in $path_out -s $time_start -e $time_end
"""