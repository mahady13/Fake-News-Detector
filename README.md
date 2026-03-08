Markdown
# 📰 Fake News Detector

A Machine Learning-based web application that classifies news articles as **Real** or **Fake**. This project utilizes Natural Language Processing (NLP) to analyze text patterns and provide accurate predictions.

🚀 **Live Demo:** [Click Here to View the App](https://fake-news-detector-mohiuddin-mahady.streamlit.app/)

---

## 🧐 Overview
In the era of information overload, misinformation spreads rapidly. This project aims to combat fake news by using a supervised machine learning model. It processes raw text, cleans it through an optimized NLP pipeline, and determines its authenticity.

## 🛠️ Tech Stack
- **Language:** Python 🐍
- **Machine Learning:** Scikit-learn (Random Forest/Multinomial NB)
- **NLP Library:** NLTK (Natural Language Toolkit)
- **Web Framework:** Streamlit
- **Data Handling:** Pandas & NumPy

## ⚡ Key Features & Optimizations
- **Advanced Preprocessing:** Implemented an efficient pipeline including:
  - Tokenization & Lowercasing
  - Stopword Removal (Optimized using `set` for $O(1)$ lookup speed)
  - Alphanumeric filtering
  - Porter Stemming for word root extraction
- **Vectorization:** Used **TfidfVectorizer** to transform text into meaningful numerical vectors.
- **Performance:** Optimized processing logic using **List Comprehensions** to handle thousands of rows efficiently.

## 📁 Project Structure
- `app.py`: The main Streamlit web application.
- `preprocess.py`: Contains the logic for text cleaning and processing.
- `model/`: Contains the trained `.pkl` model files (RFC & TF-IDF).
- `requirements.txt`: List of dependencies for cloud deployment.

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/mahady13/Fake-News-Detector.git](https://github.com/mahady13/Fake-News-Detector.git)
Create a virtual environment and install dependencies:

Bash
pip install -r requirements.txt
Run the Streamlit app:

Bash
streamlit run app.py
👤 Author
Mohiuddin Mahady Computer Science & Engineering Student

⭐ If you find this project helpful, feel free to give it a star!
