import os
import json
import random
from typing import List, Dict, Tuple
import anthropic
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from scipy import stats
from tqdm import tqdm

class Config:
    """Configuration settings for the application"""
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    RATE_LIMIT = 50  # API calls per minute
    MIN_CARDS_PER_GRADE = 1  # Minimum cards required for each grade level
    NUM_RED_CARDS_PER_GREEN = 3  # Number of red cards to sample for each green card

class AnthropicClient:
    """Handles interactions with the Anthropic API"""
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=Config.ANTHROPIC_API_KEY,
            base_url="https://api.anthropic.com",
        )
        
    def generate_response(self, prompt: str) -> str:
        """Generate a response from Claude with rate limiting"""
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            print(f"Error in API call: {e}")
            return None

class RubricGenerator:
    """Generates scoring rubrics for green cards"""
    def __init__(self, anthropic_client: AnthropicClient):
        self.client = anthropic_client
        
    def generate_rubrics(self, green_card: str) -> Tuple[Dict, Dict]:
        """Generate two different scoring rubrics for a green card"""
        
          criteria = {
              5: f"""Intensely {green_card} (Perfect Match). Must embody {green_card.lower()}ness either literally 
(Strong {green_card.lower()} taste/flavor as defining characteristic), emotionally (Deep resentment, 
spite, or emotional pain) or experientially (Harsh negative outcomes or experiences). {green_card}ness 
must be the primary/defining quality. Examples: Divorce, Defeat, Strong Coffee, Dark Chocolate""",
              4: f"""Substantially {green_card}. Notable {green_card.lower()}ness but not defining characteristic. 
Significant negative experiences/outcomes. Mixed experiences where {green_card.lower()}ness predominates. 
Regular association with {green_card.lower()} feelings/tastes. Examples: Failed Relationships, Job Loss, 
Some Medicines""",
              3: f"""Moderately {green_card}. Some {green_card.lower()} elements mixed with other qualities. 
Situations that can lead to {green_card.lower()} feelings. Experiences that may turn {green_card.lower()}. 
Items with {green_card.lower()} notes but not predominantly {green_card.lower()}. Examples: Competition, 
Criticism, Green Tea""",
              2: f"""Slightly {green_card}. Minor or occasional {green_card.lower()} elements. Potential for some 
negative feelings. Mild disappointments or setbacks. Subtle {green_card.lower()} taste components. 
Examples: Minor Losses, Some Vegetables, Light Competition""",
              1: f"""Not {green_card}. No {green_card.lower()} taste components. Positive or neutral experiences. 
Pleasant or sweet characteristics. No association with negative feelings. Examples: Pure Joy, Sweet Foods, 
Simple Pleasures"""
          }
        return criteria

class CardScorer:
    """Scores red cards according to rubrics"""
    def __init__(self, anthropic_client: AnthropicClient):
        self.client = anthropic_client
        
    def score_cards(self, green_card: str, red_cards: List[str], rubric: Dict) -> Dict[str, int]:
        """Score a list of red cards using the provided rubric"""
        # TODO: Implement scoring logic
        pass

class DataAnalyzer:
    """Analyzes scoring data and generates statistics"""
    def analyze_scores(self, scores_data: Dict) -> Dict:
        """Generate summary statistics for the scoring data"""
        # TODO: Implement analysis logic
        pass
        
    def calculate_correlation(self, scores1: List[int], scores2: List[int]) -> float:
        """Calculate correlation between two sets of scores"""
        return stats.pearsonr(scores1, scores2)[0]

def main():
    # Initialize components
    anthropic_client = AnthropicClient()
    rubric_generator = RubricGenerator(anthropic_client)
    card_scorer = CardScorer(anthropic_client)
    analyzer = DataAnalyzer()
    
    # Sample data (TODO: Replace with actual data)
    green_cards = ["Addictive", "Bitter", "Crazy"]  # Add more green cards
    red_cards = ["Bakery", "Coffee", "Chocolate"]   # Add more red cards
    
    results = {}
    
    for green_card in tqdm(green_cards, desc="Processing green cards"):
        # Sample red cards
        sampled_red_cards = random.sample(red_cards, Config.NUM_RED_CARDS_PER_GREEN)
        
        # Generate rubrics
        rubric1, rubric2 = rubric_generator.generate_rubrics(green_card)
        
        # Score cards
        scores1 = card_scorer.score_cards(green_card, sampled_red_cards, rubric1)
        scores2 = card_scorer.score_cards(green_card, sampled_red_cards, rubric2)
        
        # Store results
        results[green_card] = {
            "rubric1": rubric1,
            "rubric2": rubric2,
            "scores1": scores1,
            "scores2": scores2,
            "red_cards": sampled_red_cards
        }
    
    # Analyze results
    analysis = analyzer.analyze_scores(results)
    
    # Save results
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    # Save analysis
    with open("analysis.json", "w") as f:
        json.dump(analysis, f, indent=2)

if __name__ == "__main__":
    main() 