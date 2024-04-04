import streamlit as st
import pandas as pd

def main():
    st.title('Cloud - Résultats metrics view')
    df = pd.read_csv('data2.csv')
    
    st.write("Accuracy per epoch")
    filtered_df = df[(df['accuracy'] >= 0.8) & (df['accuracy'] <= 1.0)]
    st.line_chart(data=filtered_df, x='epoch', y='accuracy', use_container_width=True, height=400)
    
    st.write("Mean IoU per epoch")
    filtered_df = df[(df['mean_iou'] >= 0.8) & (df['mean_iou'] <= 1.0)]
    st.line_chart(data=filtered_df, x='epoch', y='mean_iou', use_container_width=True, height=400)
    
    st.write("Loss per epochs")
    st.line_chart(data=df, x='epoch', y='loss', use_container_width=True, height=400)

if __name__ == "__main__":
    main()


#sudo su
#yum install git
#git clone https://github.com/Leo-Varin/CloudComputing.git
#yum install python3-pip
#python3 -m pip install --ignore-installed streamlit
#python3 -m streamlit run app.py