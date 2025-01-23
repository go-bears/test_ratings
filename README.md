# Apples to Apples Scoring System

This project implements a scoring system for the Apples to Apples card game using the Anthropic Claude API to generate scoring rubrics and evaluate cards.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. The Anthropic API key is already configured in the Config class.

## Project Structure

- `apples_to_apples.py`: Main script containing all core functionality
- `requirements.txt`: Python dependencies
- `results.json`: Generated scoring data (created after running)
- `analysis.json`: Analysis of scoring results (created after running)

## Components

1. **AnthropicClient**: Handles API interactions with rate limiting
2. **RubricGenerator**: Creates scoring rubrics for green cards
3. **CardScorer**: Scores red cards according to rubrics
4. **DataAnalyzer**: Analyzes scoring data and generates statistics

## Usage

Run the main script:
```bash
python apples_to_apples.py
```

## TODO

1. Implement rubric generation logic in `RubricGenerator`
2. Implement scoring logic in `CardScorer`
3. Implement analysis logic in `DataAnalyzer`
4. Add comprehensive list of green and red cards
5. Add error handling and retry logic for API calls 