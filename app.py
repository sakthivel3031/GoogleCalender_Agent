from fastapi import FastAPI
from functions import run_conversation

app = FastAPI()


@app.post("/calender")
async def main(prompt: str):
    output = run_conversation(prompt)
    return output
