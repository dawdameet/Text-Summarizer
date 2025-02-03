### **Theory of Automated Text Summarization**

Text summarization can be broadly divided into two categories:
1. **Extractive Summarization**: Selects a subset of sentences from the original text to form a summary.
2. **Abstractive Summarization**: Generates new sentences that paraphrase the key information in the text, often using models like **GPT-3**, **BERT**, or **T5**.

We’ll focus on **Extractive Summarization** first, as it’s easier to implement and understand. This involves calculating the **importance of each sentence** and selecting the most relevant ones.

---

### **Mathematics Behind Extractive Summarization**

For extractive summarization, one common approach is **Sentence Similarity**. We calculate how similar each sentence is to the entire document and then select the most relevant sentences.

1. **Text Representation**: Convert each sentence into a numerical vector using techniques like **TF-IDF (Term Frequency-Inverse Document Frequency)** or **Word Embeddings** (Word2Vec, GloVe).

   - **TF-IDF** measures how important a word is in a document, considering its frequency in the document and its rarity in the corpus.
   
   \[
   \text{TF-IDF}(w, D) = \text{TF}(w, D) \times \log\left(\frac{N}{\text{DF}(w)}\right)
   \]
   
   Where:
   - \( w \) = word
   - \( D \) = document
   - \( N \) = total number of documents
   - \( \text{DF}(w) \) = number of documents containing word \( w \)

2. **Cosine Similarity**: Once we have vector representations for each sentence, we calculate the **cosine similarity** between sentences to find the most relevant ones.

   \[
   \text{Cosine Similarity}(A, B) = \frac{A \cdot B}{||A|| ||B||}
   \]
   Where:
   - \( A \) and \( B \) are vectors of the sentence.
   - \( \cdot \) denotes the dot product.
   - \( ||A|| \) and \( ||B|| \) are the magnitudes of vectors \( A \) and \( B \), respectively.

   The higher the cosine similarity between a sentence and the document, the more important that sentence is.

3. **Sentence Ranking**: After calculating similarity, rank all the sentences and select the top ones based on their relevance to the document.

---


