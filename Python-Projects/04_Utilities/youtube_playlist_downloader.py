from pytube import Playlist, YouTube

playlist_url = "https://www.youtube.com/playlist?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0"
p = Playlist(playlist_url)

print(f"Found {len(p.video_urls)} videos")

for url in p.video_urls:
    try:
        yt = YouTube(url)
        print("Downloading:", yt.title)
        yt.streams.get_highest_resolution().download()
    except Exception as e:
        print("Error with", url, ":", e)
