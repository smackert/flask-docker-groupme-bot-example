from flask import Flask, request, render_template
from dotenv import find_dotenv
import requests, json, os, logging
from bots import Bots
from responses import get_response, get_response2 
from types import SimpleNamespace

find_dotenv()
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# register bots
bot1 = Bots("bot1", "{BOT_NAME}", "{BOT_KEY}", "main chat") # main chat 
bot2 = Bots("bot2", "{BOT_NAME}", "{BOT_KEY}", "music chat") # music chat 
bot3 = Bots("bot3", "{BOT_NAME}", "{BOT_KEY}", "test chat") # test chat


@app.route("/")
def hello_world():
    return "<p>Hello, World! I'm in docker!</p>"

@app.route("/bot3/echo", methods=["POST"])
def echo():
    response = bot3.echo(request.json)
    logging.info(f"Echoing message: {response}") 
    return f"<h1>Echo</h1><p>{response}</p>"

@app.route("/test-post-data")
def test_post_data():
    test_message = {"attachments":[],"avatar_url":"https://i.groupme.com/","created_at":1302623328,"group_id":"1234567890","id":"1234567890","name":"John","sender_id":"12345","sender_type":"user","source_guid":"GUID","system":False,"text":"Hello world ☃☃","user_id":"1234567890"}
    r = requests.post("http://127.0.0.1:42010/bot3/newmessage", json=test_message)
    # bot3.send("it verkud!")
    return ''

@app.route("/<bot_num>/newmessage", methods=["POST"])
def bot3_newmessage(bot_num):
    bot = Bots.bot_list[bot_num]
    r = request.json
    response = get_response(bot, r)
    if response is not None:
        logging.info(f"{bot.bot_num} responding to {r['name']}: {response}")
        bot.send(response)
        return ''
    else:
        logging.info("No action.")
        return '' 