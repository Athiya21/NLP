import streamlit as st
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize, sent_tokenize, WhitespaceTokenizer, WordPunctTokenizer 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from collections import Counter
import pandas as pd

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

st.title("NLTK Tokenization and Word Cloud App")

# Input text from user
user_text = st.text_area("Enter your text here:", height=200)

if st.button("Generate Word Cloud"):
    if user_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Sentence Tokenization
        st.subheader("Sentence Tokenization")
        sentences = sent_tokenize(user_text)
        st.write(sentences)

        # Word Tokenization
        st.subheader("Word Tokenization")
        words = word_tokenize(user_text)
        st.write(words)

        # Whitespace Tokenization
        st.subheader("Whitespace Tokenization")
        wst = WhitespaceTokenizer()
        whitespace_tokens = wst.tokenize(user_text)
        st.write(whitespace_tokens)

        # WordPunct Tokenization
        st.subheader("WordPunct Tokenization")
        wpt = WordPunctTokenizer()
        wordpunct_tokens = wpt.tokenize(user_text)
        st.write(wordpunct_tokens)

        # Stopwords Removal
        st.subheader("After Removing Stopwords")
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word.lower() not in stop_words and word.isalpha()]
        st.write(filtered_words)

        # Stemming
        st.header("Stemming")

        porter = PorterStemmer()
        lancaster = LancasterStemmer()
        snowball = SnowballStemmer("english")

        porter_stems = [porter.stem(word) for word in filtered_words]
        lancaster_stems = [lancaster.stem(word) for word in filtered_words]
        snowball_stems = [snowball.stem(word) for word in filtered_words]

        st.subheader("Porter Stemmer")
        st.write(porter_stems)

        st.subheader("Lancaster Stemmer")
        st.write(lancaster_stems)

        st.subheader("Snowball Stemmer")
        st.write(snowball_stems)

        # Detokenization
        st.header("Detokenization")
        detokenizer = TreebankWordDetokenizer()
        detokenized_text = detokenizer.detokenize(filtered_words)
        st.write(detokenized_text)

        # Word Cloud
        st.header("Word Cloud")
        filtered_text = ' '.join(filtered_words)
        wordcloud = WordCloud(width=480, height=300, background_color='white').generate(filtered_text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)

        # N-gram Analysis
        st.header("N-Grams")
        n = st.slider("Select N for N-Grams", min_value=2, max_value=5, value=2)
        ngrams = zip(*[filtered_words[i:] for i in range(n)])
        ngram_freq = Counter([" ".join(gram) for gram in ngrams])
        ngram_df = pd.DataFrame(ngram_freq.items(), columns=["N-Gram", "Frequency"]).sort_values(by="Frequency", ascending=False)
        st.dataframe(ngram_df)
