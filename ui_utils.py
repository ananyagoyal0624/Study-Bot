import streamlit as st

def transform(input_list):
    new_list = []
    for item in input_list:
        print("DEBUG: Current item ->", item)  # Debugging ke liye
        for key in item:
            if 'question1' in key or 'question2' in key or 'question3' in key:
                question_num = key[-1]  # Last character extract kar rahe ho
                
                # Check karo ki required keys exist karti hain ya nahi
                required_keys = [f'A_{question_num}', f'B_{question_num}', f'C_{question_num}', f'D_{question_num}', f'reponse{question_num}']
                missing_keys = [k for k in required_keys if k not in item]
                
                if missing_keys:
                    print(f"⚠ Warning: Missing keys in item -> {missing_keys}")
                    continue  # Skip kar do agar keys nahi mil rahi

                question_dict = {
                    'question': item[key],
                    'A': item[f'A_{question_num}'],
                    'B': item[f'B_{question_num}'],
                    'C': item[f'C_{question_num}'],
                    'D': item[f'D_{question_num}'],
                    'reponse': item[f'reponse{question_num}']
                }
                new_list.append(question_dict)
    return new_list
