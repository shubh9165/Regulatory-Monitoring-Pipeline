import streamlit as st
from src.database.database import create_database
from scheduler import start
from dotenv import set_key

# Create SQLite database
create_database()

st.set_page_config(page_title="AI Regulatory Monitoring", page_icon="📄")

st.title("📄 AI Regulatory Monitoring System")

# Website selection
website = st.selectbox(
    "Select Website",
    ["RBI", "SEBI","IRDAI"]
)


# Email input
email = st.text_input("Enter your Email ID")



# Start Monitoring
if st.button("🚀 Start Monitoring"):

    if email == "":
        st.warning("Please enter your Email ID.")
    else:

        set_key(".env","website",website)
        set_key(".env","receiver",email)

        with st.spinner("Monitoring regulations..."):
            start()

        st.success("✅ Monitoring Completed Successfully!")