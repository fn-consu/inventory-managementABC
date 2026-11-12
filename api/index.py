"""Vercel serverless entrypoint.

Exposes the FastAPI app from server/main.py so Vercel's Python runtime can serve it.
Local development is unchanged: run `uv run python main.py` from the server directory.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "server"))

from main import app  # noqa: E402,F401
