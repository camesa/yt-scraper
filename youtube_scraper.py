import os
import pymongo
import googleapiclient.discovery
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Set up the YouTube API client with your API key
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=os.environ["YOUTUBE_API_KEY"])

# Set up the MongoDB client with your connection string
mongo_client = pymongo.MongoClient(os.environ["MONGODB_CONNECTION_STRING"])
mongo_db = mongo_client["youtube"]
mongo_channels_collection = mongo_db["channels"]
mongo_videos_collection = mongo_db["videos"]

# Get the keyword from user input
keyword = input("Enter the keyword you want to search for: ")

# Search for channels and save them to the MongoDB collection
channel_request = youtube.search().list(
    part="id,snippet",
    q=keyword,
    type="channel",
    maxResults=50
)
channel_response = channel_request.execute()
for item in channel_response["items"]:
    channel = {
        "id": item["id"]["channelId"],
        "title": item["snippet"]["title"],
        "description": item["snippet"]["description"],
        "thumbnail": item["snippet"]["thumbnails"]["default"]["url"],
        "publishedAt": item["snippet"]["publishedAt"],
    }
    mongo_channels_collection.insert_one(channel)

# Search for videos and save them to the MongoDB collection
video_request = youtube.search().list(
    part="id,snippet",
    q=keyword,
    type="video",
    maxResults=50
)
video_response = video_request.execute()
for item in video_response["items"]:
    video = {
        "id": item["id"]["videoId"],
        "title": item["snippet"]["title"],
        "description": item["snippet"]["description"],
        "thumbnail": item["snippet"]["thumbnails"]["default"]["url"],
        "publishedAt": item["snippet"]["publishedAt"],
        "channelId": item["snippet"]["channelId"],
    }
    mongo_videos_collection.insert_one(video)
