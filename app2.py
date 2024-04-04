import streamlit as st
import pandas as pd

def main():
    st.title(' Cloud - Résultats metrics view')
    df = pd.readcsv('data2.csv')
    st.write("Accurancy per epoch")
    st.linechart(data=df, x='epoch', y='accuracy')
    st.write("Mean Iou per epoch")
    st.linechart(data=df, x='epoch', y='mean_iou')
    st.write("Loss per epochs")
    st.line_chart(data=df, x='epoch', y='loss')
if __name__ == "__main":
    main()