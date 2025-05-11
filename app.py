import sqlite3
import streamlit as st
import pandas as pd


@st.cache_data
def get_products():
    conn = sqlite3.connect("db/store.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]

    conn.close()

    df = pd.DataFrame(rows, columns=col_names)
    return df


st.title("📦 รายการสินค้า")
data = get_products()
st.dataframe(data, use_container_width=True)
