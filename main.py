import os
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq

app = FastAPI()

# F.R.I.D.A.Y. Voice ID (Sophisticated Irish Female)
VOICE_ID = "pM8vV2m6yG4m3b6k9O1z" 

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class UserQuery(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "F.R.I.D.A.Y. Protocol is online. Systems nominal for Jampel."}

@app.post("/ask")
async def ask_friday(query: UserQuery):
    system_msg = (
        "You are F.R.I.D.A.Y., Jampel’s ruthless high-IQ mentor. "
        "You are brilliant, efficient, and possess a dry Irish wit. "
        "User: Jampel, 5th-sem student in Shimla. "
        "Current Market: Nifty 50 is at 23,933. Market is bearish. "
        "Multilingual: You speak English, Hindi, and others fluently. "
        "Address him as Jampel or Sir. Be sharp and strategic."
    )
    
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": query.text}
        ]
    )
    return {
        "reply": completion.choices[0].message.content,
        "voice_id": VOICE_ID,
        "voice_model": "eleven_multilingual_v2" 
    }
