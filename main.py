from package.Insta_Media_Downloader import Insta_Media_Downloader

def main() -> None:
    downloader = Insta_Media_Downloader("tony_bot_224", "Tejomay@000")
    downloader.download_all_media("blue_dive_")
    
if __name__ == "__main__":

    try:
        main()

    except Exception as e:
        print(f"Failed {e}")
