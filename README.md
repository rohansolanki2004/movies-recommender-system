# 🎬 Movie Recommendation System

A personalized **Movie Recommendation System** built using **Python**, **Pandas**, and **Scikit-learn**.  
The system recommends movies similar to a user-selected movie by analyzing movie metadata and applying **machine learning–based similarity techniques**.

---

## 📌 Project Overview

This project demonstrates how data preprocessing and feature extraction can be combined with **content-based filtering** to generate relevant movie recommendations.

The model takes a movie name as input and returns a list of similar movies based on textual and numerical features extracted from the dataset.

---

## 🚀 Features

- 🔍 Accepts a movie title as user input  
- 🤖 Recommends similar movies using **cosine similarity**
- 🧹 Data preprocessing and cleaning for better accuracy
- 🧠 Feature extraction from movie metadata (genres, keywords, cast, crew, etc.)
- ⚡ Efficient and scalable recommendation pipeline

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Jupyter Notebook**

---

## 📂 Dataset

- TMDB 5000 Movies Dataset  
- TMDB 5000 Credits Dataset  

These datasets include information such as:
- Movie titles
- Genres
- Cast & crew
- Keywords
- Overview

---

## ⚙️ How It Works

1. **Data Loading**  
   Load movie and credits datasets using Pandas.

2. **Data Preprocessing**  
   - Merge datasets  
   - Handle missing values  
   - Extract and clean important features  

3. **Feature Engineering**  
   Combine relevant attributes into a single feature vector.

4. **Similarity Calculation**  
   Use **Cosine Similarity** to measure similarity between movies.

5. **Recommendation**  
   Given a movie name, return the top similar movies.

---

## ▶️ Usage

```python
recommend("Avatar")
