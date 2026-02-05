"""
FastAPI application for Valentine's Day invitation.
Uses app_logic.py directly via API endpoints - no JavaScript generation needed.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from app_logic import app_logic
from typing import Dict, List

app = FastAPI(
    title="Valentine's Day Invitation",
    description="A special Valentine's Day invitation web app",
    version="1.0.0"
)

# Enable CORS for API endpoints
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    """Serve the main HTML page."""
    html_file = Path(__file__).parent / "index.html"
    return FileResponse(html_file)


@app.get("/api/config")
async def get_config() -> Dict:
    """
    Get application configuration directly from app_logic.py.
    This is the Python source of truth - no JavaScript generation needed.
    """
    return {
        "no_messages": app_logic.no_messages,
        "confetti_colors": app_logic.confetti_colors,
        "num_floating_hearts": app_logic.num_floating_hearts,
        "num_confetti_pieces": app_logic.num_confetti_pieces,
    }


@app.get("/api/hearts")
async def get_hearts_config() -> List[Dict]:
    """
    Get floating hearts configuration generated directly from app_logic.py.
    """
    return app_logic.generate_floating_heart_config()


@app.get("/api/confetti")
async def get_confetti_config() -> List[Dict]:
    """
    Get confetti configuration generated directly from app_logic.py.
    """
    return app_logic.generate_confetti_config()


@app.get("/api/no-message")
async def get_no_message() -> Dict[str, str]:
    """
    Get the next 'No' button message directly from app_logic.py.
    """
    message = app_logic.get_no_message()
    return {"message": message}


@app.get("/api/yes-scale")
async def get_yes_scale() -> Dict[str, float]:
    """
    Increment and get the Yes button scale directly from app_logic.py.
    """
    scale = app_logic.increment_yes_button_scale()
    return {"scale": scale}


@app.post("/api/reset")
async def reset_state():
    """
    Reset the application state in app_logic.py.
    """
    app_logic.reset()
    return {"status": "reset", "message": "Application state reset"}


# Mount static files directory (CSS and JavaScript - JavaScript uses API endpoints)
static_dir = Path(__file__).parent / "public"
if static_dir.exists():
    app.mount("/public", StaticFiles(directory=str(static_dir)), name="public")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Valentine's Day app is running!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
