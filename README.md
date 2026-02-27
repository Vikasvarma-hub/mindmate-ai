# 🧠 MindMate AI — Your Personal Mental Health Companion

> "Unlike generic AI chatbots that forget you after every session, MindMate remembers you, tracks your emotions over time, adapts to your age, and guides you through real CBT therapy — turning a one-time conversation into a long-term mental health relationship."

---

## ✨ Features

- 💬 **AI Chat** — Age-adaptive personas for Teen, Adult, and Senior users
- 🧘 **CBT Therapy Session** — Structured 5-step Cognitive Behavioral Therapy with personal insight card
- 📖 **AI Journal** — Write freely, get emotional analysis and reflection questions
- 🎯 **Goal Tracking** — Set weekly goals, track streaks, get AI encouragement
- 🧬 **Mental Health Profile** — Personalised profile built from your data over time
- 🌬️ **Breathing Exercises** — Box Breathing, 4-7-8, and Deep Calm with guided animation
- 🧠 **Long-Term Memory** — Remembers you across sessions via Firebase
- 📊 **Mood Tracking** — Detects emotion on every message, tracks journey over time

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| AI Model | Groq — llama-3.3-70b-versatile |
| Database | Firebase Realtime Database |
| Auth | Firebase Authentication |
| Language | Python |

---

## 🚀 Run Locally

```bash
git clone https://github.com/Vikasvarma-hub/mindmate-ai.git
cd mindmate-ai
pip install -r requirements.txt
streamlit run app.py
```

Add your keys in a `.env` file:
```
GROQ_API_KEY=your_groq_key
```
And add your `firebase_key.json` in the root folder.

---

## 📁 Project Structure

```
mindmate-ai/
├── app.py              # Main Streamlit app — 6 tabs
├── brain.py            # AI response, emotion detection, memory summary
├── memory.py           # Chat history, long-term memory, mood tracking
├── therapist.py        # CBT session logic and insight card
├── journal.py          # Journal analysis
├── goals.py            # Goal tracking and encouragement
├── mental_profile.py   # Personal mental health profile generator
├── safeguard.py        # Crisis detection and off-topic guard
├── profile_manager.py  # Age group logic
├── firebase_config.py  # Firebase initialisation
└── requirements.txt
```

---

## ⚠️ Disclaimer

MindMate is an AI companion, not a licensed therapist.
In crisis? Call **iCall: 9152987821** or **Vandrevala Foundation: 1860-2662-345**