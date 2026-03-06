# 🔥 Resume Roaster AI

> Upload your resume. Get brutally honest (but constructive) feedback in seconds.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=flat-square)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green?style=flat-square)

## What is this?

Resume Roaster is a fun AI-powered app that gives your resume a **comedy-roast-style review** — think brutal honesty meets real career advice. Upload your resume, pick a roast level, and see if you can survive the heat. 🔥

## Features

- 📄 **PDF & TXT support** — Drop your resume and go
- 🌶️ **3 roast levels** — Mild, Medium, or Savage
- ⚡ **Fast feedback** — Results in ~5 seconds
- 🛠️ **Actually useful** — Real actionable advice under the humor
- 📥 **Downloadable roast** — Save your roast as markdown
- 🔒 **Privacy first** — Your resume is never stored

## Quick Start

### 1. Clone & install

```bash
git clone <your-repo-url>
cd resume-roaster-ai
python -m venv venv

# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Add your API key

Create a `.env` file (or edit the existing one):

```
OPENAI_API_KEY=sk-your-actual-key-here
```

Or just paste it in the sidebar when the app runs.

### 3. Run it

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501` 🚀

## Project Structure

```
resume-roaster-ai/
├── app.py              # Main Streamlit app
├── roaster.py          # LLM roasting engine
├── parser.py           # PDF/TXT text extraction
├── .env                # API key (not committed)
├── .gitignore
├── .streamlit/
│   └── config.toml     # Dark theme config
├── requirements.txt
└── README.md
```

## How It Works

1. **Upload** — Your resume is parsed with PyMuPDF (PDF) or read as text (TXT)
2. **Prompt** — The text is sent to GPT-4o-mini with a comedy-roast system prompt
3. **Roast** — The AI scores your resume, highlights strengths, roasts weaknesses, and gives real fixes
4. **Share** — Copy your roast results or download as markdown

## Roast Levels

| Level     | Vibe                                          |
| --------- | --------------------------------------------- |
| Mild 😊   | Gentle teasing, mostly encouragement          |
| Medium 🔥 | Classic roast — balanced burns + advice       |
| Savage 💀 | Full send. Maximum burns. Still constructive. |

## Tech Stack

- **Frontend**: Streamlit
- **LLM**: OpenAI GPT-4o-mini
- **PDF Parsing**: PyMuPDF
- **Styling**: Custom CSS with fire gradients 🔥

## License

MIT — roast freely.
