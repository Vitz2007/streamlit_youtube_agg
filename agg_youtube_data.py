# Import libraries
import pandas as pd
import streamlit as st
import plotly.express as px


# Give a Title
st.title('Aggregated Youtube Data for Countries')

# Load cleaned data and cache via Streamlit
@st.cache
def load_data():
    agg_country_subs = pd.read_csv('clean_country_subs').loc[:,
                       'video_title':'average_watch_time']
    return agg_country_subs

# Create dataframe from function
agg_country_subs = load_data()

# Filtering by continents
continent_select = agg_country_subs['continent'].drop_duplicates()


# Build a dashboard with widget sidebar
continent_sidebar = st.sidebar.selectbox('Select a continent:', continent_select)


# Get new df for continent is continent_sidebar
continent_country = agg_country_subs.loc[agg_country_subs.continent == continent_sidebar]


# Retrieve country video_title columns from original df and drop duplicates
country_select = continent_country.country.drop_duplicates()
# video_select = continent_country.video_title.drop_duplicates()

# Display country sidebar with views and is subscribed columns in dashboard
country_sidebar = st.sidebar.selectbox('Countries:', country_select)

# Display bar graph with country views
fig = px.bar(continent_country, x='views', y='is_subscribed', color='country', orientation= 'h')
st.plotly_chart(fig)

# Give a Title
st.title('Aggregated Youtube Data for Video Titles')

# Add video title selection
video_title_sidebar = st.sidebar.selectbox('Video:', ('Views', 'Likes / Average watch time'))

# Create bar graph displaying views and total subscribers with likes for each video
if video_title_sidebar == 'Views':
    video_titles = tuple(agg_country_subs['video_title'].drop_duplicates())
    video_view = st.selectbox('Pick a video:', video_titles)
    videos_df = agg_country_subs.loc[agg_country_subs.video_title == video_view]
    fig = px.bar(videos_df, x='views', y='is_subscribed', color='country',
                 orientation='h')
    st.plotly_chart(fig)
elif video_title_sidebar == 'Likes / Average watch time':
    video_titles1 = tuple(agg_country_subs['video_title'].drop_duplicates())
    video_subs = st.selectbox('Pick a video:', video_titles1)
    video_df1 = agg_country_subs.loc[agg_country_subs.video_title == video_subs]
    fig = px.bar(video_df1, x='video_likes_added', y='average_watch_time', color='country',
                 orientation='v').update_layout(xaxis_rangeslider_visible=True,
                                                xaxis=dict(autorange=True))
    st.plotly_chart(fig)