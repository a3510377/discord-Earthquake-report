import json
import os

import requests
from discord.ext import commands, tasks
from dotenv import load_dotenv

import discord
from function import *

load_dotenv()
bot = commands.Bot(command_prefix="!")
data = sets(
    os.getenv("token"), APIToken=os.getenv("APIToken"))


def setup():
    try:
        open(data.checkFile)
    except:
        with open(data.checkFile, "w") as outfile:
            json.dump({}, outfile, ensure_ascii=False, indent=4)
            print("建立 check.json 完成")


@bot.event
async def on_ready():
    print("-"*15)
    print(bot.user.name)
    print(bot.user.id)
    print(bot.user)
    print("-"*15)
    setup()
    if data.APIToken:
        earthquake.start()
        print("地震報告啟動")
    else:
        print("請至 https://opendata.cwb.gov.tw/userLogin 獲取中央氣象局TOKEN並放置於 .env 檔案中")


@tasks.loop(seconds=10)
async def earthquake():
    # 大型地震
    API = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization={data.APIToken}&format=JSON&areaName="
    # 小型地震
    API2 = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={data.APIToken}&format=JSON"

    b = requests.get(API).json()
    s = requests.get(API2).json()
    _API = b["records"]["earthquake"][0]["earthquakeInfo"]["originTime"]
    _API2 = s["records"]["earthquake"][0]["earthquakeInfo"]["originTime"]

    async def goTo(how, now):
        for ch in data.channels:
            await sosIn(bot.get_channel(ch),({API: b,API2: s}[how]), data)
        with open(data.checkFile, 'w') as outfile:
            json.dump(now, outfile, ensure_ascii=False, indent=4)

    with open(data.checkFile, "r") as file:
        file = json.load(file)
    for i in [API, API2]:
        if not file.get(i):
            file[i] = ""
    if file[API] != _API:
        file[API] = _API
        await goTo(API, file)
    if file[API2] != _API2:
        file[API2] = _API2
        await goTo(API2, file)

bot.run(data.token)
