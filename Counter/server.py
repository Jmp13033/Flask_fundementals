
from flask import Flask, url_for,redirect, render_template, request, session # Import Flask to allow us to create our app
app = Flask(__name__)
app.secret_key ="yourkey" 

@app.route("/")
def server():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1 
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    if "counter" in session:
        session["counter"] += 2
    else:
        session["counter"] = 0
    return render_template("index.html")



app.route
@app.route("/del")
def delete():
    session.clear()
    return redirect("/") 

    

    

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.