from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        num1 = int(request.form.get("num1", 0))
        num2 = int(request.form.get("num2", 0))
        resultado = num1 + num2
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
