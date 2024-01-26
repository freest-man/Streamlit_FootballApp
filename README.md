# Streamlit_FootballApp

App Deployed Here ---> https://footballapp.streamlit.app/


Incase the App malfunctions here's a demo:

(https://www.youtube.com/watch?v=MqCAH1u2aao&ab_channel=Sasi)

This code is a Streamlit app for exploring English Premier League (EPL) football team statistics.

For the Data Visualisation UI, the package used is PygWalker
Check it out here: https://kanaries.net/home/pygwalker

Let me break down the key components for you:

1/ Imports

![image](https://github.com/freest-man/Streamlit_FootballApp/assets/116303271/6217c586-ca03-4cd1-8d04-cd7ba24b1979)

These are Python libraries used for creating the web app (Streamlit for the app interface), handling data (Pandas, NumPy), and creating visualizations (**PygWalker**).

StreamlitRender is for rendering the Dashboard UI

init_streamlit_com is for initiating communication between pygwalker and streamlit

GlobalVarManager is to set the Kanaries API for the chat feature.

2/ App Title and Description:

![image](https://github.com/freest-man/Streamlit_FootballApp/assets/116303271/abd1d682-bd09-4cd7-89ec-3b98c7ffebc8)

It sets the title of the app and provides a brief description of what the app does, including the Python libraries used and the data source.

3/ User Input Sidebar

![image](https://github.com/freest-man/Streamlit_FootballApp/assets/116303271/d2da7e72-bd26-4a66-9494-e359c25cdaf9)

The sidebar allows users to select the year for which they want to explore EPL stats.

4/ Data Source and Web Scraping

![image](https://github.com/freest-man/Streamlit_FootballApp/assets/116303271/c4443705-0799-4d87-89d9-0c672a704898)

The load_data function retrieves EPL team stats for the selected year by scraping data from the provided URL. 
The data is stored in a Pandas DataFrame.

5/ User Input for Team Selection

![image](https://github.com/freest-man/Streamlit_FootballApp/assets/116303271/53aeaba8-14fd-4b8f-b5ba-ced77c34d7d2)

Users can select one or more teams from the sidebar.

The data is filtered based on the selected teams, and the resulting DataFrame is displayed.

6/ Visualization

![image](https://github.com/freest-man/Streamlit_FootballApp/assets/116303271/82933d07-3064-4085-be5d-e96ce06af10f)


A button is provided to generate a visualization using the PygWalker library.

The button triggers the creation and rendering of a PyGWalker visualization using a cached instance of the StreamlitRenderer class.
