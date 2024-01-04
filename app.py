from pytube import YouTube
import os

def YoutubeDownloader(url):
    try:
        output_path = '.\\Downloads'
        os.makedirs(output_path, exist_ok=True)
        yt = YouTube(url)
        vdstream = yt.streams.filter(only_audio=True, bitrate=f"128kbps").first()
        vdstream.download(output_path)
        old_file_name = os.path.join(output_path, vdstream.default_filename)
        new_file_name = os.path.join(output_path, f"{vdstream.default_filename}.mp3").replace('.mp4', '')
        os.rename(old_file_name, new_file_name)
        print(f"เสร็จสิ้นการดาวน์โหลดเพลง: {new_file_name}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการดาวน์โหลด {url}: {str(e)}")
def main():
    urls = input("ป้อน URL (แต่ละเพลงคั่นด้วยช่องว่าง): ").split()
    for url in urls:
        YoutubeDownloader(url)
if __name__ == "__main__":
    main()
