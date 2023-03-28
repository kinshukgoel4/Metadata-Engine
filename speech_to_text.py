import speech_recognition as sr
import moviepy.editor as mp
import json

# Load the video file
clip = mp.VideoFileClip("video2.mov")

# Extract the audio from the video
audio = clip.audio.to_audiofile("audio.wav")

# Initialize the recognizer
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile("audio.wav") as source:
    # Listen to the audio data
    audio_data = r.record(source)
    # Use Google Speech Recognition to transcribe the audio data
    text = r.recognize_google(audio_data)

# Print the transcribed text
# print(text)

data = {"text": text}

# create a JSON file and write the data to it
with open("output1.json", "w") as outfile:
    json.dump(data, outfile)