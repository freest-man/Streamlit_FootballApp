import streamlit as st
import pandas as pd
import base64
import numpy as np
import pygwalker as pyg
import streamlit.components.v1 as components


st.title('EPL Stats Explorer')

st.markdown("""
This app performs simple webscraping of EPL Football Team stats data !
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [https://fbref.com/en/](https://fbref.com/en/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1992,2024))))

league_data = {
    0: "League Standings",
    2: "Squad Stats",
    4: "GK Stats",
    8: "Shooting Stats",
    10: "Passing Stats",
    16: "Defensive Stats",
    18: "Possesion Stats"
}

values_list = [value for value in league_data.values()]

selected_stat = st.sidebar.selectbox('Select the Stat', [value for value in league_data.values()])


def get_keys_by_value(dictionary, target_value):
    return [key for key, value in dictionary.items() if value == target_value]


target_value = selected_stat
ass_key = get_keys_by_value(league_data, target_value)



# Web scraping of EPL Team stats
# https://fbref.com/en/comps/9/Premier-League-Stats
#@st.cache_data
def load_data(year):
    url = "https://fbref.com/en/comps/9/" + str(year) + "-" + str(year+1)
    if selected_stat == "League Standings":
        html = pd.read_html(url, header=0)
    else:
        html = pd.read_html(url, header=1)
    df = html[ass_key[0]]
    raw = df.reset_index(drop=True)
    raw = raw.fillna(0)
    playerstats = raw
    return playerstats
playerstats = load_data(selected_year)




# Sidebar - Team selection
sorted_unique_team = sorted(playerstats.Squad.unique())
selected_team = st.sidebar.multiselect('Squad', sorted_unique_team, sorted_unique_team)

# # Sidebar - Position selection
# unique_pos = ['RB','QB','WR','FB','TE']
# selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# # Filtering data
df_selected_team = playerstats[(playerstats.Squad.isin(selected_team))]

st.markdown(f"* **Data Shown:** {selected_stat} ")


st.write(df_selected_team)



def analysisdash():
    pyg_html = pyg.to_html(df_selected_team)
    # Embed the HTML into the Streamlit app
    components.html(pyg_html, height=1000, width= 1100  , scrolling=True)



if st.button("Create Visualisation with this Data"):
    analysisdash()
