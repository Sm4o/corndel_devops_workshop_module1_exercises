import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--film-name', dest='film_name',
                    help='sum the integers (default: find the max)')
parser.add_argument('--stars', dest='stars', 
                    type=int,
                    choices=[1, 2, 3, 4, 5],
                    help='Any integer between 1 and 5')

args = parser.parse_args()


with open('film_reviews.txt', 'a') as f:
    f.write(f"{args.film_name}, {args.stars}\n")
    print('Written review to file')