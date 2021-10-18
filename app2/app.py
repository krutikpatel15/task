# Step 1 : Import
from flask import Flask

# Step 2 : Onject of Flask class
app = Flask(__name__)

# Data
reg_users = ["krutik","bhagyesh","manas"]

# Step 3 : Define the routes and bnd them to some logic
@app.route('/')
def home():
    return("Welcome to home page")

@app.route('/about_us')
def about():
    return("This is about us page")

@app.route('/user/<user_name>')
def user_profile(user_name):
    if user_name in reg_users:
        return("Welcome {}".format(user_name))
    else:
        return("User not found. Kindly register.")

# Step 4 : Start the application
if __name__=="__main__":
    app.run(debug=True)
