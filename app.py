from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello World!'


@app.route('/films/list')
def list_film_items():
    """
    Lists all films in a table
    :param stars: to filter by stars value
    :returns: renders html base.html template
    """
    stars = request.values.get("stars", "")

    film_reviews = get_film_reviews(filter_stars=stars)
    print(film_reviews)
    return render_template(
        'base.html', 
        headers=film_reviews[0].keys(),
        reviews=film_reviews,
    )


@app.route('/films/submit', methods=['POST'])
def submit_film_review():
    """
    Expects JSON form data like:
    {
        "film_name": "Film Name", 
        "stars": 4
    }

    Stores record in file film_reviews.txt
    """
    data = request.form

    print(data)

    with open('film_reviews.txt', 'a') as f:
        f.write(f"{data['film_name']}, {data['stars']}\n")
        print('Written review to file')


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
