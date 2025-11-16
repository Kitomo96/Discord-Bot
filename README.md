# Python Discord Bot (with Gemini AI)

This is a Discord bot built with `discord.py` that was created as a project for Codedex. It has been expanded to include generative AI responses using the Google Gemini API.

## 🚀 Features

* **Meme Command**: Responds to `$meme` by fetching a random meme from the `meme-api`.
* **AI Chatbot**: Responds to any message that **@mentions** the bot. It uses the `gemini-2.5-flash-lite` model to generate a unique response to the user's prompt.

## 🔧 Setup and Installation

To run this bot yourself, follow these steps.

### 1. Clone the Repository

```bash
git clone [https://github.com/Kitomo96/Discord-Bot.git](https://github.com/Kitomo96/Discord-Bot.git)
cd Discord-Bot
```
### 2. Install Dependencies

It's recommended to use a virtual environment. Once you've set one up, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Create Your Environment File

This repository includes a file named .env.example.

1- Rename this file to .env

2 -Open the new .env file and enter your secret keys.

It should look like this:

DISCORD_TOKEN=your_discord_bot_token_here
GEMINI_API_KEY=your_google_ai_studio_key_here