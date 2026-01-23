import os
import sys
import concurrent.futures
import logging
from moviepy import VideoFileClip

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 指定波特率、预设。
def compress_video(input_path, output_path, bitrate="500k", preset="fast"):
    """
    压缩视频文件，并尝试保持质量。
    """
    try:
        if not os.path.exists(input_path):
            logging.error(f"输入文件不存在: {input_path}")
            return

        clip = VideoFileClip(input_path)
        clip.write_videofile(output_path, bitrate=bitrate, codec='libx264', preset=preset)
        logging.info(f"压缩完成: {output_path}")
    except Exception as e:
        logging.error(f"压缩失败: {input_path} - {str(e)}")


def main(desktop_path, bitrate="5000k", preset="fast"):
    if not os.path.exists(desktop_path):
        logging.error(f"路径 {desktop_path} 不存在，请检查是否正确设置了路径。")
        return

    video_files = [os.path.join(desktop_path, filename) for filename in os.listdir(desktop_path) if
                   filename.endswith(('.mp4', '.avi', '.mkv', '.mov'))]

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for input_path in video_files:
            base, ext = os.path.splitext(os.path.basename(input_path))
            output_path = os.path.join("videos", f"{base}{ext}")
            future = executor.submit(compress_video, input_path, output_path, bitrate, preset)
            futures.append(future)

            # 等待所有任务完成
        concurrent.futures.wait(futures)


if __name__ == "__main__":
    # 解析命令行参数
    bitrate = "5000k"  # 默认比特率为 500k
    preset = "fast"  # 默认预设为 fast
    desktop_path = "./videos-raw/"
    main(desktop_path=desktop_path, bitrate=bitrate, preset=preset)
