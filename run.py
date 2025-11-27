from fastapi import FastAPI
from mediaflow_proxy.main import app as mediaflow_app

# App principale esposta a Hugging Face
main_app = FastAPI()

# Monta direttamente MediaFlow Proxy sotto "/"
main_app.mount("/", mediaflow_app)
