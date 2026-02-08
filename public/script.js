const questionCard = document.getElementById("question-card");
const successCard = document.getElementById("success-card");
const yesBtn = document.getElementById("yes-btn");
const noBtn = document.getElementById("no-btn");
const buttonsContainer = document.getElementById("buttons-container");
const hintText = document.getElementById("hint-text");
const floatingHeartsContainer = document.getElementById("floating-hearts");
const confettiContainer = document.getElementById("confetti-container");
const noFloatingMessagesContainer = document.getElementById("no-floating-messages");

// State
let noClickCount = 0;
let yesButtonScale = 1;
let noButtonScale = 1;

// No button messages
const noMessages = [
  //"No",
  "Are you sure?",
  "Really sure?",
  "Think again!",
  "Last chance!",
  "You can't escape love!",
  "Nope, try again!",
  "I'm not giving up!",
  "Come on! 💕",
  "Please, 😘",
];

// Create floating hearts background
function createFloatingHearts() {
  for (let i = 0; i < 20; i++) {
    const heart = document.createElement("div");
    heart.className = "background-heart";
    heart.textContent = "❤️";
    heart.style.left = `${Math.random() * 100}%`;
    heart.style.animationDelay = `${Math.random() * 5}s`;
    heart.style.animationDuration = `${6 + Math.random() * 4}s`;
    heart.style.fontSize = `${12 + Math.random() * 24}px`;
    floatingHeartsContainer.appendChild(heart);
  }
}

// Create confetti
function createConfetti() {
  const colors = [
    "hsl(350, 80%, 55%)",
    "hsl(340, 70%, 60%)",
    "hsl(20, 100%, 70%)",
    "hsl(350, 100%, 88%)",
    "hsl(0, 0%, 100%)",
  ];

  for (let i = 0; i < 100; i++) {
    const confetti = document.createElement("div");
    confetti.className = "confetti-piece";
    confetti.style.left = `${Math.random() * 100}%`;
    confetti.style.backgroundColor =
      colors[Math.floor(Math.random() * colors.length)];
    confetti.style.animationDelay = `${Math.random() * 2}s`;
    confetti.style.transform = `rotate(${Math.random() * 360}deg)`;
    confettiContainer.appendChild(confetti);
  }
}

// Create floating message at old position (balloon style: floats up for 2s then disappears)
function createFloatingNoMessage(messageText, leftPx, topPx) {
  if (!noFloatingMessagesContainer) return;
  const el = document.createElement("div");
  el.className = "no-floating-message";
  el.textContent = messageText;
  el.style.left = `${leftPx}px`;
  el.style.top = `${topPx}px`;
  noFloatingMessagesContainer.appendChild(el);
  // Remove after 2 seconds (animation ends)
  setTimeout(() => {
    el.remove();
  }, 2000);
}

// Move the No button
function moveNoButton() {
  // Use the entire card as the boundary for more freedom
  const cardRect = questionCard.getBoundingClientRect();
  const containerRect = buttonsContainer.getBoundingClientRect();
  const btnRect = noBtn.getBoundingClientRect();

  // Old position relative to buttons-container (for floating message)
  const oldLeft = btnRect.left - containerRect.left;
  const oldTop = btnRect.top - containerRect.top;

  // Get current message and show it at OLD position (balloon floats up, then disappears)
  const messageToShow = noMessages[noClickCount];
  createFloatingNoMessage(messageToShow, oldLeft, oldTop);

  // Cycle to next message for next time (comment: message no longer on button)
  noClickCount = (noClickCount + 1) % noMessages.length;

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
  noBtn.style.left = `${newX - containerOffsetX}px`;
  noBtn.style.top = `${newY - containerOffsetY}px`;

  // No button text stays "No" (old: noBtn.textContent = noMessages[noClickCount];)
  noBtn.textContent = "No 🥺";

  // Make Yes button bigger (increase font size and padding instead of transform,
  // so it doesn't conflict with existing CSS animations on the button)
  yesButtonScale = Math.min(yesButtonScale + 0.15, 2.5);
  const baseFontSizeRem = 1.25; // matches .btn-yes font-size in CSS
  const basePaddingYRem = 1; // matches .btn-yes padding in CSS (vertical)
  const basePaddingXRem = 3; // matches .btn-yes padding in CSS (horizontal)
  yesBtn.style.fontSize = `${baseFontSizeRem * yesButtonScale}rem`;
  yesBtn.style.padding = `${basePaddingYRem * yesButtonScale}rem ${
    basePaddingXRem * yesButtonScale
  }rem`;

  //make no button smaller
  noButtonScale = Math.max(noButtonScale - 0.05, 0.55);
  // const baseFontSizeRem = 1.25; // matches .btn-yes font-size in CSS
  // const basePaddingYRem = 1; // matches .btn-yes padding in CSS (vertical)
  // const basePaddingXRem = 3; // matches .btn-yes padding in CSS (horizontal)
  noBtn.style.fontSize = `${baseFontSizeRem * noButtonScale}rem`;
  noBtn.style.padding = `${basePaddingYRem * noButtonScale}rem ${
    basePaddingXRem * noButtonScale
  }rem`;

  // Show hint after first escape
  // if (noClickCount > 0) {
  //   hintText.textContent = "Hint: The Yes button is getting bigger... 😉";
  // }
}

// Handle Yes click
function handleYesClick() {
  questionCard.style.display = "none";
  successCard.style.display = "block";
  createConfetti();
}

// Event Listeners
yesBtn.addEventListener("click", handleYesClick);
noBtn.addEventListener("mouseenter", moveNoButton);
noBtn.addEventListener("click", moveNoButton);

// Initialize
createFloatingHearts();
