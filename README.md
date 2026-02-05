# Valentine's Day Invitation 💕

A beautiful, interactive Valentine's Day invitation web application built with **Python (FastAPI)** and dynamically generated JavaScript.

## Features

- ✨ Animated floating hearts background
- 🎉 Confetti celebration when "Yes" is clicked
- 😄 Interactive "No" button that moves around
- 💖 Beautiful gradient design with animations
- 📱 Responsive design for mobile and desktop
- 🐍 **JavaScript logic written in Python** - The app logic is now in Python and generates JavaScript dynamically

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Option 1: Using the run script
```bash
python run.py
```

### Option 2: Using Uvicorn directly
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Option 3: Using Python module
```bash
python -m uvicorn main:app --reload
```

The application will be available at: **http://127.0.0.1:8000**

## Project Structure

```
date/
├── main.py              # FastAPI application (serves HTML and generates JS)
├── app_logic.py         # Python module with application logic
├── script_generator.py  # Generates JavaScript from Python logic
├── run.py               # Simple run script
├── requirements.txt     # Python dependencies
├── index.html           # Main HTML page
├── public/
│   ├── style.css        # Stylesheet
│   └── script.js        # Original JS (backup, now served dynamically from Python)
└── README.md            # This file
```

## API Endpoints

- `GET /` - Main page (serves index.html)
- `GET /public/script.js` - Dynamically generated JavaScript from Python
- `GET /public/style.css` - Static CSS file
- `GET /health` - Health check endpoint

## Development

The application runs with auto-reload enabled by default, so any changes to Python files will automatically restart the server.

For frontend changes (HTML/CSS/JS), you may need to hard refresh your browser (Ctrl+F5 or Cmd+Shift+R) to see changes.

## Technologies Used

- **Python** - Backend logic and JavaScript generation
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **JavaScript** - Client-side interactivity (generated from Python)
- **CSS3** - Animations and styling

## How It Works

The application logic is written in Python (`app_logic.py`), which contains:
- No button messages configuration
- Confetti colors
- Floating hearts generation logic
- Button scaling logic

The `script_generator.py` module converts this Python logic into JavaScript code that runs in the browser. The FastAPI server dynamically generates and serves the JavaScript when `/public/script.js` is requested.

This approach allows you to:
- Write application logic in Python
- Maintain type safety and Python's rich ecosystem
- Still have interactive client-side behavior
- Easily modify logic in Python without touching JavaScript directly
