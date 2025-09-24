# 🎵 Discord MusicMate

MusicMate is a simple and clean **Discord Music Bot** built with Python.  
It can **play music from YouTube**, manage a queue, and control playback.

> Repo: [Vibe-Coding](https://github.com/nafiul-afk/Vibe-Coding) → `Discord-MusicMate/`

---

## 📂 Project Structure
```

Discord-MusicMate/
├─ bot.py                # main bot code
├─ requirements.txt      # Python dependencies
├─ README.md             # documentation
├─ .gitignore            # ignore cache & secrets
└─ .github/
      └─ workflows/
             └─ deploy.yml      # GitHub Actions workflow (optional)

````

---

## 🚀 Features
- `!play [song name or YouTube URL]` — Plays or queues a song
- `!pause` — Pauses the music
- `!resume` — Resumes playback
- `!skip` — Skips the current song
- `!queue` — Shows the song queue
- `!stop` — Stops playback and leaves the voice channel

---

## 🛠️ Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/nafiul-afk/Vibe-Coding.git
cd Vibe-Coding/Discord-MusicMate
````

### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 3️⃣ Install FFmpeg

* Download FFmpeg from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
* Extract and add the **bin** folder to your system PATH (so `ffmpeg` works from terminal).

### 4️⃣ Create a Discord Bot

* Go to [Discord Developer Portal](https://discord.com/developers/applications)
* Create a new **Application** → Go to **Bot** → Add Bot
* Copy the **Bot Token**
* Under the **Bot** tab, scroll down and enable:

  * **MESSAGE CONTENT INTENT**
  * (Voice permissions are automatic when the bot joins voice channels)

### 5️⃣ Add Your Token

You can either:

* Edit `bot.py` and replace `YOUR_BOT_TOKEN_HERE`
  **OR**
* Keep your token safe using environment variables:

```bash
export DISCORD_TOKEN=your_bot_token_here
```

(Windows PowerShell)

```powershell
$env:DISCORD_TOKEN="your_bot_token_here"
```

### 6️⃣ Run the Bot

```bash
python bot.py
```

---

## 🌐 Deployment Options

You can keep the bot running 24/7 by hosting it on:

* [Railway](https://railway.app/)
* [Render](https://render.com/)
* [Heroku](https://heroku.com/)
* GitHub Actions + your own server (workflow file included in `.github/workflows/deploy.yml`)

> If deploying on GitHub Actions or Railway, add `DISCORD_TOKEN` as an environment variable / secret.

---

## 🧩 Tech Stack

* Python 3.9+
* [discord.py](https://pypi.org/project/discord.py/)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [FFmpeg](https://ffmpeg.org/)

---

## 🤝 Contributing

Contributions are welcome!
Fork the repo → create a new branch → commit changes → open a Pull Request.

---





