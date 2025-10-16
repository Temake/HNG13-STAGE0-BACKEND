from fastapi import FastAPI
import httpx

import datetime
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/me")
async def read_me():
    profile = {
        "name": "Teminioluwa Adekoya",
        "email": "teminioluwaopemipo@gmail.com",
        "stack":"Python/FastAPI",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "github": "https://github.com/temake"
    }

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get("https://catfact.ninja/fact")
            resp.raise_for_status()
            profile["fact"] = resp.json().get("fact", "No fact available.")
    except httpx.HTTPError:
        profile["fact"] = "Unable to fetch cat fact at this time."

    return profile