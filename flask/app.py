from flask import Flask

app=Flask(__name__)
# creates an instance of the Flask class
# which will be your WSGI  (WEB SERVER GATEWAY INTERFACE) application

@app.route(rule='/index')
# def welcome():
#     return 'welcome to my first flask page 92' 

def index():
    return 'welcome to index page'
if __name__=='__main__':
    app.run(debug=True)