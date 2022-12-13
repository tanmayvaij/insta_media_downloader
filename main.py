from packages.Insta_Media_Downloader import Insta_Media_Downloader
from packages.settings import INSTAGRAM_PASSWORD, INSTAGRAM_USERNAME, TARGET_ACCOUNT

def main() -> None:
    downloader = Insta_Media_Downloader(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    downloader.download_all_media(TARGET_ACCOUNT)
    
if __name__ == "__main__":

    try:
        main()

    except Exception as e:
        print(f"Failed {e}")
