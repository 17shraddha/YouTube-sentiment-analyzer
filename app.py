import streamlit as st
from gensim import corpora
from gensim.models import LdaModel
import google.generativeai as genai
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from scraping_comments import scraper
from preprocessing_app import clean_with_timestamp, get_sentiment, preprocess_text, print_topics, generate_summary
import requests
from collections import Counter

# Configure the Streamlit page
st.set_page_config(
    page_title="YouTube Comments Sentiment Analyzer",
    page_icon="🎬",
    layout="wide"
)

# Function to set background image
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1540397521216-0b56cdc2f177?q=80&w=1973&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Access the YouTube API key from secrets
youtube_api = st.secrets['YOUTUBE_API_KEY']
gemini_api = st.secrets['GEMINI_API_KEY']

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def get_video_info(video_url, api_key):
    video_id = video_url.split('v=')[1]
    if not video_id:
        return "Invalid video URL or ID could not be extracted"
    url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=snippet&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            channel_name = data['items'][0]['snippet']['channelTitle']
            video_title = data['items'][0]['snippet']['title']
            return {"channel_name": channel_name, "video_title": video_title}
        else:
            return "Video not found"
    else:
        return f"Error: {response.status_code}"

@st.cache_data
def cached_scraper(youtube_api, video_url):
    return scraper(youtube_api, video_url)

def create_countplot(df):
    fig, ax = plt.subplots()
    sns.countplot(x='sentiment', data=df, ax=ax, order=['Positive','Neutral','Negative'], palette={'Positive': 'green', 'Neutral': 'gray', 'Negative': 'red'})
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge')
    ax.set_title('Countplot of Categories')
    st.pyplot(fig)

def get_word_cloud(df, sentiment):
    sentiment = sentiment.lower()
    if sentiment in ('positive', 'negative', 'neutral'):
        data = df[df['sentiment'].str.lower().str.contains(sentiment)]['english_comm']
    else:
        data = df['english_comm']
    text = ' '.join(data.dropna().astype(str))
    wordcloud = WordCloud(width=1920, height=1080, background_color="white", max_words=50).generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

def get_bar_chart(df, sentiment):
    if sentiment.lower() in ('positive', 'negative', 'neutral'):
        data = df[df['sentiment'] == sentiment]['english_comm']
    else:
        data = df['english_comm']
    all_words = []
    data.apply(lambda x: all_words.extend(preprocess_text(x)))
    word_counts = Counter(all_words)
    most_common_words = word_counts.most_common(15)
    words, counts = zip(*most_common_words)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.barh(words, counts, color='skyblue')
    ax.set_xlabel("Frequency", fontsize=12)
    ax.set_ylabel("Words", fontsize=12)
    ax.set_title("Top 15 most frequent keywords", fontsize=14)
    plt.gca().invert_yaxis()
    st.pyplot(fig)

def comments_trend_plot(df, sentiment):
    sentiment = sentiment.lower()
    if sentiment in ('positive', 'negative', 'neutral'):
        data = df[df['sentiment'].str.lower().str.contains(sentiment)]['hour']
    else:
        data = df['hour']
    fig, ax = plt.subplots(figsize=(10, 5))
    n, bins, patches = ax.hist(data, bins=24, range=(0, 25), edgecolor='black')
    ax.set_title(f'Comments Trend by Hour ({sentiment.capitalize()})')
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Number of Comments')
    ax.set_xticks(range(0, 25))
    for i in range(len(patches)):
        height = patches[i].get_height()
        ax.text(patches[i].get_x() + patches[i].get_width() / 2, height, str(int(height)), ha='center', va='bottom', fontsize=10)
    st.pyplot(fig)

def home_page():
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/75/YouTube_social_white_squircle_%282017%29.svg", width=100)
    st.title("🎬 YouTube Comments Sentiment Analyzer")
    st.markdown("Developed by Shraddha Chauhan ")
    st.markdown("Analyze viewer sentiment, trends, word clouds, and much more.")
    if st.button("🚀 Let's Exploring the Sentiment "):
        st.session_state.page = 'main'

def main_page():
    st.header("🔍 Analyze YouTube Video Comments")
    if st.sidebar.button("⬅️ Go to Home"):
        st.session_state.page = 'home'
        return

    video_url = st.text_input("🎥 Enter YouTube Video URL", help="Paste the full YouTube video link here")
    df = None

    if video_url:
        try:
            df = cached_scraper(youtube_api, video_url)
            df['sentiment'] = df['english_comm'].apply(get_sentiment)
            st.session_state.df = df
            genai.configure(api_key=gemini_api)
            st.success("✅ Comments fetched and processed successfully!")
            video_info = get_video_info(video_url, youtube_api)
            if isinstance(video_info, dict):
                st.subheader(f"📺 Channel: {video_info['channel_name']}")
                st.subheader(f"🎞️ Title: {video_info['video_title']}")
            else:
                st.error(video_info)
        except Exception as e:
            st.error(f"❌ Error fetching data: {e}")
    else:
        st.info('ℹ️ Please enter a YouTube video URL to begin analysis.')

    if df is not None:
        section = st.sidebar.radio("🧭 Navigate Sections", 
                                   ['Summary', 'Sentiment Distribution', 'Comment Trends', 'Word Cloud', 'Frequent Words'])

        if section == 'Summary':
            st.header("📋 Summary of Comments")
            st.markdown(generate_summary(df))

        elif section == 'Sentiment Distribution':
            st.header("📊 Sentiment Distribution")
            col1, col2, col3 = st.columns(3)
            col1.metric("👍 Positive", len(df[df['sentiment'] == 'Positive']))
            col2.metric("😐 Neutral", len(df[df['sentiment'] == 'Neutral']))
            col3.metric("👎 Negative", len(df[df['sentiment'] == 'Negative']))
            create_countplot(df)

        elif section == 'Comment Trends':
            st.header("📈 Comment Posting Trends by Hour")
            trend_sentiment = st.selectbox("Filter by Sentiment", ['All', 'Positive', 'Neutral', 'Negative'])
            comments_trend_plot(df, '' if trend_sentiment == 'All' else trend_sentiment)

        elif section == 'Word Cloud':
            st.header("☁️ Word Cloud")
            word_cloud_sentiment = st.selectbox("Filter by Sentiment", ['All', 'Positive', 'Neutral', 'Negative'])
            get_word_cloud(df, '' if word_cloud_sentiment == 'All' else word_cloud_sentiment)

        elif section == 'Frequent Words':
            st.header("🔤 Frequent Keywords in Comments")
            freq_keyword_sentiment = st.selectbox("Filter by Sentiment", ['All', 'Positive', 'Neutral', 'Negative'])
            get_bar_chart(df, '' if freq_keyword_sentiment == 'All' else freq_keyword_sentiment)

def app():
    set_background()
    if st.session_state.page == 'home':
        home_page()
    elif st.session_state.page == 'main':
        main_page()

if __name__ == "__main__":
    app()
