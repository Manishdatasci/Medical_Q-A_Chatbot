import json
import streamlit as st

# ------------------------------
# 1. Load the cleaned QnA dataset
# ------------------------------
@st.cache_data
def load_dataset():
    with open("fixed_qa_dataset.json", "r", encoding="utf-8") as f:
        return json.load(f)

qa_data = load_dataset()

# ------------------------------
# 2. Streamlit UI Setup
# ------------------------------
st.set_page_config(page_title="🩺 Medical Q&A Chatbot", layout="wide")
st.title("🩺 Medical Q&A Chatbot")
st.markdown("Ask any medical question to get accurate answers from MedQuAD.")

# User input
user_question = st.text_input("🔍 Ask your question here:")

# ------------------------------
# 3. Simple keyword-based search
# ------------------------------
def find_answer(query, data):
    query_lower = query.lower()
    matches = [item for item in data if query_lower in item['question'].lower()]
    return matches[:3] if matches else []

# ------------------------------
# 4. Show the results
# ------------------------------
if user_question:
    results = find_answer(user_question, qa_data)

    if results:
        for i, result in enumerate(results, 1):
            st.markdown(f"### ✅ Result {i}")
            st.markdown(f"**Q:** {result['question']}")
            st.markdown(f"**A:** {result['answer']}")
            if result['source']:
                st.markdown(f"🔗 [Source Link]({result['source']})")
            st.markdown("---")
    else:
        st.warning("❌ No matching answer found. Try asking differently.")
