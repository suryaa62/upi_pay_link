import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
	return flask.render_template("index.html")

@app.route("/<amount>")
def indexWithAmount(amount):
	return flask.render_template("index.html" , amount=amount)

if (__name__ == '__main__' ) :
	app.run(debug=True)

