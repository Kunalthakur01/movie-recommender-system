# 🎬 Movie Recommender System

A Content-Based Movie Recommendation System built using Python, Pandas, Scikit-Learn, and Streamlit. The application recommends movies similar to the selected movie and displays their posters using the TMDB API.

## 🚀 Features

- Recommend 5 similar movies instantly
- Fetch movie posters using TMDB API
- Interactive Streamlit interface
- Content-Based Filtering
- Fast recommendations using precomputed similarity matrix

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- TMDB API
- Pickle

## 📂 Dataset

The project uses the TMDB 5000 Movies Dataset.

Files Used:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

## ⚙️ Project Workflow

### 1. Data Collection

Loaded:

- Movies Dataset
- Credits Dataset

### 2. Data Preprocessing

Merged both datasets and selected important features:

- Genres
- Keywords
- Cast
- Crew
- Overview

### 3. Feature Engineering

Created a combined tags column containing all important movie information.

### 4. Vectorization

Used CountVectorizer to convert text data into numerical vectors.

```
CountVectorizer(max_features=5000, stop_words='english')
```
5. Similarity Calculation

Calculated movie similarity using:

cosine_similarity()
6. Recommendation Generation

When a movie is selected:

Find its index
Retrieve similarity scores
Sort movies by similarity
Return Top 5 recommendations
📁 Project Structure
Movie-Recommender-System/
│
├── app.py
├── movies_dict.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
└── README.md
💻 Installation

Clone the repository:

git clone https://github.com/kunalthakur01/movie-recommender-system.git

Move to the project directory:

cd movie-recommender-system

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py
📸 Preview

Add screenshots of:

Home Page
Movie Recommendations

Example:

images/home.png
images/recommendation.png
🎯 Future Improvements
Hybrid Recommendation System
Movie Trailer Integration
Genre Filtering
User Accounts
Better UI Design
👨‍💻 Author

Kunal Singh

GitHub: https://github.com/Kunalthakur01

⭐ If you found this project useful, consider giving it a
