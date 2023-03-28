import speech_recognition as sr
import moviepy.editor as mp

# Load the video file
clip = mp.VideoFileClip("video1.mp4")

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
print(text)
