!pip install -q streamlit altair pandas numpy pyngrok

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Заголовок дашборда
st.title("Дашборд для визуализации симулированных данных")
st.markdown("""
Данный дашборд демонстрирует работу с простыми данными и интерактивными графиками.
Вы можете настроить параметры генерации данных (количество точек и тип распределения) с помощью боковой панели.
""")

# Боковая панель для настройки параметров
st.sidebar.header("Настройки данных")
num_points = st.sidebar.slider("Число точек", min_value=100, max_value=1000, value=500, step=50)
distribution = st.sidebar.selectbox("Тип распределения", ["Нормальное", "Экспоненциальное"])

# Генерация данных
if distribution == "Нормальное":
    data = np.random.normal(loc=0, scale=1, size=num_points)
else:
    data = np.random.exponential(scale=1, size=num_points)

# Преобразование данных в DataFrame
df = pd.DataFrame({"value": data})

# Построение гистограммы через Altair
st.subheader("Гистограмма распределения")
chart = alt.Chart(df).mark_bar().encode(
    alt.X("value:Q", bin=alt.Bin(maxbins=30), title="Значение"),
    alt.Y("count()", title="Количество")
).properties(width=600, height=400)
st.altair_chart(chart, use_container_width=True)

# Отображение таблицы с первыми 20 строками данных
st.subheader("Таблица с данными")
st.dataframe(df.head(20))
