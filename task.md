
Typesafe Apples to Apples Scoring Takehome

Greeting, aspiring Data Demon!

At Typesafe we need to create synthetic data to help our models learn to perform a variety of tasks. That’s one of the main jobs of a Data Demon.

Sometimes we need to create data for scoring. Scoring is taking some input, and a number of possible scores along with guidelines for those possible scores, and outputting a score for that input using those guidelines.

For this task, we’re going to be developing scoring guidelines for… APPLES TO APPLES! 

If you’ve never played apples to apples that’s OK. The important info is that Apples to Apples has green cards that are typically adjectives, and red cards that are typically nouns. 

We’d like to create detailed scoring rubrics that will allow us to train our models to follow precise scoring criteria effectively.

Scoring rubric


A scoring rubric is a set of overall instructions, and a map of integer grades to strings describing the criteria that needs to be matched to meet that grade.

In the case of apples to apples, a scoring rubric for the green card “Bitter” might look like:


{“overall_instructions”: “””Classification Rules:
Consider both literal (taste) and figurative (emotional) bitterness
Rate based on the most common or typical experience
For events/experiences, consider the typical emotional impact
For foods/drinks, prioritize taste unless there's a stronger emotional connection
Consider cultural/contextual associations with bitterness”””,
  “criteria”: { 
	5: “””Intensely Bitter (Perfect Match). Must embody bitterness either literally (Strong bitter taste/flavor as defining characteristic), emotionally (Deep resentment, spite, or emotional pain) or experientially (Harsh negative outcomes or experiences). Bitterness must be the primary/defining quality. Examples: Divorce, Defeat, Strong Coffee, Dark Chocolate”””
4: ”Substantially Bitter. Notable bitterness but not defining characteristic. Significant negative experiences/outcomes. Mixed experiences where bitterness predominates. Regular association with bitter feelings/tastes. Examples: Failed Relationships, Job Loss, Some Medicines”
3: ”Moderately Bitter. Some bitter elements mixed with other qualities. Situations that can lead to bitter feelings. Experiences that may turn bitter. Items with bitter notes but not predominantly bitter. Examples: Competition, Criticism, Green Tea”
2: “Slightly Bitter. Minor or occasional bitter elements. Potential for some negative feelings. Mild disappointments or setbacks. Subtle bitter taste components. Examples: Minor Losses, Some Vegetables, Light Competition”
1: “Not Bitter. No bitter taste components. Positive or neutral experiences. Pleasant or sweet characteristics. No association with negative feelings. Examples: Pure Joy, Sweet Foods, Simple Pleasures”
  }
}


 Your task

We want to create data that will help us train our models to follow grading instructions precisely. For this dataset, we want very precise and clear instructions. We also want different versions of instructions (maybe with small precise changes between them) such that the same items are scored differently – this allows us to train models to precisely follow instructions when the desired answer changes with slight changes in grading criteria.


Instructions: 
For each of the green cards on the list here: (e.g Addictive)

Choose a random sample of thirty red cards from the list here (a different set of red cards per green card). (e.g. Bakery)

Make two sets of grading criteria (g1, g2) for grading red cards for fit with the chosen green card, along with corresponding grades for each red card, such that:
There are five levels of each grade, 1-5. The criteria make sense as a valid interpretation of choosing how to grade the red card for how much the green card applies (E.g how “Addictive” this red card is)
The grades assigned to the 30 red cards are roughly evenly distributed among the grade levels, with at least one in each level.
If a random person were to regrade each red card with your criteria, they’d agree with the grade you gave as often as possible. (This means have your criteria be as specific as possible and make sure your grades match!)
The correlation between the grades assigned to the red cards by g1 and g2 is as low as possible.
The criteria aren’t overly specific to the 30 random cards chosen. For example, the criteria shouldn’t include any of them verbatim as examples. However, they should be tailored to make sure there are clauses that allow these cards to be clearly classified.


Write a program to generate a list of all green cards, the criteria associated with them, and the red cards with their associated scores.
Also write a program to read in the list, and provide some basic summary statistics measuring the distributions of grades and the relative disagreements between grading criteria for the same green card.

Return to us the generated list in whatever format you’ve saved it in, and the code you used to generate the list.

 Also provide a brief writeup of the approach you took.


Project constraints

The way we think you’ll likely go about this is generating a set of creative chained queries for an existing LLM. We’re providing an anthropic API key with $25 worth of credit on it for you to use for this purpose. 

Anthropic api key (currently has a query per minute limit of 50 which is kind of slow, if it takes too long to generate all this data let us know)

(if you use anthropic you might want to use XML tags: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)

api-key-not-here

We think this should take ~4 hours (but we aren’t sure). Don’t spend too much more time on it. However much you get done is OK.

You’ll be evaluated partially on code quality and partially on considerations of data quality for the data you generate.

Good luck!
