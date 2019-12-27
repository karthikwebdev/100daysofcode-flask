from flask import *
#---------------------these are the methods for importing module----------------------------------------------
#import flask
#import flask as fk

app = Flask(__name__)
# app is the variable with Flask function in it this app has all power of whole app

@app.route('/')  
def home():
	return render_template('home.html')
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/gallery')
def gallery():
	return render_template('gallery.html')

# html file can be rendered using function render_template("")

if __name__ == '__main__':
	app.run(debug=True)
# this is used to run the application after any changes
# go to folder and press cmd on address bar to open cmd prompt
#run python file using command python index.py
#save html files in templates folder
