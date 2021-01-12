from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello World!'


@app.route('/films/list')
def list_film_items():
    stars = request.values.get("stars", "")

    film_reviews = get_film_reviews(filter_stars=stars)
    print(film_reviews)
    return render_template(
        'base.html', 
        headers=film_reviews[0].keys(),
        reviews=film_reviews,
    )


def get_film_reviews(filter_stars=None):
    film_reviews_list = [] 
    with open('film_reviews.txt', 'r') as f:
        film_reviews = f.read().splitlines()

        for review in film_reviews:
            film_name = review.split(', ')[0]
            film_stars = review.split(', ')[1]
            if filter_stars and film_stars != filter_stars: 
                pass
            else:
                film_reviews_list.append({
                    'film': film_name,
                    'stars': film_stars, 
                })

    return film_reviews_list
