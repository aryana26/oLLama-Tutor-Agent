import re
import streamlit as st
from agents.chat_agent import run_chat_agent

st.set_page_config(page_title="AI Tutor Agent", page_icon="🤖")
st.title("🤖 AI Tutor Agent with LaTeX")

query = st.text_input("Enter your question:")

# if query:
#     with st.spinner("Thinking..."):
#         response = run_chat_agent(query)

#     st.markdown("### 📖 Explanation")
#     st.markdown(response)

#     # Optional: Render LaTeX if detected
#     if "$$" in response or "\\(" in response:
#         st.markdown("### 🧮 Rendered Math")
#         try:
#             st.latex(response.split("$$")[1])
#         except:
#             st.info("LaTeX rendering skipped (invalid format).")

if query:
    with st.spinner("Thinking..."):
        response = run_chat_agent(query)

    st.markdown("### 📖 Response")
    st.markdown(response)

    # Try rendering all block LaTeX from $$...$$
    latex_blocks = re.findall(r"\$\$(.*?)\$\$", response, re.DOTALL)
    if latex_blocks:
        st.markdown("### 🧮 Rendered Equations")
        for expr in latex_blocks:
            st.latex(expr.strip())

    # Optionally also render inline math ($...$)
    inline_exprs = re.findall(r"\$(.*?)\$", response)
    if inline_exprs and not latex_blocks:
        st.markdown("### 🧮 Inline Math")
        for expr in inline_exprs:
            st.latex(expr.strip())

