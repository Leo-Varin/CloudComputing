import streamlit as st
import pandas as pd

def main():
    st.title("CV Data Viewer")
    st.sidebar.header("Settings")
    
    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Data")
        st.write(df)

if __name__ == "__main__":
    main()