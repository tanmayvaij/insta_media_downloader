from packages.settings import *

class information:

    def __init__(self):

        # Checking if both username password exists or not
        if INSTAGRAM_USERNAME == "" or INSTAGRAM_PASSWORD == "":
            print("--> Username, Password not specified. Set them in packages/settings.py")
            print("--> Exiting")
            exit()
        else:
            self.INSTAGRAM_USERNAME = INSTAGRAM_USERNAME
            self.INSTAGRAM_PASSWORD = INSTAGRAM_PASSWORD
        
        # Setting number of posts to download. 0 (all) by default
        if NO_OF_POSTS == "":
            self.NO_OF_POSTS == "0"
        else:
            self.NO_OF_POSTS = NO_OF_POSTS
    
        # Checking if target account exists or not
        if TARGET_ACCOUNT == "":
            self.download_all_media_exists = False
        else:
            self.download_all_media_exists = True
            self.TARGET_ACCOUNT = TARGET_ACCOUNT
            print("--> target account available")

        # Checking if target url exists or not
        if MEDIA_URL == "":
            self.download_by_url_exists = False
        else:
            self.download_by_url_exists = True
            self.MEDIA_URL = MEDIA_URL
            print("--> target url available")
