# BUilding url dynamially
#variable rule
# jinja 2 template engine

# jinga 2 template engine there are multiple ways 
# specifically to read the data source from the backend in the html page

# {{ }} expressions to print output in html
#{%...%} comditional statement or for loop
# {#...#} single line comments

from flask import Flask, render_template , request, redirect , url_for

app=Flask(__name__)

@app.route(rule='/')
def welcome():
    return '<html><H2>welcome to index page</H2></html>'


@app.route(rule='/index',methods=['GET'] )
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


    
@app.route('/submit-name', methods=['GET', 'POST'])
def submit_name():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

#variable rule
@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='PASSED'
    else:
        res='FAILED'
        
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=''
    if score>=50:
        res='PASSED'
    else:
        res='FAILED'
    
    exp={'score':score , 'res':res}
       
    return render_template('result1.html',results=exp)

@app.route('/successif/<int:score>')
def successif(score):
    res=''
        
    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    
    return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['data_science'])
        
        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres', score=total_score))

if __name__=='__main__':
    app.run(debug=True)