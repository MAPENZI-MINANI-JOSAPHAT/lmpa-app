from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="LMPA Quantitative Observatory")

# Monter le dossier assets pour les images et le manifest
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Dossier des templates HTML
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
