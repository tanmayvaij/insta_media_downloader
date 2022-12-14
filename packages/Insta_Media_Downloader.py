from instagrapi import Client
from os import mkdir, path

# Check if the downloads folder exists not, folder is created if does not exists
def createFolder(folder: str) -> None:
    if path.exists(folder):
        print("--> Download folder already exists")
    else:
        mkdir(folder)
        print("--> Created downloads folder")

class Insta_Media_Downloader:

    def __init__(self, username: str, password: str, posts_amount: str):

        # client instance created
        self.__client = Client()

        # trying to login into account
        print(f"--> Trying to login into your account @{username}")
        self.__client.login(username, password)
        print("--> Logged in successfully")

        # setting no. of posts to download
        self.posts_amount = int(posts_amount)

    # Method for downloading all the user medias
    def download_all_media(self, target: str) -> None:

        # downloads folder path
        DOWNLOAD_PATH = f"./downloads_{target}"
        
        # Getting user id from username
        print("--> Getting user id from username")
        user_id = self.__client.user_id_from_username(target)
        print(f"--> User id fetched - {user_id}")

        # Getting all the details of the user medias in form of list
        print("--> Getting all user media details")
        media_list = self.__client.user_medias(user_id, self.posts_amount)
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

    # Method for downloading media by url
    def download_by_url(self, url: str): 

        # Getting media pk from url
        pk = int(self.__client.media_pk_from_url(url))

        # Getting information about the media
        info = self.__client.media_info(pk)

        # Downloads folder path
        DOWNLOAD_PATH = f"./downloads_{pk}"

        createFolder(DOWNLOAD_PATH)
        
        if info.media_type == 1:
            # Method for downloading photo
            self.__client.photo_download(pk, DOWNLOAD_PATH)
            print(f"--> Downloaded media with id - {pk}")

        elif info.media_type == 2 and info.product_type == "feed":
            # Method for downloading video
            self.__client.video_download(pk, DOWNLOAD_PATH)
            print(f"--> Downloaded media with id - {pk}")
    
        elif info.media_type == 2 and info.product_type == "igtv":
            # Method for downloading igtv video
            self.__client.igtv_download(pk, DOWNLOAD_PATH)
            print(f"--> Downloaded media with id - {pk}")

        elif info.media_type == 2 and info.product_type == "clips":
            # Method for downloading reel
            self.__client.clip_download(pk, DOWNLOAD_PATH)
            print(f"--> Downloaded media with id - {pk}")

        else:
            # Method for downloading album (more than one media)
            self.__client.album_download(pk, DOWNLOAD_PATH)
            print(f"--> Downloaded media with id - {pk}")

        print("--> Finished")
