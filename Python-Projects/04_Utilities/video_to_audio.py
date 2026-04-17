from moviepy.editor import VideoFileClip

# Load video
cvt_video = VideoFileClip(r"a:\m\Prmovies-What_Every_Frenchwoman_Wants.mp4")

# Extract audio
ext_audio = cvt_video.audio

# Save audio
ext_audio.write_audiofile("audio_extracted.mp3")
