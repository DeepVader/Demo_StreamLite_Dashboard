import sqlite3
import streamlit as st
import pandas as pd
import duckdb


@st.cache_data
def get_products1():
    conn = sqlite3.connect("db/store.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]

    conn.close()

    df = pd.DataFrame(rows, columns=col_names)
    return df


st.title("📦 รายการสินค้า1")
data = get_products1()
st.dataframe(data, use_container_width=True)


@st.cache_data
def get_products2():
    duckdb.sql("ATTACH 'db/store.db' AS store")
    df = duckdb.query("SELECT * FROM store.products").df()
    return df


st.title("📦 รายการสินค้า2")
data = get_products2()
st.dataframe(data, use_container_width=True)


@st.cache_data
def get_air():
    duckdb.sql("ATTACH 'db/airbnb.db' AS airbnb")
    airbnb_listings = duckdb.query("SELECT * FROM airbnb.airbnb_listings").df()
    return airbnb_listings


st.title("🏠 รายการ Airbnb")
data = get_air()
st.dataframe(data, use_container_width=True)
