import streamlit as st
from gtts import gTTS
import os
from langdetect import detect, LangDetectException
from deep_translator import GoogleTranslator
import pycountry
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import nltk
import base64

nltk.download('punkt')
nltk.download('words')

# Initialize session state for selected languages
if "selected_langs" not in st.session_state:
    st.session_state.selected_langs = []

# Function to read text aloud
def read_aloud(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("temp.mp3")
    audio_file = open("temp.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    audio_file.close()
    os.remove("temp.mp3")

# Function to generate word cloud
def generate_wordcloud(text):
    english_words = set(nltk.corpus.words.words())
    words = word_tokenize(text)
    english_words_in_text = [word for word in words if word.lower() in english_words]
    english_text = ' '.join(english_words_in_text)

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(english_text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    plt.tight_layout()
    return fig

# Background image setup
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_img_base64 = get_base64("back.jpg")  # Use your image file

# CSS: background + fixed visible title (not cut off) + spacing
page_bg_css = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{bg_img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

h1 {{
    position: fixed;
    # top: 30px; /* moved down to prevent cutting off */
    top: 45px;
    left: 0;
    right: 0;
    z-index: 9999;
    margin: auto;
    width: 100%;
    font-size: 2.5em;
    color: black;
    background-color: rgba(255,255,255,0.7);
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    backdrop-filter: blur(5px);
}}

.block-container {{
    # padding-top: 120px;
    padding-top: 140px;
}}

label, .stTextArea label, .stMultiSelect label {{
    color: var(--text-color) !important;
    font-weight: bold;
}}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# Fixed, clear title
st.markdown("<h1>🌐 Globalize</h1>", unsafe_allow_html=True)

# # Function to handle language selection
# def on_lang_select():
#     for lang in st.session_state.target_languages_input:
#         if lang not in st.session_state.selected_langs:
#             st.session_state.selected_langs.append(lang)
def on_lang_select():
    st.session_state.selected_langs = st.session_state.target_languages_input.copy()

    # DO NOT clear dropdown so selected langs are visible
    # If you want them to disappear from dropdown, keep clearing:
    # st.session_state.target_languages_input = []

# Layout
col1, col2 = st.columns(2)

# with col1:
#     paragraph = st.text_area("Enter one paragraph:")
with col1:
    st.markdown(
        '<div style="font-weight: bold; font-size: 20px; margin-bottom: -80px; color: white">Enter one paragraph:</div>', 
        unsafe_allow_html=True
    )
    paragraph = st.text_area(label="", key="paragraph_input", height=150)


with col2:
    all_languages = [lang.name for lang in pycountry.languages if hasattr(lang, 'alpha_2')]

    # Language dropdown removes only unselected options
    available_languages = [lang for lang in all_languages if lang not in st.session_state.selected_langs]

    # Merge selected back into the list so they stay visible in box
    current_selection = st.session_state.get("target_languages_input", [])
    dropdown_options = st.session_state.selected_langs + available_languages

    st.markdown(
        '<div style="font-weight: bold; font-size: 17px; margin-bottom: -50px; color: white;">Select the desired languages for translation:</div>',
        unsafe_allow_html=True
    )
    target_languages_input = st.multiselect(
        label="",  # empty label to hide default label
        options=dropdown_options,
        default=st.session_state.selected_langs,
        key="target_languages_input",
        on_change=on_lang_select
   )

    # target_languages_input = st.multiselect(
    #     "Select the desired languages for translation:",
    #     options=dropdown_options,
    #     default=st.session_state.selected_langs,
    #     key="target_languages_input",
    #     on_change=on_lang_select
    # )

# Read original aloud
if st.button("Read Aloud"):
    if paragraph.strip():
        read_aloud(paragraph)
    else:
        st.warning("Please enter some text to read aloud.")


# Language detection
paragraph_language = None
if paragraph.strip():
    try:
        paragraph_language = detect(paragraph)
        language_name = pycountry.languages.get(alpha_2=paragraph_language).name
        st.write("**Detected language:**", language_name)
        # read_aloud(paragraph, paragraph_language)
    except LangDetectException as e:
        st.error("Language detection failed: {}".format(e))
        paragraph_language = 'en'
        language_name = 'English'
    except Exception as e:
        st.error("Error during language detection: {}".format(e))


# Language detection
# paragraph_language = None
# if paragraph.strip():
#     try:
#         paragraph_language = detect(paragraph)
#         language_name = pycountry.languages.get(alpha_2=paragraph_language).name
#         st.write("**Detected language:**", language_name)
#         read_aloud(paragraph, paragraph_language)

#     except LangDetectException as e:
#         st.error("Language detection failed: {}".format(e))
#         paragraph_language = 'en'
#         language_name = 'English'
#     except Exception as e:
#         st.error("Error during language detection: {}".format(e))

# Translate to English if needed
if paragraph_language and paragraph_language != 'en':
    try:
        translated_paragraph = GoogleTranslator(source=paragraph_language, target='en').translate(paragraph)
        st.write("**Translated to universal language English:**")
        st.write(translated_paragraph)
    except Exception as e:
        st.error(f"Translation to English failed: {e}")
        translated_paragraph = paragraph
else:
    translated_paragraph = paragraph

# Word cloud
if translated_paragraph.strip():
    try:
        translated_paragraph_utf8 = translated_paragraph.encode('utf-8', 'ignore').decode('utf-8')
        wordcloud_fig = generate_wordcloud(translated_paragraph_utf8)
        st.sidebar.subheader("Word Cloud")
        st.sidebar.pyplot(wordcloud_fig)
    except Exception as e:
        st.error(f"Error generating word cloud: {e}")

# Translate and speak
if st.button("Translate and Read Aloud"):
    if not paragraph.strip():
        st.warning("Please enter a paragraph first.")
    elif not st.session_state.selected_langs:
        st.warning("Please select at least one target language.")
    else:
        for lang_name in st.session_state.selected_langs:
            try:
                lang_code = pycountry.languages.lookup(lang_name).alpha_2
                translated_text = GoogleTranslator(source=paragraph_language, target=lang_code).translate(paragraph)
                st.write(f"**Translated paragraph in {lang_name}:**")
                st.write(translated_text)
                read_aloud(translated_text, lang_code)
            except Exception as e:
                st.error(f"Translation to {lang_name} failed: {e}")
