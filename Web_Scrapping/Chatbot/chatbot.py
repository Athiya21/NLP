import streamlit as st
from nltk.chat.util import Chat, reflections
import streamlit.components.v1 as components

pairs = [
    [r"(.*)(fever|cough|cold|headache|pain)(.*)",
     ["It seems like you're experiencing %2. Please rest, drink fluids, and consider visiting a doctor if it persists."]],
    [r"(.*)appointment(.*)",
     ["You can schedule an appointment with our healthcare provider. Would you like to book for today or tomorrow?"]],
    [r"(.*)emergency(.*)",
     ["If this is an emergency, please call 108 or visit your nearest hospital immediately."]],
    [r"(.*)your name ?",
     ["My name is MedBot, your healthcare assistant."]],
    [r"hi|hello|hey|hola|holla",
     ["Hello! I'm here to assist you with health-related questions."]],
    [r"(.*)help(.*)",
     ["Sure, I can assist with symptoms, booking appointments, or general advice."]],
    [r"(.*)today",
     ["Appointment booked for today. A confirmation will be sent to your phone."]],
    [r"(.*)tomorrow",
     ["Appointment booked for tomorrow. A confirmation will be sent to your phone."]],
    [r"(.*)feeling (.*)tired(.*)",
     ["Fatigue can be caused by many factors like stress, lack of sleep, or illness. Consider resting or speaking to a doctor."]],
    [r"(.*)created",
     ["Athiya created me using Python's NLTK library.", "top secret ;)"]],
    [r"quit",
     ["Take care! If needed, visit us again."]],
    [r"(.*)",
     ["I'm here to assist you. Could you please rephrase or be more specific?"]]
]

chatbot = Chat(pairs, reflections)

st.set_page_config("🩺 MedBot", layout="centered")

# Fixed header outside the chatbox
# st.markdown("""
# <div style='position:sticky; top:0; background-color:white; padding:10px 0; z-index:999; border-bottom:1px solid #eee;'>
#     <h2 style='text-align:center; margin:0;'>🩺 MedBot: Your Healthcare Assistant</h2>
# </div>
# """, unsafe_allow_html=True)
st.markdown("""
<div style='
    position: sticky;
    top: -1;
    background: linear-gradient(90deg, #4e9af1, #1f77f3);
    color: white;
    padding: 15px 0;
    z-index: 999;
    border-bottom: 2px solid #0a47a1;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
'>
    <h1 style='
        text-align: center;
        margin: 0;
        font-weight: 900;
        font-size: 2.5rem;
        letter-spacing: 0.1px;
        user-select: none;
    '>🩺 MedBot: Your Healthcare Assistant</h1>
</div>
""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = [
        ("MedBot", "Hello! I am MedBot, created by Athiya. I can assist you regarding healthcare.")
    ]

# Build chat HTML with scrollable div 300px height and auto-scroll JS
chat_html = """
<div id="chat-box" style="height: 250px; overflow-y: auto; padding: 12px; border-radius: 10px; background: #f9f9f9; border:1px solid #ccc;">
"""
for sender, msg in st.session_state.history:
    align = "right" if sender == "You" else "left"
    bg = "#dcf8c6" if sender == "You" else "#eeeeee"
    chat_html += f"""
    <div style="text-align:{align}; margin: 6px 0;">
        <span style="display:inline-block; background:{bg}; padding:10px 15px; border-radius:18px; max-width:75%;">{msg}</span>
    </div>
    """
chat_html += "</div>"

# Inject JS to auto scroll chat box to bottom on load
chat_html += """
<script>
    var chatBox = document.getElementById('chat-box');
    if(chatBox){
        chatBox.scrollTop = chatBox.scrollHeight;
    }
</script>
"""

components.html(chat_html, height=260, scrolling=False)

# Fixed input area below chat box
with st.form("chat_form", clear_on_submit=True):
    cols = st.columns([10, 1])
    user_input = cols[0].text_input("Type your message...", label_visibility="collapsed")
    submit = cols[1].form_submit_button("➤")

if submit and user_input.strip():
    msg = user_input.strip()
    st.session_state.history.append(("You", msg))
    reply = chatbot.respond(msg)
    st.session_state.history.append(("MedBot", reply))
    st.rerun()