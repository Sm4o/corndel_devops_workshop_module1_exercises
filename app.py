from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello World!'


@app.route('/films/list')
def list_film_items():
    film_reviews = get_film_reviews()
    print(film_reviews)
    return render_template(
        'base.html', 
        headers=film_reviews[0].keys(),
        reviews=film_reviews,
    )


def get_film_reviews():
    film_reviews_list = [] 
    with open('film_reviews.txt', 'r') as f:
        film_reviews = f.read().splitlines()

        for review in film_reviews:
            film_reviews_list.append({
                'film': review.split(', ')[0], 
                'stars': review.split(', ')[1],
            })

    return film_reviews_list
