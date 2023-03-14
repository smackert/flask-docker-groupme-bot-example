import logging, re
import urllib.request
import re, requests


def search_yt(query):
    try:
        logging.info(f"searching YT for: {query}")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        video_link = "https://www.youtube.com/watch?v=" + video_ids[0]
        logging.info(f"Found video: {video_link}") 
        return video_link 
    except:
        logging.warn("Failed to search YT!")

def search_yt_api(query):
    try:
        logging.info(f"searching YT for: {query}")
        res = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=" + requests.utils.quote(query) +"&key={YOUTUBE_API_KEY}")
    except:
        logging.warn("Failed to search YT API.")
    if res is not None:
        try:
            video_id = res.json()['items'][0]['id']['videoId']
            video_link = "https://www.youtube.com/watch?v=" + video_id
            return video_link
        except:
            logging.warn("Failed parsing YT JSON search results.")
    

def get_response(bot, req):
    text = req['text']
    name = req['name']
    user_id = req['user_id'] 

    # check if msg is from self
    if bot.chat_name == name:
        return 

    # GLOBAL FUNCTIONS
    if(re.search(r"^yt[\s]", text, re.IGNORECASE)):
        query = text[3:]
        return search_yt_api(query)
    
    # BOT CASES
    if bot.bot_num == "bot1" or bot.bot_num == "bot3":
        if(re.search("{TRIGGER_WORD}", text, re.IGNORECASE)):
            return "{FUNNY_PICTURE_LINK}"
    
    if bot.bot_num == "bot2":
        return None

    if bot.bot_num == "bot3":
        if(re.search("foxbody", text)):
            logging.warn(f"{bot.bot_num} is responding to {bot.chat_name} = {name}")
            return "pic of a mustang foxbody"

    logging.info("No valid responses found. Ignoring.")
    return None

def get_response2(bot, req):
    text = req['text']
    name = req['name']
    user_id = req['user_id']

    if bot.chat_name == name:
        return 
    if bot.bot_num == "bot3":
        if(re.search("{TRIGGER_WORD}", text, re.IGNORECASE)):
            return "http://i.imgur.com/thz9832"
        if(re.search("boxfody", text)):
            return "pic of a mustang boxfody"

