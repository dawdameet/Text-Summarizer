
# Text Summarization using TF-IDF and Cosine Similarity

This project implements a basic extractive text summarization model using **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to generate concise summaries of a given text. The goal is to identify the most important sentences in a document and return a coherent summary.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Explanation](#explanation)
- [Example](#example)
- [License](#license)

## Installation

Before running the script, ensure that the necessary Python libraries are installed. You can install them using `pip`:

```bash
pip install nltk scikit-learn numpy
```

Additionally, you need to download the required NLTK resources:

```python
import nltk
nltk.download('punkt')
```

## Usage

1. Clone or download the repository to your local machine.
2. Run the script directly after installing dependencies.

```bash
python summarize_text.py
```

This will read the input text and print out the summary, which consists of the most relevant sentences.

## Explanation

### Step-by-Step Process:
1. **Text Preprocessing**:
   - The input text is divided into individual sentences using `nltk.sent_tokenize`.
   
2. **TF-IDF Vectorization**:
   - Each sentence is converted into a numerical vector using **TF-IDF** representation. This helps to capture the importance of each term in the sentence relative to the entire document.
   
3. **Document Representation**:
   - The document is represented as the average vector of all sentence vectors in the document.

4. **Cosine Similarity**:
   - Cosine similarity is calculated between each sentence’s vector and the average document vector. This gives us a similarity score for each sentence relative to the entire document.

5. **Ranking and Selecting Top Sentences**:
   - The sentences are ranked based on their similarity scores, and the top N sentences (determined by the user) are selected to form the summary.

### Key Concepts:
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: This metric is used to reflect how important a word is to a document in a collection. It helps to highlight rare words in a document while reducing the impact of common words.
- **Cosine Similarity**: This is used to measure the cosine of the angle between two vectors. In this case, it measures how similar a sentence is to the document by comparing their vector representations.
  
### Output:
The script outputs a short, concise summary containing the most important sentences based on their relevance to the overall document.

## Example

Given the following input text:

```text
A purple octopus wearing a top hat strolled through the bustling marketplace, humming a tune that sounded suspiciously like a mix of jazz and whale songs. Nearby, a group of toaster-like robots were arguing over the best way to butter toast, while a llama on roller skates zoomed past, shouting something about pineapple pizza being the ultimate truth. In the corner of the market, a wizard was selling enchanted cheese graters that could supposedly predict the weather, but only if you asked them nicely. Meanwhile, the clouds above decided to rain tiny marshmallows, which everyone agreed was both delightful and extremely inconvenient.
```

The generated summary could look something like:

```text
"A purple octopus wearing a top hat strolled through the bustling marketplace, humming a tune that sounded suspiciously like a mix of jazz and whale songs. Nearby, a group of toaster-like robots were arguing over the best way to butter toast."
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README should help explain the purpose and usage of the summarization script and provide clear instructions for someone looking to use or contribute to the project!
