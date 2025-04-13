from fastapi import FastAPI
import sys
import os

# Add the app directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app", "api")))

# Import the FastAPI app from the main.py file
from main import app

# Export the app for Vercel
handler = app 