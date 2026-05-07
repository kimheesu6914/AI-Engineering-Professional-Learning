import pandas as pd
import numpy as np

# A1 Goal 4: AI/ML Practice - Data Preprocessing
# Importance: Model performance depends on data quality, so logging the cleaning process is key.

data = {
    'User_ID': [1, 2, 3, 4, 5],
    'Input_Text': ['Hello', 'How are you?', None, 'Good morning', ' '],
    'Label': [1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

def clean_ai_data(df):
    # Handling Null values: Replace None with 'Unknown' to avoid model training errors.
    df['Input_Text'] = df['Input_Text'].fillna("Unknown")
    
    # Strip whitespace: Prevents tokenization issues in NLP.
    df['Input_Text'] = df['Input_Text'].str.strip()
    
    return df

# Run and check results
cleaned_df = clean_ai_data(df)
print(cleaned_df)

"""
[Reflection]
Through this practice, I've truly grasped the meaning of 'Garbage In, Garbage Out.' 
By manually cleaning the data, I realized that managing data sources and quality 
is a much bigger responsibility for an AI Engineer than just coding. 

In this context, I believe that Goal 1 (Indigenous Data Sovereignty) should also 
be considered an essential part of the data preprocessing stage to ensure 
the AI is developed ethically from the ground up.
"""
