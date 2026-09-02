# Empathetic-AI-Mental-Wellness-Advisor

A multilingual AI-powered **Mental Peace Advisor chatbot** built with **Streamlit and Google Gemini**. The application provides a conversational interface where users can share their feelings, receive empathetic responses, and interact with the chatbot through both **text and voice input**.

The chatbot supports multiple languages and uses Google Gemini to generate supportive, context-aware responses based on the user's message.

## Features

- **AI Emotional Support** — Provides compassionate and supportive responses to users.
- **Google Gemini Integration** — Uses Gemini models to generate natural-language responses.
- **Multilingual Support** — Supports English, Urdu, Sindhi, Punjabi, Chinese, Arabic, French, Spanish, German, Persian, and Turkish.
- **Text Chat** — Users can communicate with the chatbot through a simple Streamlit chat interface.
- **Voice Input** — Converts spoken input into text using SpeechRecognition and Google Speech Recognition.
- **Language-Aware Voice Recognition** — Uses language-specific speech recognition codes.
- **Conversation History** — Maintains the conversation during the current Streamlit session.
- **Formatted Responses** — Converts bullet points and bold text into styled HTML for better readability.
- **Responsive Chat UI** — Separate visual styles for user and chatbot messages.
- **Fallback Model** — Attempts to use another Gemini model when the primary model reaches its quota.
- **Custom Styling** — Uses CSS to create a clean and friendly interface.

## AI Capabilities

The chatbot is instructed to respond appropriately to different emotional situations.

Examples include:

- **Sadness** — Provides comforting and uplifting responses.
- **Criticism or Scolding** — Offers reassurance and positive encouragement.
- **Anxiety or Panic** — Suggests simple breathing exercises.
- **Loneliness** — Encourages healthy connection with friends or family.
- **Grief** — Responds with empathy and acknowledges that healing takes time.
- **Low Self-Esteem** — Provides positive affirmations and encouragement.
- **Unclear Messages** — Asks the user for additional context.
- **Conversation Exit** — Responds with a farewell when the user says "quit".

## Supported Languages

| Language | Code |
|---|---|
| English | `en` |
| Urdu | `ur` |
| Sindhi | `sd` |
| Punjabi | `pa` |
| Chinese | `zh` |
| Arabic | `ar` |
| French | `fr` |
| Spanish | `es` |
| German | `de` |
| Persian | `fa` |
| Turkish | `tr` |

The application also maps these language codes to speech-recognition locales such as `en-US`, `ur-PK`, `zh-CN`, `ar-SA`, and `fr-FR`.

## How It Works

```text
                    User
                     │
             ┌───────┴────────┐
             │                │
          Text Input       Voice Input
             │                │
             │          Speech Recognition
             │                │
             └───────┬────────┘
                     ▼
              User Message
                     │
                     ▼
             Language Selection
                     │
                     ▼
              Gemini AI Model
                     │
                     ▼
           Supportive AI Response
                     │
                     ▼
             Response Formatting
                     │
                     ▼
               Chat Interface
```

## Project Structure

```text
mental-peace-advisor/
│
├── app.py
│
├── mental_peace_advisor/
│   ├── __init__.py
│   ├── model_api.py
│   ├── config.py
│   ├── chat_ui.py
│   └── formatting.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Core Components

### `app.py`

The main Streamlit application.

It handles:

- Page configuration
- Language selection
- Chat input
- Conversation state
- Voice input
- Speech recognition
- Displaying chatbot responses
- Custom CSS styling

Example:

```python
reply = get_bot_response(
    user_input.strip(),
    language=st.session_state.lang
)
```

### `model_api.py`

Responsible for communication with Google Gemini.

The module:

1. Receives the user's message.
2. Builds the chatbot prompt.
3. Adds behavioral guidelines.
4. Passes the selected language.
5. Sends the prompt to Gemini.
6. Returns the generated response.

The application also includes quota handling:

```text
Primary Gemini Model
        │
        ▼
   API Request
        │
   ┌────┴────┐
   │         │
