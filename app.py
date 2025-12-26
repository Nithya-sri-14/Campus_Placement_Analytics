import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Campus Placement Analytics", layout="wide")

st.title("📊 Campus Placement Analytics Dashboard")

# Load dataset
df = pd.read_csv("placement_data.csv")

# Convert Yes/No to numeric
df['Placed'] = df['Placed'].map({'Yes': 1, 'No': 0})

# Metrics
total_students = len(df)
placed_students = df['Placed'].sum()
placement_percentage = (placed_students / total_students) * 100

c1, c2, c3 = st.columns(3)
c1.metric("Total Students", total_students)
c2.metric("Placed Students", placed_students)
c3.metric("Placement %", f"{placement_percentage:.2f}%")

# Pie chart
st.subheader("Placed vs Not Placed")
fig1, ax1 = plt.subplots()
df['Placed'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax1)
st.pyplot(fig1)

# Department-wise placement
st.subheader("Department-wise Placement")
dept = df.groupby('Department')['Placed'].mean() * 100
fig2, ax2 = plt.subplots()
dept.plot(kind='bar', ax=ax2)
ax2.set_ylabel("Placement %")
st.pyplot(fig2)

# Company-wise hiring
st.subheader("Top Recruiting Companies")
company = df[df['Placed'] == 1]['Company'].value_counts()
fig3, ax3 = plt.subplots()
company.plot(kind='bar', ax=ax3)
st.pyplot(fig3)

# CGPA vs Package
st.subheader("CGPA vs Package")
fig4, ax4 = plt.subplots()
sns.scatterplot(data=df, x='CGPA', y='Package_LPA', ax=ax4)
st.pyplot(fig4)

