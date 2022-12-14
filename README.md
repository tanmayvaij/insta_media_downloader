# Insta Media Downloader

## Setup Instructions

### 1. Install all the script dependencies.
```sh
python3 install -r requirements.txt
```

### 2. In the packages/setting.py add the following details. Either of the last three variables can be empty string.
```env

INSTAGRAM_USERNAME="<your_instagram_username>"

INSTAGRAM_PASSWORD="<your_instgram_password>"

TARGET_ACCOUNT="<your_target_account>"

NO_OF_POSTS="<amount_of_posts_to_download>"

MEDIA_URL="<url_of_target_media>"

```

### 3. Start the script
```sh
python3 ./main.py
```
