from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from text import extract_text_from_image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        
    allow_credentials=True,
    allow_methods=["*"],       
    allow_headers=["*"],        
)

@app.post("/extract-text/")
async def extract_text(file_path: str):
    extracted_text = extract_text_from_image(file_path)
    return {"extracted_text": extracted_text}
