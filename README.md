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

Some Glimpse of my project 
<img width="1907" height="877" alt="Picture1" src="https://github.com/user-attachments/assets/6f234c75-a435-4edc-9cd5-86d7b48c893d" />
<img width="1906" height="872" alt="picture8" src="https://github.com/user-attachments/assets/9582b75f-6f64-4e37-a6d7-8ccb742a5e7a" />
<img width="1916" height="872" alt="picture7" src="https://github.com/user-attachments/assets/ac70da73-4bdd-46f1-9c63-4d070b31c011" />
<img width="1906" height="882" alt="picture6" src="https://github.com/user-attachments/assets/8df7a374-478f-4c2a-9ce7-6bfa97ca60b3" />
<img width="1918" height="872" alt="Picture5" src="https://github.com/user-attachments/assets/95295d75-49c5-49a4-856c-88a48c077a56" />
<img width="1910" height="872" alt="picture4" src="https://github.com/user-attachments/assets/cb171078-31e0-49bb-a8af-de2943735910" />
<img width="1897" height="872" alt="Picture3" src="https://github.com/user-attachments/assets/2b03c5d3-c141-4a4c-87d5-3c39c06f05e6" />
<img width="1903" height="875" alt="Picture2" src="https://github.com/user-attachments/assets/67218615-7333-49df-b42a-18b0e25f6a89" />

