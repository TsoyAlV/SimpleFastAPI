from fastapi import FastAPI
from typing import Optional
import pandas as pd
import json

app = FastAPI()


@app.get("/")
async def root():
    return "Check List"

