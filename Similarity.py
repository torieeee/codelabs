from transformers import AutoTokenizer, AutoModel
import torch
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import json

# Load LaBSE model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/LaBSE")
model = AutoModel.from_pretrained("sentence-transformers/LaBSE")
df=pd.read_excel("E:/Downloads/Test Files.xlsx")

# Assuming 'Other Names' column contains first names
female_names = df[df['Gender'] == 'F']['Other Names'].str.split().str[0].unique()
male_names = df[df['Gender'] == 'M']['Other Names'].str.split().str[0].unique()


def compute_embeddings(names):
    encoded_input = tokenizer(names.tolist(), padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**encoded_input)
    embeddings = model_output.last_hidden_state.mean(dim=1)
    return embeddings

# Compute embeddings for male and female names
male_embeddings = compute_embeddings(male_names)
female_embeddings = compute_embeddings(female_names)

# Compute the similarity matrix
similarity_matrix = cosine_similarity(male_embeddings, female_embeddings)

# Prepare the results dictionary
results = []

# Filter and collect similar names
for i, male_name in enumerate(male_names):
    for j, female_name in enumerate(female_names):
        similarity = similarity_matrix[i][j]
        if similarity >= 0.5:  # 50% similarity threshold
            results.append({
                "male_name": male_name,
                "female_name": female_name,
                "similarity": float(similarity)
            })

# Save results to a JSON file
output_path = "E:/Downloads/similar_names.json"
with open(output_path, 'w') as json_file:
    json.dump(results, json_file, indent=4)
