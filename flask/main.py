from flask import Flask, render_template

app=Flask(__name__)

@app.route(rule='/')
def welcome():
    return '<html><H2>welcome to index page</H2></html>'


@app.route(rule='/index' )
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
if __name__=='__main__':
    app.run(debug=True)