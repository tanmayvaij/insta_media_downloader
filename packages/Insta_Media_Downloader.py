from instagrapi import Client
from dotenv import load_dotenv
from os import mkdir, path

# loading environment variables
load_dotenv("./config.env")

# Check if the downloads folder exists not, folder is created if does not exists
def createFolder(folder: str) -> None:
    if path.exists(folder):
        print("--> Download folder already exists")
    else:
        mkdir(folder)
        print("--> Created downloads folder")

class Insta_Media_Downloader:

    def __init__(self, username: str, password: str):

        # client instance created
        self.__client = Client()

        # trying to login into account
        print(f"--> Trying to login into your account @{username}")
        self.__client.login(username, password)
        print("--> Logged in successfully")

    # Method for downloading all the user medias
    def download_all_media(self, target: str) -> None:

        DOWNLOAD_PATH = "./downloads"
        
        # Getting user id from username
        print("--> Getting user id from username")
        user_id = self.__client.user_id_from_username(target)
        print(f"--> User id fetched - {user_id}")

        # Getting all the details of the user medias in form of list
        print("--> Getting all user media details")
        media_list = self.__client.user_medias(user_id)
        print("--> Got all media successfully")

        createFolder(DOWNLOAD_PATH)

        # Starting the download process 
        print("--> Starting the download process")
        for i in media_list:
            
            if i.media_type == 1:
                # Method for downloading photo
                self.__client.photo_download(int(i.pk), DOWNLOAD_PATH)
                print(f"--> Downloaded media with id - {i.pk}")

            elif i.media_type == 2 and  i.product_type == "feed":
                # Method for downloading video
                self.__client.video_download(int(i.pk), DOWNLOAD_PATH)
                print(f"--> Downloaded media with id - {i.pk}")

            elif i.media_type == 2 and i.product_type == "igtv":
                # Method for downloading igtv video
                self.__client.igtv_download(int(i.pk), DOWNLOAD_PATH)
                print(f"--> Downloaded media with id - {i.pk}")

            elif i.media_type == 2 and i.product_type == "clips":
                # Method for downloading reel
                self.__client.clip_download(int(i.pk), DOWNLOAD_PATH)
                print(f"--> Downloaded media with id - {i.pk}")

            else:
                # Method for downloading album (more than one media)
                self.__client.album_download(int(i.pk), DOWNLOAD_PATH)
                print(f"--> Downloaded media with id - {i.pk}")

        print("--> Finished")
