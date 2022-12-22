import pytube
import os

# url input
yt = pytube.YouTube(input("Enter URL: \n>>"))

# only audio
audio = yt.streams.filter(only_audio=True).first()

# path where to save
downloads_path = "downloads"

# dwonloading
file = audio.download(output_path=downloads_path)

# saving file
base, ext = os.path.splitext(file)
new_file = base + ".mp3"
os.rename(file, new_file)

# success display
print(yt.title + " has been successfully downloaded.")
