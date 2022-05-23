# streamlit youtube aggregated data
interactive aggregated youtube visuals from Ken Jee's channel


# Youtube Aggregated Data Visualization for Countries and Video Titles by Streamlit

#### -- Project Status: [Completed]


## Project Intro/Objective
The aim of this project was to uncover which country the views came from, which videos were popular, common keywords in video titles, and whether subscribed users resulted in more likes or dislikes. 


### Methods Used
Data Visualization


### Technologies
* Pycharm
* Python
* Pandas
* Plotly
* Streamlit


## Project Description
Although new insights were discovered from exploring [k_jee_youtube_data](https://github.com/Vitz2007/k_jee_youtube_data/blob/main/notebook/kjee_yt_analysis.ipynb) data set, I wanted to take it a step further and make an interactive visualization where a specific country could be examined and each video title could be further analyzed. 
Because this interactive visualization wouldn’t include all columns, I wanted the fastest way to deploy this and streamlit offered the simplicity and user-friendliness to accomplish this.
One difficulty I ran into with streamlit was that displaying visuals such as graphs with lots of data resulted in a small scale visual. To overcome this and present visuals in a more readable manner, I used plotly's range slider which helped adjust the range to make the visual bigger and readable.


## Needs of this project
- data visualizations
- shareable web app via Streamlit
- let users explore data set through visuals


## Getting started
1. Install streamlit via command line or terminal using pip.
2. Add @st.cache before loading data for faster loading of data.
3. Load csv clean_country_subs [data is here](https://github.com/Vitz2007/streamlit_youtube_agg-app/raw/main/clean_country_subs) into streamlit.
