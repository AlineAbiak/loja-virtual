from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="senai",
        database="bdprodutos"
    )

@app.route("/produtos/cadastrar", methods=["GET", "POST"])
def cadastrarProduto():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        preco = request.form["preco"]
        fabricante = request.form["fabricante"]

        try:
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
                INSERT INTO tbprodutos (NOME, DESCRICAO, PRECO, FABRICANTE)
                VALUES (%s, %s, %s, %s)
            """

            valores = (nome, descricao, preco, fabricante)

            cursor.execute(sql, valores)
            conn.commit()
            conn.close()

            return """
            <script>
                alert('Produto cadastrado com sucesso!');
                window.location.href = '/produtos/cadastrar';
            </script>
        """
        except Exception as e:
            return f"""
                <script>
                    alert('Erro ao cadastrar o produto: {e}');
                    window.location.href = '/produtos/cadastrar';
                </script>
            """    
    else:
        return render_template("produtos/cadastrar.html")

if __name__ == "__main__":
    app.run(debug=True)
