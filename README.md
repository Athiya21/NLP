# NLP
  - NLU (Natural language understanding)
  - NLG (Natural language Generation)

## Natural Language Understanding (NLU)

### Tokenization
- `word_tokenize`: Tokenizes text into words using NLTK's recommended tokenizer.
- `sent_tokenize`: Splits text into sentences.
- `blankline_tokenize`: Splits text based on blank lines.
- `WhitespaceTokenizer`: Tokenizes text based on whitespace.
- `wordpunct_tokenize`: Splits text into alphabetic and non-alphabetic characters (e.g., punctuation).

### Types of Tokens
- **Bigrams**: Tokens of two consecutive words.
- **Trigrams**: Tokens of three consecutive words.
- **N-grams**: Tokens of *n* consecutive words.

### Stemming
- **Porter Stemmer**: Produces the root form of tokens (e.g., *give* from *giving*).
- **Lancaster Stemmer**: A more aggressive stemmer, producing core roots (e.g., *giv* from *giving*).
- **Snowball Stemmer**: Similar to Porter but supports multiple languages like English, Spanish, French, etc.

### Lemmatization
- Converts words to their base or dictionary form (e.g., *giving* → *give*).

### Parts of Speech (POS) Tagging
- Identifies the grammatical category (noun, verb, adjective, etc.) of each word.

### Named Entity Recognition (NER)
- Detects named entities such as people, organizations, locations, dates, etc.
