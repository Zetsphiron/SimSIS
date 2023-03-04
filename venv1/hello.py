from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def hello_world():
	if request.form.get("inputA") and request.form.get("inputB"):
		a=request.form.get("inputA")
		b=request.form.get("inputB")
		suma=str(int(a)+int(b))
	else:
		a=""
		b=""
		suma=""

	return render_template("index.html", a=a, b=b, suma=suma)

if __name__ == '__main__':
	app.run(debug=True)