import youtube_dl



def download(url):
    downloads_path = 'downloads'
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'nocheckcertificate': True,
        'prefer_ffmpeg': True,
        'forcefilename': True,
        'outtmpl': downloads_path+'/%(title)s.%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)


if __name__ == "__main__":
    video_url = ['https://www.youtube.com/watch?v=y8OtzJtp-EM']
    download(video_url)
