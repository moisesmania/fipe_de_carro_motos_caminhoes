from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    marcas = []
    modelos = []
    anos = []

    tipo = request.form.get("tipo")
    marca = request.form.get("marca")
    modelo = request.form.get("modelo")
    ano = request.form.get("ano")

    # Carregar marcas se tipo selecionado
    if tipo:
        res = requests.get(f"https://parallelum.com.br/fipe/api/v1/{tipo}/marcas")
        if res.status_code == 200:
            marcas = res.json()

    # Carregar modelos se marca selecionada
    if tipo and marca:
        res = requests.get(f"https://parallelum.com.br/fipe/api/v1/{tipo}/marcas/{marca}/modelos")
        if res.status_code == 200:
            modelos = res.json().get("modelos", [])

    # Carregar anos se modelo selecionado
    if tipo and marca and modelo:
        res = requests.get(f"https://parallelum.com.br/fipe/api/v1/{tipo}/marcas/{marca}/modelos/{modelo}/anos")
        if res.status_code == 200:
            anos = res.json()

    # Consultar preço se ano selecionado
    if tipo and marca and modelo and ano:
        res = requests.get(f"https://parallelum.com.br/fipe/api/v1/{tipo}/marcas/{marca}/modelos/{modelo}/anos/{ano}")
        if res.status_code == 200:
            resultado = res.json()
        else:
            resultado = {"erro": "Não foi possível consultar o preço"}

    return render_template(
        "index.html",
        tipo=tipo,
        marca=marca,
        modelo=modelo,
        ano=ano,
        marcas=marcas,
        modelos=modelos,
        anos=anos,
        resultado=resultado
    )

if __name__ == "__main__":
    app.run(debug=True)
