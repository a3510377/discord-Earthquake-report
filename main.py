import json
import os
import requests
from dotenv import load_dotenv
from discord.ext import commands, tasks

from typing import Optional, List


load_dotenv()

API_URLS = {
    "feel": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization={token}&limit=1&areaName=",
    "smallArea": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={token}&limit=1&areaName="
}


class Bot(commands.Bot):
    def __init__(
        self,
        *,
        channels: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        checkFile: Optional[str] = None,
        APIToken: Optional[str] = None,
        command_prefix: Optional[str] = None,
    ):
        super().__init__(
            command_prefix=command_prefix or os.getenv("PREFIX", "!"),
            help_command=None,
        )

        self.tags: List[str] = \
            tags or list(map(str, os.getenv("TAGS", "").split())) or []
        self.checkFile: str = \
            checkFile or os.getenv("CHECK_FILE", "check.json")
        self.APIToken: str = APIToken or os.getenv("APIToken")
        self.channels: List[str] = channels or []

        if not self.APIToken:
            raise Exception(
                "TOKEN 錯誤或未設置，請至 https://opendata.cwb.gov.tw/userLogin 獲取中央氣象局TOKEN並放置於 .env 檔案中"
            )

        try:
            open(self.checkFile)
        except FileNotFoundError:
            with open(self.checkFile, "w", encoding="utf-8") as file:
                json.dump({}, file, ensure_ascii=False)
                print(f"建立 {self.checkFile} 完成")

    async def on_ready(self):
        print("-" * 15)
        print(self.user.name)
        print(self.user.id)
        print(self.user)
        print("-" * 15)
        self.earthquake.start()

    @tasks.loop(minutes=1)
    async def earthquake(self):
        for url in API_URLS:
            r = requests.get(url).json()
            earthquake = r["records"]["earthquake"]
            if r["success"] != "true" or not earthquake:
                continue


bot = Bot()
bot.run(os.getenv("TOKEN"))
