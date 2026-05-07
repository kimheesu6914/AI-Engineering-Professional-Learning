import pandas as pd
import numpy as np

# A1 Goal 4: AI/ML Practice - Data Preprocessing
# Purpose: Practise basic data cleaning for AI model preparation.
# Importance: Model performance depends on data quality.

data = {
    'User_ID': [1, 2, 3, 4, 5],
    'Input_Text': ['Hello', 'How are you?', None, ' Good morning', ' '],
    'Label': [1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

def clean_ai_data(df):

    # Create a copy to avoid changing the original dataset directly.
    df = df.copy()

    # Replace missing values to reduce training errors.
    df['Input_Text'] = df['Input_Text'].fillna('Unknown')

    # Remove unnecessary whitespace.
    df['Input_Text'] = df['Input_Text'].str.strip()

    # Replace empty strings after stripping whitespace.
    df['Input_Text'] = df['Input_Text'].replace('', 'Unknown')

    # Remove duplicate rows if duplicates exist.
    df = df.drop_duplicates()

    return df

# Run cleaning process
cleaned_df = clean_ai_data(df)

# Display cleaned dataset
print("Cleaned Dataset:")
print(cleaned_df)

# Validate missing values
print("\nMissing Values:")
print(cleaned_df.isnull().sum())

# Check label distribution
print("\nLabel Distribution:")
print(cleaned_df['Label'].value_counts())

"""
[Reflection]

Through this practice, I developed a deeper understanding of the
'Garbage In, Garbage Out' principle in AI development.

By manually cleaning the dataset, I realised that data preprocessing
is not a minor step, but an important responsibility that directly
affects model quality and reliability.

This activity also helped me understand the importance of professional
accountability in AI workflows. While this practice used a simplified
sample dataset, it reminded me that ethical principles such as
Indigenous Data Sovereignty and responsible data governance should be
considered when working with Indigenous or culturally sensitive data.

Using GitHub to document this learning process also strengthened my
understanding of professional workflows, version control, and reflective
practice as a future AI Engineer.
"""
