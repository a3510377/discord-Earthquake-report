# [![Discord](https://discord.com/api/guilds/808241076657717268/widget.png)](https://discord.gg/rCZeuaucjf)

# 此為 discord **地震報告**接收系統

### 設定方式

請於 .env 文件中放入你的 discord Token 和中央氣象局 Token
例如:

```env
token="token"
APIToken=""
```
( 找不到中央氣象局 Token 沒關西，你啟動後如果APIToken為空會發給你申請網址

你將於 main.py 文件中的第 13 行看到

```py
data = sets(
    os.getenv("token"), APIToken=os.getenv("APIToken")
)
```

可以換成

```py
data = sets(
    os.getenv("token"), APIToken=os.getenv("APIToken"),
    checkFile="你要確認文件放置的地方( 預設為./check.json",
    channels="你要發送到的頻道ID( 預設為無，頻道和頻道間請用空格區分，例如:100 200",
    Tags="當報告發出將通知的用戶ID或身分組ID( 預設為無，成員和成員間請用空格區分，例如:100 200"
)
```

### 安裝環境

請安裝 python >=3.8.2
windows 端請輸入

```cmd
pip install -r -U package.txt
```

### 開發人員

<a href="https://github.com/a3510377">
    <img width="100px" src="https://cdn.discordapp.com/avatars/688181698822799414/f6534feffc3f15cf439cb2fdd579aab5.webp?size=128">
</a>
