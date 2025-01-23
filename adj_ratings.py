import pandas as pd
import os
import anthropic
from tqdm import tqdm

from dotenv import load_dotenv

from prompts import build_grading_prompt1

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


def get_adj_prompts(adj: str):

    prompt = build_grading_prompt1(adj)
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        tools=[
            {
                "name": "adj_rubric",
                "description": "Prints extract named entities.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "entities": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "green_card_adj": {"type": "string", "description": adj},
                                    "criteria": {"type": "string", "description": prompt},
                                    "synonyms_and_examples": {"type": "string", "description": "examples of the adjective at each level"}
                                    ,
                                },
                                "required": ["green_card_adj", "synonyms_and_examples"]
                            }
                        }
                    },
                    "required": ["entities"]
                }       
            }, 
        ],
        messages=[{"role": "user", "content": prompt}]
    )
    for content in response.content:
        if content.type == "tool_use" and content.name == "adj_rubric":
            data_dict = content.input["entities"][0]
            print(data_dict)
            return data_dict


def main():
    responses = []
    adjs = pd.read_csv("adjs.csv")["adj"].tolist()[:100]
    print(len(adjs))

    for adj in tqdm(adjs):
        response = get_adj_prompts(adj)
        responses.append(response)


    responses_df = pd.DataFrame(responses)
    print(responses_df.head())
    responses_df.to_csv("adj_rubrics.csv", index=False)

if __name__ == "__main__":
    main()  