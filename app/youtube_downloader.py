from natsort import natsorted

from youtube_dl import YoutubeDL


url = "https://www.youtube.com/watch?v=dKjKnWMpLFU"

video = YoutubeDL().e

# TODO:
# lekezelni
video.check_availability()

video_streams = video.streams
print(video.title)

video.streams.get_highest_resolution().download()



# TODO:
# kiszedni külön az mp3 és mp4 streameket
# kiválasztani, mit szeretne
# onnan menni tovább resolutionra

