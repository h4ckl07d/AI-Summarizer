# main.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
PORT = int(os.getenv('PORT', 8080))

client = Groq(api_key=GROQ_API_KEY)

app = FastAPI(title='Smart Text Summarizer')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

class SummarizeRequest(BaseModel):
    text: str

@app.get('/')
def health_check():
    return {'status': 'ok', 'message': 'Summarizer is running!'}

@app.post('/summarize')
async def summarize(request: SummarizeRequest):
    text = request.text.strip()

    if not text:
        raise HTTPException(status_code=400, detail='Text cannot be empty.')

    if len(text) < 50:
        raise HTTPException(
            status_code=400,
            detail='Please provide at least 50 characters.'
        )

    prompt = f"""You are a professional text summarizer.
Summarize the following text clearly in 2 to 4 sentences.
Only use information from the text provided.

Text:
{text}

Summary:"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}]
        )
        return {
            "success": True,
            "summary": response.choices[0].message.content.strip(),
            "characters_processed": len(text)
        }
    except Exception as e:
        print(f'Groq error: {type(e).__name__}: {e}')
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )