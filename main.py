from fastapi import FastAPI
import httpx
from fastapi.responses import JSONResponse
import datetime
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/me")
async def read_me():
        try:
            profile = {
            "status": "success",
            "user": {
                "name": "Teminioluwa Adekoya",
                "email": "teminioluwaopemipo@gmail.com",
                "stack": "Python/FastAPI",
                "linkedIn": "https://www.linkedin.com/in/teminioluwa-adekoya-6537a2294/",
                "github": "https://github.com/temake"
            },
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "fact": "No fact available."
        }
            try:
                async with httpx.AsyncClient(timeout=5.0) as client:
                    resp = await client.get("https://catfact.ninja/fact")
                    resp.raise_for_status()
                    profile["fact"] = resp.json().get("fact", profile["fact"])
            except httpx.HTTPError:
                profile["fact"] = "Unable to fetch cat fact at this time."
            return JSONResponse(content=profile)

        except Exception as e:
             print(f"An Error Occured : {e}")