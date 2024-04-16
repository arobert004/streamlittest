import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")
pd.options.display.max_columns = 200 
pd.options.display.float_format = '{:.3f}'.format

link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'

df = pd.read_csv(link)

issou = sns.histplot(df,
             x = 'time-to-60')

st.button("HISTO", type="primary")
if st.button('HEATMAP'):
    st.pyplot(issou)
else:
    sns.histplot(df,
                x = 'time-to-60')
    plt.title("HEATMAP OF WEATHER DB")
    plt.show()