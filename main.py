from packages.Insta_Media_Downloader import Insta_Media_Downloader
from packages.information import information

def main() -> None:

    # initialized information instance
    info = information()

    # initialized downloader instance
    downloader = Insta_Media_Downloader(
        info.INSTAGRAM_USERNAME, 
        info.INSTAGRAM_PASSWORD,
        info.NO_OF_POSTS
    )

    # executing download_add_media if the target account is specified
    if info.download_all_media_exists:
        downloader.download_all_media(info.TARGET_ACCOUNT)
    
    # executing download_by_url if the target url is specified
    if info.download_by_url_exists:
        downloader.download_by_url(info.MEDIA_URL)
    
if __name__ == "__main__":

    try:
        main()

    except Exception as e:
        print(f"--> Failed {e}")
        print("--> Exiting")
