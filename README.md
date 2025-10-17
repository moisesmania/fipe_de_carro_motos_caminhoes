# Consulta FIPE - Flask

Aplicação web em **Flask** que permite consultar veículos na **tabela FIPE**, selecionando **tipo → marca → modelo → ano**, mostrando o preço do veículo.

---

## Estrutura do projeto

flask_loja_fipe/
├── app.py
├── requirements.txt
└── templates/
└── index.html

yaml
Copiar código

---

## Pré-requisitos

- Python 3.11 ou superior
- Pip (gerenciador de pacotes Python)
- VS Code (ou outro editor de sua preferência)
- Acesso à internet (para consultar a API FIPE)

---

## Passo a passo para rodar o projeto

### 1. Clonar o repositório

No terminal, execute:

```bash
git clone https://github.com/seu-usuario/flask_loja_fipe.git
cd flask_loja_fipe
Substitua seu-usuario pelo seu usuário no GitHub.

2. Criar e ativar o ambiente virtual
No Windows:

bash
Copiar código
python -m venv venv
venv\Scripts\activate
No Linux/Mac:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
3. Instalar as dependências
bash
Copiar código
pip install -r requirements.txt
Isso vai instalar o Flask e o requests, necessários para rodar a aplicação.

4. Rodar a aplicação
bash
Copiar código
python app.py
A aplicação estará disponível em http://127.0.0.1:5000/

Abrir no navegador e acessar o formulário para consulta FIPE

5. Como usar
Selecione o tipo de veículo (Carros, Motos, Caminhões)

Escolha a marca

Escolha o modelo

Escolha o ano

O preço e demais informações serão exibidos abaixo do formulário

6. Estrutura de arquivos
app.py: arquivo principal da aplicação Flask

requirements.txt: lista de dependências

templates/index.html: front-end com formulário e resultado

7. Como contribuir
Faça um fork do repositório

Crie uma branch para suas alterações:

bash
Copiar código
git checkout -b minha-feature
Faça as alterações e teste localmente

Faça um commit:

bash
Copiar código
git add .
git commit -m "Descrição da mudança"
Faça push para sua branch:

bash
Copiar código
git push origin minha-feature
Abra um Pull Request no repositório original

8. Licença
Este projeto é open source, sinta-se livre para usar e modificar conforme necessário.

9. Links úteis
API FIPE: https://deividfortuna.github.io/fipe/v2/

yaml
Copiar código

