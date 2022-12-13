from packages.Insta_Media_Downloader import Insta_Media_Downloader
from os import environ

def main() -> None:
    downloader = Insta_Media_Downloader( 
        environ.get('INSTAGRAM_USERNAME'), 
        environ.get('INSTAGRAM_PASSWORD')    
    )
    downloader.download_all_media(environ.get("TARGET_ACCOUNT"))
    
if __name__ == "__main__":

    try:
        main()

    except Exception as e:
        print(f"Failed {e}")
