# Import the required library.
from flask import Flask

# Create a Flask object.
app = Flask(__name__)

# To Creates the routes.
@app.route('/')
def home():
    return '<h1 style="color:green;">You are on Homepage.</h1>'

# Run the application.
if __name__=='__main__':
    app.run()

