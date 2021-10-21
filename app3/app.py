from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
# def fun1():
#     return "This is response from GET request"

# @app.route('/', methods=['POSt'])
# def fun2():
#     return "This is response from POST request"

@app.route('/', methods=['GET','POST'])
def fun():
    if request.method=='POST':
        return "This is response from POST request"
    return "This is response from GET request"

if __name__=="__main__":
    app.run(debug=True)
