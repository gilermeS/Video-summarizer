
import yt_dlp
import whisper
import config


def download_youtube_audio(url, output_path="audio.mp3"):

	ydl_opts = {
		'format': 'bestaudio/best',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'outtmpl': output_path.replace('.mp3', '.%(ext)s'),
		'quiet': True,
		'ffmpeg_location': config.ff_path,
	}

	with yt_dlp.YoutubeDL(ydl_opts) as ydl:

		info = ydl.extract_info(url, download=True)
		filename = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")


	return filename




model = whisper.load_model("base")

# result = model.transcribe("audio.mp3", fp16=False)


























