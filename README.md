# 🧠 NLP (Natural Language Processing)

- **NLU (Natural Language Understanding)**
- **NLG (Natural Language Generation)**

---

## 🔍 Natural Language Understanding (NLU)

### Tokenization
- `word_tokenize`: Tokenizes text into words.
- `sent_tokenize`: Splits text into sentences.
- `blankline_tokenize`: Splits text based on blank lines.
- `WhitespaceTokenizer`: Tokenizes text based on whitespace.
- `wordpunct_tokenize`: Splits text into alphabetic and non-alphabetic characters.

### Types of Tokens
- **Bigrams**: Tokens of two consecutive words.
- **Trigrams**: Tokens of three consecutive words.
- **N-grams**: Tokens of *n* consecutive words.

### Stemming
- **Porter Stemmer**: Produces the root form of tokens (e.g., *give* from *giving*).
- **Lancaster Stemmer**: A more aggressive stemmer, producing core roots (e.g., *giv* from *giving*).
- **Snowball Stemmer**: Similar to Porter but supports multiple languages like English, Spanish, French, etc.

### Lemmatization
- Converts words to their base or dictionary form (e.g., *achieve* → *achieve*).

### Parts of Speech (POS) Tagging
- Identifies grammatical categories (noun, verb, adjective, etc.).

### Named Entity Recognition (NER)
- Detects entities such as people, organizations, locations, dates, etc.

---

## ✍️ Natural Language Generation (NLG)

### Word Cloud
- Visual representation of text data where word size indicates frequency or importance.

### NLP Algorithms | Word Embedding Algorithms

 **Bag of Words (BoW)**
  - Represents text as a collection of individual word counts, ignoring grammar and word order but preserving multiplicity.

- **TF-IDF (Term Frequency–Inverse Document Frequency)**
  - A statistical measure used to evaluate how important a word is to a document in a collection, balancing frequency with uniqueness.

- **Word2Vec**
  - A neural network-based approach to learn word embeddings (vector representations of words).
  - **CBOW (Continuous Bag of Words)**: Predicts the target word from surrounding context words.
  - **Skip-Gram**: Predicts surrounding context words from a target word.

![image](https://github.com/user-attachments/assets/b50a1f41-4511-4ae8-8099-3b37e4a7f9cb)
