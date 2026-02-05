"""
Python module that generates JavaScript code dynamically.
This converts the Python logic into executable JavaScript.
"""
from app_logic import app_logic
import json


def generate_javascript() -> str:
    """Generate the JavaScript code from Python logic."""
    
    # Get configuration from Python
    hearts_config = app_logic.generate_floating_heart_config()
    no_messages = json.dumps(app_logic.no_messages)
    confetti_colors = json.dumps(app_logic.confetti_colors)
    
    js_code = f"""
// This JavaScript is generated from Python (app_logic.py)
const questionCard = document.getElementById("question-card");
const successCard = document.getElementById("success-card");
const yesBtn = document.getElementById("yes-btn");
const noBtn = document.getElementById("no-btn");
const buttonsContainer = document.getElementById("buttons-container");
const hintText = document.getElementById("hint-text");
const floatingHeartsContainer = document.getElementById("floating-hearts");
const confettiContainer = document.getElementById("confetti-container");

// State (initialized from Python)
let noClickCount = 0;
let yesButtonScale = 1;

// No button messages (from Python)
const noMessages = {no_messages};

// Confetti colors (from Python)
const confettiColors = {confetti_colors};

// Create floating hearts background
function createFloatingHearts() {{
  const heartsConfig = {json.dumps(hearts_config)};
  
  heartsConfig.forEach((config, i) => {{
    const heart = document.createElement("div");
    heart.className = "background-heart";
    heart.textContent = "❤️";
    heart.style.left = `${{config.left}}%`;
    heart.style.animationDelay = `${{config.animation_delay}}s`;
    heart.style.animationDuration = `${{config.animation_duration}}s`;
    heart.style.fontSize = `${{config.font_size}}px`;
    floatingHeartsContainer.appendChild(heart);
  }});
}}

// Create confetti
function createConfetti() {{
  for (let i = 0; i < 100; i++) {{
    const confetti = document.createElement("div");
    confetti.className = "confetti-piece";
    confetti.style.left = `${{Math.random() * 100}}%`;
    confetti.style.backgroundColor = confettiColors[Math.floor(Math.random() * confettiColors.length)];
    confetti.style.animationDelay = `${{Math.random() * 2}}s`;
    confetti.style.transform = `rotate(${{Math.random() * 360}}deg)`;
    confettiContainer.appendChild(confetti);
  }}
}}

// Move the No button
function moveNoButton() {{
  // Use the entire card as the boundary for more freedom
  const cardRect = questionCard.getBoundingClientRect();
  const containerRect = buttonsContainer.getBoundingClientRect();
  const btnRect = noBtn.getBoundingClientRect();

  // Calculate the offset of buttons-container within the card
  const containerOffsetX = containerRect.left - cardRect.left;
  const containerOffsetY = containerRect.top - cardRect.top;

  // Calculate positions relative to the card
  // The button can move anywhere within the card boundaries
  const maxX = cardRect.width - btnRect.width;
  const maxY = cardRect.height - btnRect.height;

  // Generate random position within the entire card
  const newX = Math.random() * maxX;
  const newY = Math.random() * maxY;

  // Apply escaping class and position
  // Position relative to buttons-container, but calculate to stay within card bounds
  noBtn.classList.add("escaping");
  noBtn.style.position = "absolute";
  noBtn.style.left = `${{newX - containerOffsetX}}px`;
  noBtn.style.top = `${{newY - containerOffsetY}}px`;

  // Update message (cycle through messages continuously)
  noClickCount = (noClickCount + 1) % noMessages.length;
  noBtn.textContent = noMessages[noClickCount];

  // Make Yes button bigger (increase font size and padding instead of transform,
  // so it doesn't conflict with existing CSS animations on the button)
  yesButtonScale = Math.min(yesButtonScale + 0.15, 2);
  const baseFontSizeRem = 1.25; // matches .btn-yes font-size in CSS
  const basePaddingYRem = 1; // matches .btn-yes padding in CSS (vertical)
  const basePaddingXRem = 3; // matches .btn-yes padding in CSS (horizontal)
  yesBtn.style.fontSize = `${{baseFontSizeRem * yesButtonScale}}rem`;
  yesBtn.style.padding = `${{basePaddingYRem * yesButtonScale}}rem ${{basePaddingXRem * yesButtonScale}}rem`;
}}

// Handle Yes click
function handleYesClick() {{
  questionCard.style.display = "none";
  successCard.style.display = "block";
  createConfetti();
}}

// Event Listeners
yesBtn.addEventListener("click", handleYesClick);
noBtn.addEventListener("mouseenter", moveNoButton);
noBtn.addEventListener("click", moveNoButton);

// Initialize
createFloatingHearts();
"""
    return js_code.strip()
