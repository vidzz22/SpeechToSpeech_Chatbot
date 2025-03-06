from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from jose import JWTError, jwt
from config import settings

app = FastAPI(title="Speech-to-Speech Chatbot API")

# Configure CORS for your frontend (adjust origin as needed)
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to MongoDB
client = MongoClient(settings.MONGO_URI)
db = client.get_default_database()  # or specify your DB name

# Pydantic models for user and token
class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# JWT configuration
SECRET_KEY = settings.JWT_SECRET
ALGORITHM = "HS256"

@app.get("/")
def read_root():
    return {"message": "Welcome to the Speech-to-Speech Chatbot API"}

@app.post("/auth/signup")
def signup(user: User):
    if db.users.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already exists")
    # Initialize with default credits (e.g., 100)
    user_data = user.dict()
    user_data["credits"] = 100
    db.users.insert_one(user_data)
    return {"message": "User created successfully"}

@app.post("/auth/login", response_model=Token)
def login(user: User):
    db_user = db.users.find_one({"username": user.username})
    if not db_user or db_user["password"] != user.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token_data = {"sub": user.username}
    access_token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(lambda request: request.headers.get("Authorization"))):
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    token = token.replace("Bearer ", "")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/stt")
def speech_to_text(request: Request, current_user: str = Depends(get_current_user)):
    # Stub implementation for Speech-to-Text processing
    # Integrate your Whisper-based processing here
    return {"message": "STT processing endpoint", "user": current_user}

@app.post("/llm")
def generate_response(request: Request, current_user: str = Depends(get_current_user)):
    # Stub implementation for LLM-based response generation
    # Integrate your LLaMA (or alternative) processing here
    return {"message": "LLM response generation endpoint", "user": current_user}

@app.post("/tts")
def text_to_speech(request: Request, current_user: str = Depends(get_current_user)):
    # Stub implementation for Text-to-Speech conversion
    # Integrate your Coqui TTS or Google TTS processing here
    return {"message": "TTS processing endpoint", "user": current_user}

@app.get("/credits")
def get_credits(current_user: str = Depends(get_current_user)):
    user = db.users.find_one({"username": current_user})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    credits = user.get("credits", 100)
    return {"username": current_user, "credits": credits}
