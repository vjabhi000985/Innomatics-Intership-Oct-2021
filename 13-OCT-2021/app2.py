# Import the required library.
from flask import Flask

# Create a Flask object.
app = Flask(__name__)

reg_users = ['abhi','rohan','sachin','robin']

# To Creates the routes.
@app.route('/')
def home():
    return '<h1 style="color:green;">You are on Homepage.</h1>'

@app.route('/about_us')
def fun():
    return '<h1>You are in about us page.</h1>'

@app.route('/user/<user_name>')
def user_profile(user_name):
    if user_name in reg_users:
        return "Welcome{}".format(user_name)
    else:
    	return '<h1>User not found.</h1>'


# Run the application.
if __name__=='__main__':
    app.run()

