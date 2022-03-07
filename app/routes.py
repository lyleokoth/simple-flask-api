from app import app
from flask import jsonify

#an a array that will hodl for books.
books = [
    {
        "id": 1,
        "title": "CS50",
        "description": "Intro to CS and art of programming!",
        "author": "Havard",
        "borrowed": False
    },
    {
        "id": 2,
        "title": "Python 101",
        "description": "little python code book.",
        "author": "Will",
        "borrowed": False
    }
]

#The default root
@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def index():
    """
    Shows the index/home page

    Called whenever a GET request is made to the / or /api route

    Parameters
    ----------
    None

    Raises
    ------
    None

    Returns
    -------
    reply: str
        A string description of the api!
    """

    reply = 'Welcome to the books API!'
    return reply

#The route to access all books
@app.route('/api/books', methods=['GET'])
def all_books():
    """
    Returns all the books in our database

    Called whenever a GET request is made to the /api/books route

    Parameters
    ----------
    None

    Raises
    ------
    None

    Returns
    -------
    books: json
        A list of all the books in our database
    """

    return jsonify(books)
