from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/progress", methods=["GET"])
def get_progress():
	return jsonify(f"reply from endpoint get_progress")

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)