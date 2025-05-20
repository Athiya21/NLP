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
- **Lancaster Stemmer**: More aggressive, producing core roots (e.g., *giv* from *giving*).
- **Snowball Stemmer**: Similar to Porter, supports multiple languages.

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

- **Bag of Words (BoW)**
  - Represents text as a collection of word counts, ignoring order.

- **TF-IDF (Term Frequency–Inverse Document Frequency)**
  - Evaluates word importance in a document based on frequency and rarity.

- **Word2Vec**
  - Neural approach for word embeddings.
  - **CBOW (Continuous Bag of Words)**: Predicts a word from its context.
  - **Skip-Gram**: Predicts context from a given word.
