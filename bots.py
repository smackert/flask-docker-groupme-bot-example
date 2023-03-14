import logging
import requests
logger = logging.getLogger(__name__)

class Bots():
    bot_list = {}
    def __init__(self, bot_num, chat_name, bot_id, desc):
        self.chat_name = chat_name
        self.bot_num = bot_num
        self.bot_id = bot_id 
        self.desc = desc
        
        Bots.bot_list[bot_num] = self

        logger.info(f"New bot registered: {self.chat_name} - {self.desc}")
    
    def echo(self, newmessage):
        return newmessage

    def send(self, response):
        post_message = {"text" : response, "bot_id" : self.bot_id}
        logging.info(f"SENDING MESSAGE:{self.chat_name}:{post_message}")
        requests.post("https://api.groupme.com/v3/bots/post", json=post_message)
        return