Success   Quota Error
   │         │
   ▼         ▼
Response   Backup Model
```

### `config.py`

Contains Gemini configuration such as:

- API key
- Model name
- Generation configuration
- Temperature

Example configuration:

```python
GEN_CONFIG = {
    "temperature": 0.5
}
```

### `chat_ui.py`

Responsible for rendering the conversation.

User messages are displayed separately from chatbot messages, creating a familiar chat-style interface.

```text
                  User Message
                       ───────►

◄────── Mental Peace BOT Response
```

### `formatting.py`

Converts Gemini responses into styled HTML.

It supports:

- Paragraph formatting
- Bullet points
- Bold text
- Spacing
- HTML list formatting

For example:

```text
**Take a short break.**

- Drink some water.
- Take a few deep breaths.
- Talk to someone you trust.
```

is converted into formatted HTML for Streamlit.

## Voice Interaction

The application supports microphone-based interaction using:

- `SpeechRecognition`
- `PyAudio`
- Google Speech Recognition

Workflow:

```text
Microphone
    ↓
SpeechRecognition
    ↓
Audio → Text
    ↓
Gemini
    ↓
AI Response
    ↓
Chat Interface
```

The speech recognition language is automatically selected based on the user's chosen chatbot language.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd mental-peace-advisor
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
MODEL_NAME=gemini-1.5-flash
```

Then load the variables in `config.py` instead of hardcoding credentials.

For example:

```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-flash")

GEN_CONFIG = {
    "temperature": 0.5
}
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser with the Mental Peace Advisor interface.

## Usage

### 1. Select a Language

Choose a preferred language from the language selector.

### 2. Send a Message

Type your message in the chat input.

Example:

```text
I'm feeling very stressed today.
```

The chatbot generates a supportive response.

### 3. Use Voice Input

Click:

```text
🗣️ Start Speaking
```

Allow microphone access and speak naturally.

The application converts your speech into text and sends it to Gemini.

### 4. Continue the Conversation

The conversation remains available during the active Streamlit session.

## Example Interaction

```text
User:
I feel lonely and don't know what to do.

Mental Peace BOT:
It's understandable to feel lonely sometimes. You don't have
to handle everything by yourself.

- Consider talking to someone you trust.
- Take a short walk or spend some time outside.
- Do something small that usually makes you feel comfortable.
```

## Technology Stack

| Category | Technology |
|---|---|
| Frontend / UI | Streamlit |
| AI Model | Google Gemini |
| Programming Language | Python |
| Voice Recognition | SpeechRecognition |
| Audio Input | PyAudio |
| Data Processing | Pandas, NumPy |
| Response Formatting | HTML + Regex |
| Configuration | Python / Environment Variables |

## Requirements

Main dependencies include:

```text
streamlit
google-generativeai
SpeechRecognition
PyAudio
gTTS
pandas
numpy
```

Install everything with:

```bash
pip install -r requirements.txt
```

## Security

Never commit API keys or other credentials to GitHub.

Your current `config.py` contains a hardcoded Google API key. That key should be **revoked/rotated** and replaced with an environment variable.

Add the following to `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
venv/
```

Use:

```env
GOOGLE_API_KEY=your_new_api_key
```

instead of:

```python
API_KEY = "your-secret-api-key"
```

## Important Disclaimer

This chatbot is designed to provide **general emotional support and conversational guidance**. It is not a replacement for a licensed mental-health professional, therapist, doctor, or emergency service.

For serious or urgent situations, users should seek help from a qualified professional or appropriate emergency support service.

## Future Improvements

- **Text-to-Speech** for spoken chatbot responses
- **Persistent Conversation History**
- **User Authentication**
- **Database Integration**
- **Personalized Conversations**
- **Emotion/Sentiment Detection**
- **Conversation Analytics**
- **Improved Safety Guardrails**
- **Streaming Gemini Responses**
- **Mobile-Friendly UI**
- **Cloud Deployment**
- **Professional Mental-Health Resource Integration**

## Author

Jawaria Tariq

## License

This project is intended for educational and experimental purposes.
