# Starter code for FastAPI REST API assignment

# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example data model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory storage
items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

# Add your CRUD endpoints below
