import cohere
import anthropic
import os
from dotenv import load_dotenv
import dspy
load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

cohere_client = cohere.Client(COHERE_API_KEY)
anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


lm = dspy.LM('anthropic/claude-3-opus-20240229', api_key='YOUR_ANTHROPIC_API_KEY')
dspy.configure(lm=lm)