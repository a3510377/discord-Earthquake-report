# [![Discord](https://discord.com/api/guilds/808241076657717268/widget.png)](https://discord.gg/rCZeuaucjf)

# 此為 discord **地震報告**接收系統

### 設定方式

請於 .env 文件中放入你的 discord Token 和中央氣象局 Token
例如:

- 如果 discord bot Token 為: `XXX`
- 如果 中央氣象局 API 授權碼為: `CWB-168DA0A5-FGH0-42D9-C50A-49G0004CCD0`

```env
token="XXX"
APIToken="CWB-168DA0A5-FGH0-42D9-C50A-49G0004CCD0"
```

( 找不到中央氣象局 Token 沒關係，你啟動後如果 APIToken 為空會發給你申請網址

#### 若為 repl.it 架設，建議使用 **https://app.jsonstorage.net/** API

檔案設定請添加:

- 如果 jsonstorage 裡的 Get Json 網址為: `https://app.jsonstorage.net/#/items/f351da5d-ba45-4f22-8a33-ec2970b0198f` (取 https://app.jsonstorage.net/#/items/ 後面那一段
- 如果 jsonstorage 裡的 Api Keys 為: `cc041cf0-69ef-49c0-8caa-5016330505b4`

```env
JsonUrl="f351da5d-ba45-4f22-8a33-ec2970b0198f"
JsonUrlToken="cc041cf0-69ef-49c0-8caa-5016330505b4"
```

並使用 repl.it.py 為主檔

---

你將於 main.py or repl.it.py 文件中的第 13 行看到

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
