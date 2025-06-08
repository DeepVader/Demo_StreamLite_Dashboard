import sqlite3
import streamlit as st
import pandas as pd
import duckdb


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


st.title("📦 รายการสินค้า1")
data = get_products()
st.dataframe(data, use_container_width=True)


@st.cache_data
def get_products():
    duckdb.sql("ATTACH 'db/store.db' AS products")
    df = duckdb.query("SELECT * FROM products.products").df()
    return df


st.title("📦 รายการสินค้า2")
data = get_products()
st.dataframe(data, use_container_width=True)
