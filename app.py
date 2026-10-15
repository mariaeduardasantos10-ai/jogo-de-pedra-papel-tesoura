import random
from flask import Flask, render_template, request

app = Flask(__name__)

OPCOES = ["pedra", "papel", "tesoura"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/jogar", methods=["POST"])
def jogar():
    # Obtém a escolha enviada pelo formulário do HTML
    jogador = request.form.get("escolha")
    computador = random.choice(OPCOES)

    # Lógica de vitória / empate / derrota
    if jogador == computador:
        resultado = "Empate! 🤝"
    elif (
        (jogador == "pedra" and computador == "tesoura")
        or (jogador == "tesoura" and computador == "papel")
        or (jogador == "papel" and computador == "pedra")
    ):
        resultado = "Você Venceu! 🎉✨"
    else:
        resultado = "O Computador Venceu! 🤖"

    return render_template(
        "index.html",
        resultado=resultado,
        jogador=jogador.capitalize() if jogador else "",
        computador=computador.capitalize(),
    )

if __name__ == "__main__":
    print("Servidor rodando! Acesse o jogo em: http://127.0.0.1:5000")
    app.run(debug=True)