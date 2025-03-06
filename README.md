# SpeechToSpeech_Chatbot
AI chatbot

File structure

SPEECHTOSPEECH_CHATBOT/  
SPEECHTOSPEECH_CHATBOT/  
├── docker-compose.yml         # Orchestrates frontend, backend, and MongoDB services
├── .env                       # Global environment variables (e.g., DB URI, JWT secret)
├── README.md
│
├── frontend/                  # Next.js frontend
│   ├── Dockerfile             # Dockerfile for the Next.js app
│   ├── package.json
│   ├── next.config.js
│   ├── public/                # Public assets
│   │   ├── logo.png           # Platform logo
│   │   └── styles.css         # CSS file for custom styling
│   └── pages/
│       ├── index.js           # Home page (chat interface, etc.)
│       └── dashboard.js       # User dashboard (credits, profile, etc.)
│
└── backend/                   # FastAPI backend
    ├── Dockerfile             # Dockerfile for the FastAPI app
    ├── requirements.txt       # Python dependencies (FastAPI, uvicorn, pymongo, python-jose, etc.)
    ├── main.py                # FastAPI application (routes for auth, STT, LLM, TTS, credits)
    └── config.py              # Database & environment configuration (loads .env values)
