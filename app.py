from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    mensagem = ""
    if request.method == "POST":
        nota1 = float(request.form.get("nota1", 0))
        nota2 = float(request.form.get("nota2", 0))
        resultado = (nota1 + nota2)/2
        
        if resultado >= 7 :
            mensagem = "Parabens você passou!"
        else:
            mensagem = "te vejo na final!"
    
    return render_template("index.html", resultado=resultado, mensagem = mensagem)

if __name__ == "__main__":
    app.run(debug=True)
