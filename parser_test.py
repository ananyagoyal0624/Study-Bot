import re
from langchain.output_parsers.regex import RegexParser

def transform(input_list):
    new_list = []
    for item in input_list:  # Ensure item is a dictionary
        question_dict = {
            "question": item.get("question", ""),
            "A": item.get("A", ""),
            "B": item.get("B", ""),
            "C": item.get("C", ""),
            "D": item.get("D", ""),
            "response": item.get("response", ""),
        }
        new_list.append(question_dict)
    return new_list

# Corrected Regex
regex_pattern = r"Question:\s*(.*?)\s*CHOICE_A:\s*(.*?)\s*CHOICE_B:\s*(.*?)\s*CHOICE_C:\s*(.*?)\s*CHOICE_D:\s*(.*?)\s*Answer:\s*(\w)"

output_parser = RegexParser(
    regex=regex_pattern,
    output_keys=["question", "A", "B", "C", "D", "response"]
)

# Input String
input_string = """Question: What is the main contribution of the paper?
CHOICE_A: Introducing a hybrid architecture combining deep learning layers with a final discrete NP-hard Graphical Model reasoning layer
CHOICE_B: Proposing a new loss function that efficiently deals with logical information
CHOICE_C: Using discrete GMs as the reasoning language
CHOICE_D: All of the above
Answer: D

Question: What type of problems can the proposed neural architecture and loss function efficiently learn to solve?
CHOICE_A: Only visual problems
CHOICE_B: Only symbolic problems
CHOICE_C: Only energy optimization problems
CHOICE_D: NP-hard reasoning problems expressed as discrete Graphical Models, including symbolic, visual, and energy optimization problems
Answer: D
"""

# Parse Input
parsed_output = output_parser.parse(input_string)

# Transform Parsed Data
output_dict = transform(parsed_output)

# Print Output
print(output_dict)
