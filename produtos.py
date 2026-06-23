from conexao import conectar

def produtos_salvos(nome, quantidade):

    try:

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        INSERT INTO produtos
        (nome, quantidade)
        VALUES (%s, %s)
        """

        valores = (
            nome,
            quantidade
        )

        cursor.execute(sql, valores)

        conn.commit()

        print("Produto registrado")

    except Exception as erro:
        print("Erro:", erro)

    finally:

        cursor.close()
        conn.close()

#selecionar produtos
def listar_produtos():

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM produtos")

        dados = cursor.fetchall()

        return dados

    except Exception as erro:

        print("Erro: ", erro)

        return []

    finally:
        cursor.close()
        conn.close()

#deletar produto
def deletar_produto(id):

    try:

        conn = conectar()
        cursor = conn.cursor()

        sql = "DELETE FROM produtos WHERE id = %s"

        cursor.execute(sql, (id,))

        conn.commit()

        print("Produto removido!")

    except Exception as erro:

        print("Erro: ", erro)

    finally:
        cursor.close()
        conn.close()