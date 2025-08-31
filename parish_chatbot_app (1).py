
import streamlit as st

st.set_page_config(page_title='Parish Bulletin Chatbot', layout='wide')
st.title('🕍 Catholic Parish Bulletin Chatbot')

# Sidebar filters
st.sidebar.header('🔍 Filter Options')
selected_parish = st.sidebar.text_input('Enter Parish Name (optional)')
selected_date = st.sidebar.text_input('Enter Bulletin Date (optional)')

# Chat interface
st.subheader('💬 Ask a question about the parish bulletins')
user_query = st.text_input('Your question:')

# Load bulletin text from PDF
import fitz
with fitz.open("merged1 (1).pdf") as doc:
    bulletin_text = " ".join([page.get_text() for page in doc])

# Simple keyword-based response logic
def answer_query(query, text):
    query_lower = query.lower()
    File "/mount/src/-parish-chatbot/parish_chatbot_app (1).py", line 29, in <module>
    response = answer_query(user_query, bulletin_text)
File "/mount/src/-parish-chatbot/parish_chatbot_app (1).py", line 24, in answer_query
    lines = text.split('')
    matched_lines = [line for line in lines if query_lower in line.lower()] 
    return "".join(matched_lines[:10]) if matched_lines else "Sorry, no relevant information found."

if user_query:
    response = answer_query(user_query, bulletin_text)
    st.markdown('### 📝 Response')
    st.write(response)
