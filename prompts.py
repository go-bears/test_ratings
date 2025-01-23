def build_grading_prompt1(adj: str = "addictive"):
    """prompt builder for grading criteria for intensity of an adjective"""

    instructions = f"""Generate at least three appropriate synonyms for {adj} at each of the following levels of intensity levels. 
   Add synonyms and examples for {adj} at the specific intensity level.

    Rating Criteria:
    """
    criteria = {
        5: {"description": "Extreme/Intense: This level represents the most extreme or intense form of the adjective. It is the pinnacle of the characteristic, where its impact or presence is overwhelming and defining. Examples include:",
        "examples": ["Intense bitterness: A taste so bitter it's almost unbearable, like strong, unfiltered coffee.",
        "Extreme joy: An overwhelming sense of happiness and elation, leaving one spee]chless."
        "Intense pain: A level of physical or emotional pain that is excruciating and all-encompassing."],
        "synonyms and examples": {"level": 5, "synonyms": [], "examples": []},
        },
        4: {"description": "Substantial/Significant: Here, the adjective is a notable and significant presence, but it may not be the sole defining factor. It has a strong impact and is a major component of the experience or description. Examples:",
        "examples": ["Substantial bitterness: A taste or experience with a strong bitter element, but balanced with other flavors or emotions.",
        "Significant beauty: A sight or person with remarkable aesthetics, leaving a lasting impression.",
        "Significant challenge: A task or obstacle that is difficult and demanding, requiring great effort."],
        "synonyms and examples": {"level": 4, "synonyms": [], "examples": []},
        },
        3: {"description": "Moderate/Noticeable: At this level, the adjective is a noticeable and distinct feature, but it is not the dominant force. It adds character and depth, but other elements are also present and influential. Examples:",
        "examples": ["Moderate bitterness: A hint of bitterness that adds complexity, like a hint of lemon zest in a dessert.",
        "Noticeable courage: A display of bravery that stands out, but is not the sole focus of the story."],
        "synonyms and examples": {"level": 3, "synonyms": [], "examples": []},
        },
        2: {"description": "Slight/Mild: Here, the adjective is a subtle and minor element, often easily overlooked. It adds a hint of the characteristic, but it is not a defining quality. Examples:",
        "examples": ["Slight bitterness: A barely perceptible bitter taste, like a hint of bitterness in a mild tea.",
        "Mild curiosity: A subtle interest or intrigue, not a burning desire."],
        "synonyms and examples": {"level": 2, "synonyms": [], "examples": []},
        },
        1: {"description": "None/Neutral: This level represents the absence or neutrality of the adjective. There is no trace of the characteristic, and other elements are more prominent or influential. Examples:",
        "examples": ["None/Neutral bitterness: A taste or experience with absolutely no bitter notes, like a sweet dessert.",
        "Neutral emotion: A state of mind with no strong feelings, a calm and balanced emotional state."],
        "synonyms and examples": {"level": 1, "synonyms": [], "examples": []},
        }
    }

    return instructions + str(criteria)



def grading_prompt_2(noun: str = "bakery"):
    """prompt for noun with tangible features"""

    quality = "Tangibility"
    instructions = f"""
    Classification Rules:
    Use the following criteria to classify the noun: {noun}.
    if the noun is a compound noun phrase, classify the entire phrase, and not the individual components.
    Apply standard and most common meanings of the noun.


    Rating Criteria:
    """

    criteria = {
        0: "Brand Names, titles, proper nouns, place or planet names",
        1: "Abstract Nouns (e.g., love, idea, legal terms)",
        2: "Common nouns with Limited {quality} (e.g., thought, feeling, sleep)",
        3: "Common nouns with Some {quality} and some ability to measure a feature (e.g., music, sunlight, water)",
        4: "Common Nouns with Strong {quality} and some countability  (e.g., table, apple)",
        5: "High {quality} and countable Common Nouns (e.g., rock, chair)"
    }

    return instructions + str(criteria)

def overall_instructions(adj: str = "bitter"):
    """overall instructions for the prompt"""
    return {
        "overall_instructions": """Classification Rules:
        Consider both literal and figurative meanings of {adj}
        Base rating on the most common or typical experience
        For events/experiences, consider the typical emotional impact
        For foods/drinks, prioritize taste unless there's a stronger emotional connection
        Consider cultural/contextual associations with {adj}
"""
    }
