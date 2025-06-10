from pydub import AudioSegment

def compress_audio(input_file, output_file, bitrate="64k"):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="mp3", bitrate=bitrate)

# 使用示例
musics = ["enzalla-lullaby"]

for music in musics:
    compress_audio(f"{music}.mp3", f"{music}-compressed.mp3", "32k")

