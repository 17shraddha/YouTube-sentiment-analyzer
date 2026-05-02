# 🎬 YouTube Comments Sentiment Analyzer

🔗 **GitHub Repository**
https://github.com/17shraddha/YouTube-sentiment-analyzer

---

## 📌 Project Description

This project is a **Streamlit-based web application** that analyzes YouTube video comments.
It extracts comments using the YouTube Data API, performs **sentiment analysis**, and visualizes the results using graphs and NLP techniques.

The application helps in understanding audience opinions by classifying comments into:

* Positive 😊
* Neutral 😐
* Negative 😡

---

## 🚀 Features

* 🔗 **YouTube Data Extraction**
  Fetch comments using YouTube Data API

* 🧠 **Sentiment Analysis**
  Classifies comments into Positive, Neutral, and Negative

* 📊 **Sentiment Distribution**
  Visual count plot of sentiment categories

* 📈 **Comment Trend Analysis**
  Shows comment activity by hour

* ☁️ **Word Cloud**
  Displays most frequent words visually

* 🔤 **Frequent Keywords**
  Bar chart of top words in comments

* 🧾 **Summary Generation**
  Generates insights from comments

* 🧩 **Topic Modeling (LDA)**
  Extracts topics from comments

* 🤖 **Gemini API Integration**
  Interprets topics using AI

---

## 📸 Project Preview

### 🏠 Home Page

![Home](images/home.png)

### 📊 Sentiment Analysis

![Sentiment](images/sentiment.png)

### ☁️ Word Cloud

![Word Cloud](images/wordcloud.png)

### 📈 Comment Trends

![Trend](images/trend.png)

---

## 🛠️ Tech Stack

* **Frontend/UI**: Streamlit
* **Backend**: Python

**Libraries Used:**

* NLTK
* TextBlob
* Gensim
* Matplotlib
* Seaborn
* WordCloud

**APIs Used:**

* YouTube Data API
* Gemini API

---

## ⚙️ Project Workflow

1. User enters YouTube video URL
2. Comments are fetched using YouTube API
3. Text is cleaned and preprocessed
4. Sentiment analysis is applied
5. Data is visualized using graphs
6. Word cloud and keyword extraction is performed
7. LDA model extracts topics
8. Gemini API interprets topics

---

## 🧪 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/17shraddha/YouTube-sentiment-analyzer
cd YouTube-sentiment-analyzer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add API Keys

Create a folder `.streamlit/` and inside it create a file `secrets.toml`:

```toml
YOUTUBE_API_KEY = "your_api_key"
GEMINI_API_KEY = "your_api_key"
```

### 6. Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
YouTube-sentiment-analyzer/
│── app.py
│── scraping_comments.py
│── preprocessing_app.py
│── requirements.txt
│── README.md
│── .gitignore
│── images/
│── .streamlit/
```

---

## 👩‍💻 Author

**Shraddha Chauhan**

---

## 🎯 Future Scope

* Deploy as live web application
* Add real-time analytics
* Improve NLP model accuracy
* Add multilingual support
