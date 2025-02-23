# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Bolin Wu**

---

## Dataset
From Kaggle dataset: IMDB Movies Dataset, Top 1000 Movies by IMDB Rating
https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows

The dataset contains 1000 data. 500 samples were randomly sampled and stored in data/movie_500.csv used for recommendation.

## Setup
Docker is used. If not installed, see https://docs.docker.com/engine/install/. 

Run the following command in the directory of `Dockerfile`.

`docker build -t movie-recommender .`

## Running
Run the following command in the directory of `Dockerfile`.

`docker run --rm movie-recommender "<your-description>"`

## Results
Sample results from `docker run --rm movie-recommender "I like action movies set in space"`:

Top Recommendations:
1. Aliens
2. The Man Who Would Be King
3. Ghostbusters
4. Clerks
5. Blade Runner

## Video Demo
See `demo.md`.