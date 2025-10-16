from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/me")
async def read_me():
    profile = {
        "name": "Teminioluwa Adekoya",
        "role": "Backend Engineer",
        "location": "Lagos, Nigeria",
        "github": "https://github.com/temake"
    }

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get("https://catfact.ninja/fact")
            resp.raise_for_status()
            profile["cat_fact"] = resp.json().get("fact", "No fact available.")
    except httpx.HTTPError:
        profile["cat_fact"] = "Unable to fetch cat fact at this time."

    return profile