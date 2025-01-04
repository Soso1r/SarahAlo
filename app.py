from flask import Flask, render_template

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/destinations')
def destinations():
    return render_template('destinations.html')

@app.route('/itinerary')
def itinerary():
    return render_template('itinerary.html')

@app.route('/real_time_updates')
def real_time_updates():
    return render_template('real_time_updates.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/accommodations')
def accommodations():
    return render_template('accommodations.html')

@app.route('/offline_access')
def offline_access():
    return render_template('offline_access.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
