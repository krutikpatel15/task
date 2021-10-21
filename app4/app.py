from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about', methods=["GET", "POST"])
def about_us():
    if request.method=="POST":
        return "Thanks {} for registering".format(request.form.get('in_1'))
    return "This is about us page"

if __name__=="__main__":
    app.run(debug=True)
