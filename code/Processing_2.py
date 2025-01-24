import pandas as pd
import re

# Function to standardize strings and apply transformations
def standardize_strings(df):
    for column in df.select_dtypes(include=['object']).columns:
        # Replace spaces or dashes between words with underscores
        df[column] = df[column].apply(lambda x: re.sub(r'[-\s]', '_', x))  # Handle hyphen and spaces
        # Convert to lowercase to ensure uniformity
        # df[column] = df[column].str.lower()  # Optional: Uncomment this line if you want to convert to lowercase
    return df

# Load the dataset from the provided path
file_path = "C:\\Users\\16348\\Desktop\\C题数据\\2025_Problem_C_Data\\summerOly_athletes.csv"
athletes_data = pd.read_csv(file_path)

# Apply string standardization
athletes_data = standardize_strings(athletes_data)

# Save the processed data to a new CSV file
output_file_path = "C:\\Users\\16348\\Desktop\\C题数据\\2025_Problem_C_Data\\processed_summerOly_athletes.csv"
athletes_data.to_csv(output_file_path, index=False)

print(f"Processed data has been saved to: {output_file_path}")
