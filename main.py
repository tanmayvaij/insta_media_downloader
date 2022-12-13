from instagrapi import Client

class Insta_Media_Downloader:

    def __init__(self, username, password):
        self.client = Client()
        self.client.login(username, password)

    def get_user_id(self, target):
        return self.client.user_id_from_username(target)

    def fetch_medias_list(self, userid):
        raw_list = self.client.user_medias(userid)
        return [ 
            {  
                "pk": int(i.pk), 
                "media_type": i.media_type, 
                "product_type": i.product_type 
            } 
            for i in raw_list 
        ]

    def download_media(self, media_list):

        for i in media_list:
            
            if i['media_type'] == 1:
                print(self.client.photo_download(i['pk']))

            elif i['media_type'] == 2 and  i['product_type'] == "feed":
                print(self.client.video_download(i['pk']))

            elif i['media_type'] == 2 and i['product_type'] == "igtv":
                print(self.client.igtv_download(i['pk']))

            elif i['media_type'] == 2 and i['product_type'] == "clips":
                print(self.client.clip_download(i['pk']))

            else:
                print(self.client.album_download(i['pk']))

downloader = Insta_Media_Downloader("tony_bot_224", "Tejomay@000")

downloader.download_media(
    downloader.fetch_medias_list(
        downloader.get_user_id("blue_dive_")
    )
)
