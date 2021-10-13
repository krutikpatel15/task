# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return("It's Home Page")

# if __name__== "__main__":
#     app.run()

n=input()
print(type(n))
print(n)
m=list()
m.append(n[0])
x=n[0]
for i in range(1,len(n)):
    x+=n[i]
    m.append(x)
print(m)