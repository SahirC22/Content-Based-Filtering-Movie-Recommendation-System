

#  Content-Based Movie Recommendation System

A simple yet powerful content-based movie recommendation system that suggests movies similar to a selected title by analyzing metadata like overviews, genres, keywords, and cast. Built using Python, machine learning techniques, and deployed via Streamlit.

---


## 📌 Features

-  Content-based filtering using TF-IDF & cosine similarity
-  Movie metadata analysis (overview, genre, cast, keywords)
-  High-quality movie posters fetched dynamically using OMDB API
-  Lightweight, fast, and responsive UI via Streamlit
-  Works without user history – solves the cold start problem
-  Easily deployable as a web app

---

##  How It Works

1. User selects a movie from the list.
2. The system extracts its feature vector using TF-IDF (on metadata).
3. Cosine similarity is computed against all other movies.
4. Top similar movies are ranked and displayed with posters via OMDB.

---

##  Tech Stack

| Category | Tools / Libraries |
|----------|-------------------|
| Language | Python |
| Frontend | Streamlit |
| ML Libraries | scikit-learn, pandas |
| APIs | OMDB API |
| Utilities | pickle, requests |


---

##  Requirements

Install dependencies using pip:

bash
pip install -r requirements.txt

Dependencies include:
	•	streamlit
	•	pandas
	•	scikit-learn
	•	requests


 ##  Run Locally

 
1.	Clone the repository:

- git clone ( https://github.com/SahirC22/Content-Based-Filtering-Movie-Recommendation-System.git )

- cd Content-Based-Filtering-Movie-Recommendation-System

2.	Start the Streamlit app:

- streamlit run mapp.py

3.	Open in your browser: 
 
- http://localhost:8501


##  OMDB API Key Setup

	•	Get your free API key: https://www.omdbapi.com/apikey.aspx
	•	Add it to a .env file or directly in the code (for testing only):

API_KEY = "your_omdb_api_key"



⸻

##  Datasets Used

- https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
- credits.csv 
- keywords.csv
	
These can be sourced from: The Movie Dataset (TMDb) on Kaggle


✅ Advantages

	•	Doesn’t rely on user history (great for new users)
 
	•	No collaborative filtering required
 
	•	Fast response time due to preprocessed models

❌ Limitations

	•	Can’t adapt to evolving user tastes over time
 
	•	Limited by available metadata (cold start for new movies)
 
	•	Less effective for highly subjective preferences


**System Architecture**

``[User] → [Streamlit UI] → [Recommendation Engine] → [Similarity Calculator]
                                     ↓
                               [OMDB API]
                                     ↓
                             [Display Results]``


# *License*

This project is open-source under the MIT License.


# *Contributions*

Pull requests are welcome! If you’d like to contribute:

	1.	Fork the repo
 
	2.	Create a new branch (git checkout -b feature-xyz)
 
	3.	Commit your changes
 
	4.	Push to the branch (git push origin feature-xyz)
 
	5.	Open a Pull Request



# *Contact*

For queries, suggestions, or collaboration:

**Abdus Sahir Choudhury**

📫 Email: rajsahir001@gmail.com

🌐 Portfolio: https://sahirportfolio.carrd.co

