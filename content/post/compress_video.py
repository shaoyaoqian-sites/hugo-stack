from moviepy.editor import VideoFileClip
import os

def compress_with_moviepy(input_path, output_path, target_size_mb=5):
    """
    使用MoviePy压缩视频
    """
    try:
        # 加载视频
        clip = VideoFileClip(input_path)
        
        # 计算目标比特率 (粗略估算)
        duration = clip.duration  # 视频时长(秒)
        target_bitrate = (target_size_mb * 8192) / duration  # 单位: kbps
        
        # 写入压缩后的视频
        clip.write_videofile(
            output_path,
            codec='libx264',
            bitrate=f"{target_bitrate:.2f}k",
            audio_codec='aac',
            audio_bitrate='128k',
            preset='slow',
            threads=4,
            ffmpeg_params=['-movflags', '+faststart']
        )
        
        print(f"视频压缩成功，保存为: {output_path}")
        output_size = os.path.getsize(output_path) / (1024 * 1024)
        print(f"输出文件大小: {output_size:.2f}MB")
        
        return True
    except Exception as e:
        print(f"压缩失败: {e}")
        return False

# 使用示例
input_video = 'input.mp4'
output_video = 'compressed_moviepy.mp4'
compress_with_moviepy(input_video, output_video, target_size_mb=5)