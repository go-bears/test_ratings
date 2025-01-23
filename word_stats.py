import statistics
import pandas as pd

from cards import get_red_cards
from prompts import grading_prompt_2

from dotenv import load_dotenv
import os

load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

import anthropic
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


nouns = [word.lower() for word in get_red_cards()]
print(nouns)

responses = []

def get_noun_rating(noun: str):
    prompt = grading_prompt_2(noun)
    print(prompt)
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        tools=[
            {
                "name": "noun_rating",
                "description": "Prints extract named entities.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "entities": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "red_card_noun": {"type": "string", "description": noun},
                                    "rating": {"type": "string", "description": "noun type score"},
                                    "context": {"type": "string", "description": "reasoning for classification"},
                                },
                                "required": ["red_card_noun", "rating", "context"]
                            }
                        }
                    },
                    "required": ["entities"]
                }
            }
        ],
        messages=[{"role": "user", "content": prompt}]
    )
    for content in response.content:
        if content.type == "tool_use" and content.name == "noun_rating":
            data_dict = content.input["entities"][0]
            print(data_dict)
            return data_dict


def main():
    for noun in sorted(nouns):
        response = get_noun_rating(noun)
        responses.append(response)


    responses_df = pd.DataFrame(responses)
    print(responses_df.head())
    responses_df.to_csv("noun_ratings.csv", index=False)

if __name__ == "__main__":
    main()  
    # df = pd.read_csv("noun_ratings.csv")
    # print(df.iloc[0][1])
    # print(df.iloc[0])