"""
sudo apt install python3-pip -y #to install python3 pip
pip install pytube #to install pytube module

st = yt.streams #to get all streams list of video.
video_files = st.filter(progressive=True) #to fetch all audio and video files list.
video_file = st.filter(progressive=True).first() #to fetch first audio and video file.
audio_file = st.filter(type="audio").first() #to fetch first audio file.
title = yt.title #to fetch title of video
thumbnail = yt.thumbnail_url #to fetch thumbnail of video.
desc = yt.description[:200] #to fetch video description sliced in 200 words only.
video_file.download("./") #to download video file.
audio_file.download("./") #to download audio file.

progressive="True" = audio/video
progressive="False" = video
"""
from pytube import* #pip install pytube

url = "https://www.youtube.com/watch?v=T5o_0BoTvWg"
yt = YouTube(url)
st = yt.streams #to get all streams list of video.
# video_file = st.filter(progressive=True).first() #to fetch first audio and video file.
audio_file = st.filter(only_audio=True).first() #to fetch first audio file.

audio_file.download("./")