from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        print(request.form)
        name = request.form['name']
        email = request.form.get('email')
        print(name,email)
        return render_template('kc.html',course=email)
    name = "python"
    l = [10,20,30,40]
    results = "average"
    return render_template('kc.html',course=name,
                           marks=l,results=results)

if __name__=="__main__":
    app.run(debug=True)





