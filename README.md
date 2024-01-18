# Streamlit_FootballApp

App Deployed Here ---> https://footballapp.streamlit.app/


Incase the App malfunctions here's a demo:

(https://www.youtube.com/watch?v=MqCAH1u2aao&ab_channel=Sasi)

This code is a Streamlit app for exploring English Premier League (EPL) football team statistics.

For the Data Visualisation UI, the package used is PygWalker
Check it out here: https://kanaries.net/home/pygwalker

Let me break down the key components for you:

1/ Imports

![image](https://github.com/freest-man/Streamlit_FootballApp/assets/116303271/3c09367f-37aa-4d6f-b768-3f434df36596)


These are Python libraries used for creating the web app (Streamlit for the app interface), handling data (Pandas, NumPy), and creating visualizations (PygWalker).

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

![image](https://github.com/freest-man/Streamlit_FootballApp/assets/116303271/876fc148-6896-482f-b552-0730c8b475fa)

Users can select one or more teams from the sidebar.

6/ Filtering and Displaying Data

![image](https://github.com/freest-man/Streamlit_FootballApp/assets/116303271/ef0404df-6bb2-403f-9e65-1c3bb1a74720)

The data is filtered based on the selected teams, and the resulting DataFrame is displayed.

7/ Visualization

![image](https://github.com/freest-man/Streamlit_FootballApp/assets/116303271/41b1ca91-d398-4334-86b3-502eff821d57)

A button is provided to generate a visualization using the PygWalker library. 

When clicked, it calls the analysisdash function, which converts the DataFrame to HTML using PygWalker and displays it in the app.
