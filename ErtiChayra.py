import os
import telebot
import requests
import json
#Bot Token
BOT_TOKEN = "8083229980:AAGLFsB1eAXMyY1NpsQTp3_7wyami_uLh9Y"
#Api Key
API_KEY="1ac0de6adff7af251595a666ddba5c8cd8927411"
#Bot Chat ID
CHAT_ID = "8083229980"
#Bot Instance
bot = telebot.TeleBot(BOT_TOKEN)
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
print(requests.get(url).json())
#wallet adresses.
wallet_Adresses = {
    "shark":"LW8N4GF86AnAVg9Fts9bjNxF7b35YiRiUg ",
    "miketyson":"ltc1qa2jn004jkwa2rg5wy76gy6vqn2qh5297hm2gjw",
    "stitch":"LT7uEFVqJLfrZLcUzyg4svzQWfXnB6PgUG"
}
#Log Messages.
def log_message(message):
    p = "C:\\Users\\Saba\\Desktop\\Scam Dealers\\LOG.txt"
    # log
    f = open(p, mode="a")
    message = str(message).replace("None", "null")
    message = str(message).replace("'", '"')
    message = str(message).replace("False", 'false')
    message = str(message).replace("<", '"')
    message = str(message).replace(">", '"')

    jl = json.loads(message)
    f.write(f"\n\n\n")

    f.write("first_name: ")
    f.write("\t")
    for i in jl['json']['from']['first_name']:
        f.write(f"{str(i)}")

    f.write("\n")

    f.write("username: ")
    f.write("\t")
    for i in jl['json']['from']['username']:
        f.write(f"{str(i)}")

    f.write("\n")

    f.write("id: ")
    f.write("\t")
    for i in str(jl['json']['from']['id']):
        f.write(f"{str(i)}")

    f.write("\n")

    f.write("Text: ")
    f.write("\t\"")
    for i in jl['json']['text']:
        f.write(f"{str(i)}")
    f.write("\"")
    f.write(f"\n\n\n")
    f.close()
#Check Adress
def CheckAdress(url):
    urlltcUncomfirmed = f"https://rest.cryptoapis.io/blockchain-data/litecoin/mainnet/address-transactions-unconfirmed/{url}?context=yourExampleString&limit=50&offset=0"
    # urlltcconfirmed=f"https://rest.cryptoapis.io/blockchain-data/litecoin/mainnet/addresses/LW8N4GF86AnAVg9Fts9bjNxF7b35YiRiUg/transactions?context=yourExampleString&limit=50&offset=0"
    querystring = {"context": "yourExampleString", "limit": "50", "offset": "0"}
    headers = {
        'x-api-key': "1ac0de6adff7af251595a666ddba5c8cd8927411"
    }
    req = requests.get(urlltcUncomfirmed, headers=headers, params=querystring).json()
    req = requests.get(urlltcUncomfirmed, headers=headers, params=querystring).json()
    req = str(req).replace("None", "null")
    req = str(req).replace("'", '"')
    req = str(req).replace("False", 'false')
    jl = json.loads(str(req))
    if jl['data']['items'] == []:
        return str(f"Total Uncomfirmed Incoming BARIGASNAME Transactions: Empty")
    else:
        #check if sender is the url itself.
        # if jl['data']['items'][0]['senders'][0]['address'] == url:
        #     #if yes then return empty
        #     return str(f"Total Uncomfirmed Incoming BARIGASNAME Transactions: Only Outgoing Transactions")
        msg = ""
        msg = "Incoming Uncomfirmed Transactions  of BARIGASNAME Are:transactionId:         "
        for i in jl['data']['items'][0]['transactionId']:
            msg = msg + str(i)
        msg = msg + "                     recipients:                  "
        for i in jl['data']['items'][0]['recipients']:
            msg = msg + str(i)
        msg = msg + "                   senders:                   "
        for i in jl['data']['items'][0]['senders']:
            if i['address'] == url:
                continue
            msg = msg + str(i)
        return msg
@bot.message_handler(commands=['checkall'])
#Check Every Wallet Addresses.
def checkAll(message):
    msg = ""
    msg += CheckAdress(wallet_Adresses['shark']).replace("BARIGASNAME","Shark")
    msg+=f"\n{CheckAdress(wallet_Adresses['miketyson']).replace("BARIGASNAME","MikeTyson")}"
    msg += f"\n{CheckAdress(wallet_Adresses['stitch']).replace("BARIGASNAME", "Stitch")}"
    bot.reply_to(message, msg)
    log_message(message)
@bot.message_handler(commands=['shark'])
#Check Shart Wallet Address
def CheckShark(message):
    bot.reply_to(message,CheckAdress(wallet_Adresses['shark']).replace("BARIGASNAME","Shark"))
    log_message(message)
#Check MikeTyson Wallet Address
@bot.message_handler(commands=['miketyson'])
def CheckMike(message):
    log_message(message)
    bot.reply_to(message,CheckAdress(wallet_Adresses['miketyson']).replace("BARIGASNAME","MikeTyson"))
@bot.message_handler(commands=['stitch'])
def CheckStitch(message):
    log_message(message)
    bot.reply_to(message,CheckAdress(wallet_Adresses['stitch']).replace("BARIGASNAME","Stitch"))
#start and hello Commands
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Wsup?")
    bot.send_message(message,"@Qvaba")
#Echo on All The Messages.
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    log_message(message)
bot.infinity_polling()