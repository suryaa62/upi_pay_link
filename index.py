import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
	return flask.render_template("index.html")

@app.route("/<amount>")
def indexWithAmount(amount):
	return flask.render_template("index.html" , amount=amount)

@app.route("/test")
def test():
	return flask.redirect('upi://pay?pa=7828369492@ybl&amp;pn=Suryakant Agrawal&amp;cu=INR')

if (__name__ == '__main__' ) :
	app.run(debug=True)

