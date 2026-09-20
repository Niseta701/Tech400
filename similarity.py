import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

folder_path = "articles"

documents = []
filenames = []

for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
            documents.append(f.read())
            filenames.append(file)

vectorizer = TfidfVectorizer(stop_words="english")

tfidf_matrix = vectorizer.fit_transform(documents)

similarity_matrix = cosine_similarity(tfidf_matrix)

df = pd.DataFrame(
    similarity_matrix,
    index=filenames,
    columns=filenames
)

print("\nDocument Similarity Matrix:\n")
print(df.round(3))


#heatmap
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,8))
sns.heatmap(df, annot=True)

plt.title("Document Similarity Matrix")
plt.show()