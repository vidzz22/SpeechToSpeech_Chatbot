# SpeechToSpeech_Chatbot
AI chatbot

File structure

SPEECHTOSPEECH_CHATBOT/  
│── backend/                  # Backend (Node.js/FastAPI)  
│   │── models/               # AI Models (Whisper, LLaMA 3.2, TTS)  
│   │── routes/               # API Endpoints  
│   │── services/             # Core Business Logic  
│   │── utils/                # Helper Functions  
│   │── app.py                # FastAPI Main Backend (Optional)  
│   │── server.js             # Node.js Main Backend  
│   │── Dockerfile            # Backend Dockerfile  
│   │── .env                  # Backend Environment Variables  
│   │── requirements.txt       # Python Dependencies (For FastAPI)  
│   │── package.json           # Node.js Dependencies  
│   └── README.md              # Backend Docs  
│  
│── frontend/                 # Frontend (Next.js)  
│   │── components/           # Reusable UI Components  
│   │── pages/                # Next.js Pages  
│   │── public/               # Static Assets (Images, Icons)  
│   │── styles/               # CSS & Tailwind Styles  
│   │── utils/                # Helper Functions  
│   │── Dockerfile            # Frontend Dockerfile  
│   │── .env.local            # Frontend Environment Variables  
│   │── package.json          # Frontend Dependencies  
│   └── README.md             # Frontend Docs  
│  
│── database/                 # MongoDB & Database Configurations  
│   │── models/               # MongoDB Schemas  
│   │── config.js             # Database Connection  
│   └── seed.js               # Initial Data Seeding  
│  
│── docker-compose.yml        # Docker Compose for Backend & Frontend  
│── .gitignore                # Ignore Files for Git  
│── README.md                 # Project Documentation  
