"""
Python module containing the application logic for the Valentine's Day invitation.
This module contains the business logic that was previously in JavaScript.
"""
import random
from typing import List


class ValentineAppLogic:
    """Contains the core logic for the Valentine's Day invitation app."""
    
    def __init__(self):
        self.no_click_count = 0
        self.yes_button_scale = 1.0
        
        # No button messages
        self.no_messages = [
            "No",
            "Are you sure?",
            "Really sure?",
            "Think again!",
            "Last chance!",
            "You can't escape love!",
            "Nope, try again!",
            "I'm not giving up!",
            "Come on! 💕",
            "Please? 🥺",
        ]
        
        # Confetti colors
        self.confetti_colors = [
            "hsl(350, 80%, 55%)",
            "hsl(340, 70%, 60%)",
            "hsl(20, 100%, 70%)",
            "hsl(350, 100%, 88%)",
            "hsl(0, 0%, 100%)",
        ]
        
        self.num_floating_hearts = 20
        self.num_confetti_pieces = 100
    
    def get_no_message(self) -> str:
        """Get the next 'No' button message."""
        self.no_click_count = (self.no_click_count + 1) % len(self.no_messages)
        return self.no_messages[self.no_click_count]
    
    def increment_yes_button_scale(self) -> float:
        """Increment the Yes button scale and return the new value."""
        self.yes_button_scale = min(self.yes_button_scale + 0.15, 2.0)
        return self.yes_button_scale
    
    def generate_floating_heart_config(self) -> List[dict]:
        """Generate configuration for floating hearts."""
        hearts = []
        for i in range(self.num_floating_hearts):
            hearts.append({
                'left': random.random() * 100,
                'animation_delay': random.random() * 5,
                'animation_duration': 6 + random.random() * 4,
                'font_size': 12 + random.random() * 24,
            })
        return hearts
    
    def generate_confetti_config(self) -> List[dict]:
        """Generate configuration for confetti pieces."""
        confetti = []
        for i in range(self.num_confetti_pieces):
            confetti.append({
                'left': random.random() * 100,
                'color': random.choice(self.confetti_colors),
                'animation_delay': random.random() * 2,
                'rotation': random.random() * 360,
            })
        return confetti
    
    def reset(self):
        """Reset the application state."""
        self.no_click_count = 0
        self.yes_button_scale = 1.0


# Create a singleton instance
app_logic = ValentineAppLogic()
