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
  - **CBOW (Continuous Bag of Words)**
    - **How It Works**: CBOW predicts a target word given a context of surrounding words.
    - **For instance**, in the sentence "The cat sits on the mat," if you take the context words 
       "The," "cat," "on," "the," and "mat," CBOW would predict the target word "sits."
      
  - **Skip-Gram**
    - **How It Works**: Skip-gram does the opposite of CBOW; it uses a target word to predict its surrounding context words. For example, given the target word "sits," it                             would try to predict the context words around it.
    - **For instance**, Given the target word "sits," Skip-gram might predict the context words ("The," "cat," "on," "the," "mat").

     ![image](https://github.com/user-attachments/assets/b50a1f41-4511-4ae8-8099-3b37e4a7f9cb)

---
 ## 📚 Chunking in NLP

Chunking refers to the process of dividing text into meaningful segments, typically called **chunks**.

### Types of Chunks
- **Noun Phrase (NP)**: Groups of words that function as a noun  
  _Example_: "the big red ball"
- **Verb Phrase (VP)**: Consists of the main verb and any accompanying words  
  _Example_: "is running quickly"
- **Prepositional Phrase (PP)**: Phrases that begin with a preposition  
  _Example_: "under the table"

---

## 🤖 Chunking in LLMs

In the context of **Large Language Models (LLMs)**, *chunking* refers to a method of processing input text in smaller, manageable segments or "chunks".  
This is particularly useful for handling long inputs that exceed a model’s maximum token limit.

---

## 🧠 Transformers in NLP

The term **"transformers"** refers to a deep learning architecture introduced in the paper _"Attention is All You Need"_ by Vaswani et al., 2017.  
Transformers have since become the foundation for many state-of-the-art NLP models.

### Popular Transformer Models & Variants

1. **BERT** (Bidirectional Encoder Representations from Transformers)  
   - Understands context from both directions using masked language modeling.

2. **GPT** (Generative Pre-trained Transformer)  
   - Developed by OpenAI. Autoregressive model used primarily for text generation (e.g., GPT-2, GPT-3, GPT-4).

3. **T5** (Text-to-Text Transfer Transformer)  
   - Treats every NLP task as a text-to-text problem, offering great flexibility.

4. **RoBERTa** (A Robustly Optimized BERT Pretraining Approach)  
   - An optimized variant of BERT trained with more data and refined techniques.

5. **XLNet**  
   - Combines BERT’s bidirectionality with autoregressive features for improved dependency modeling.

6. **ALBERT** (A Lite BERT)  
   - Reduces model size while maintaining performance, optimized for efficiency.

7. **DistilBERT**  
   - A smaller, faster version of BERT that retains 95% of its performance.

8. **ERNIE** (Enhanced Representation through kNowledge Integration)  
   - Integrates external knowledge to boost language understanding. Developed by Baidu.

9. **ELECTRA**  
   - Trains more efficiently than BERT by predicting replaced tokens instead of masking them.

10. **DeBERTa** (Decoding-enhanced BERT with Disentangled Attention)  
    - Uses disentangled attention to improve performance on a variety of tasks.

11. **Vision Transformers (ViT)**  
    - Adapts the transformer model for image classification by treating images as sequences of patches.

12. **BART** (Bidirectional and Auto-Regressive Transformers)  
    - Combines BERT-style encoding with GPT-style decoding. Great for summarization and translation.

13. **LayoutLM**  
    - Designed for document understanding tasks, incorporating text layout and position information.

14. **Swin Transformer**  
    - A hierarchical vision transformer for image classification and detection tasks.

15. **Transformer-XL**  
    - Introduces recurrence for better handling of long sequences.

---

### 🚀 Note
> The field of transformers is rapidly evolving with ongoing research and newer models constantly being introduced.

---
### spacy
    -- spaCy is a powerful and efficient open-source library for advanced Natural Language Processing (NLP) in Python. It is designed specifically for production use, 
         providing fast and accurate tools to process and analyze large volumes of text. spaCy supports tasks such as tokenization, part-of-speech tagging, named entity 
         recognition, dependency parsing, and more, making it a popular choice for building NLP applications.

**Setting Up spaCy**

      - Install spaCy using pip.
        
      -  Download the English language model using the command:
        python -m spacy download en_core_web_sm
        
      - To verify the installation and get spaCy info, run:
        python -m spacy info
        
      - (Optional) If you face any issues related to Intel MKL, reinstall MKL by running:
        pip install --force-reinstall mkl
        
      - Run the info command again to confirm the setup:
        python -m spacy info

 **Setting Up spaCy in VS Code**
      - Open the integrated terminal in VS Code by pressing Ctrl + ~ (tilde).
        
      - Activate your Conda environment (if using Conda) by typing:

      - python -m ipykernel install --user --name spacyenv --display-name "Python (spacyenv)
        
      - conda activate spacyenv
        
      - Restart VS Code to apply the environment changes.
        
      - Select the Python interpreter for your environment:
        
      - Press Ctrl + Shift + P to open the Command Palette.
        
      - Search for and select Python: Select Interpreter.
        
      - Choose your Conda environment (for example, spacyenv (Python 3.x.x)).

---

### Multiple Language Translation
  
  **To set up the environment for multiple language translation, install the following Python packages:**

     - Install Streamlit for building interactive web apps.
      
     - Install mtranslate for language translation.
      
     - Install gTTS (Google Text-to-Speech) for converting text to speech.
      
     - Install pycountry to access ISO country and language information.
      
     - Install wordcloud for generating word cloud visualizations.

**You can install these packages using the following commands in your terminal or command prompt:**

    - pip install streamlit

    - pip install mtranslate
    
    - pip install gtts
    
    - pip install pycountry
    
    - pip install wordcloud

---
### NLU Stream

  **To run the NLU Stream project, please install the following Python packages:**
  
      - pip install streamlit
      
      - pip install gtts
      
      - pip install langdetect
      
      - pip install googletrans
      
      - pip install pycountry
      
      - pip install wordcloud
      
      - pip install nltk
      
      - pip install googletrans==4.0.0-rc1
      
      - pip install deep_translator


---

### XML Scraping & NLP Processing
    - This project demonstrates how to effectively scrape and clean XML files using Python libraries like xml.etree.ElementTree, BeautifulSoup, and Natural Language 
     Processing (NLP) techniques.
    
  **📌 Features**
      
      - 🗂️ Parse raw XML files
        
      - 🧼 Clean and extract structured data
        
      - 🔍 Preprocess text using NLP libraries
        
      - 🧠 Ready for downstream tasks (e.g., classification, NER)
      
  **🛠️ Technologies Used**
  
        - xml.etree.ElementTree – Standard Python library for parsing XML
        
        - BeautifulSoup – For flexible parsing and cleaning of messy XML/HTML
        
        - nltk – For tokenization, stopword removal, lemmatization

---
