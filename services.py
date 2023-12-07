from fastapi import HTTPException
from db.db import get_database_connection
from models import Usuario, UsuarioBasico
import mysql
import bcrypt

def autenticar_usuario(email: str, senha: str):
    mydb = get_database_connection()
    cursor = mydb.cursor()
    query = "SELECT * FROM usuarios WHERE email = %s"

    with mydb.cursor() as cursor:
        cursor.execute(query, (email,))
        user = cursor.fetchone()

    if not user or not bcrypt.checkpw(senha.encode('utf-8'), user[3].encode('utf-8')):
        return False
    return user

def registrar_usuario(usuario: Usuario):
    mydb = get_database_connection()
    nome_usuario = usuario.nome
    email_usuario = usuario.email
    senha_usuario = usuario.senha

    hashed_password = bcrypt.hashpw(senha_usuario.encode('utf-8'), bcrypt.gensalt())

    cursor = mydb.cursor()
    sql = "INSERT INTO usuarios (nome, email, senha_hash) VALUES (%s, %s, %s)"
    val = (nome_usuario, email_usuario, hashed_password.decode('utf-8'))
    
    try:
        cursor.execute(sql, val)
        mydb.commit()
        cursor.close()
    except mysql.connector.IntegrityError as e:
        if e.errno == 1062:  # Código de erro para chave duplicada
            raise HTTPException(status_code=400, detail="Email já cadastrado")
        else:
            raise HTTPException(status_code=500, detail="Erro interno no servidor")

    return {"message": f"Usuário {nome_usuario} registrado com sucesso! Email: {email_usuario}"}

def retornar_usuario_por_id(id_usuario: int):
    mydb = get_database_connection()
    connection = mydb
    cursor = connection.cursor()

    query = "SELECT * FROM sys.usuarios WHERE id_usuario = %s"
    values = (id_usuario,)

    with mydb.cursor() as cursor:
        cursor.execute(query, values)
        user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return {"id": user[0], "username": user[1], "email": user[2]}

def retornar_usuarios():
    mydb = get_database_connection()
    connection = mydb
    cursor = connection.cursor()

    query = "SELECT * FROM sys.usuarios"

    with mydb.cursor() as cursor:
        cursor.execute(query)
        users = cursor.fetchall()

    if not users:
        raise HTTPException(status_code=404, detail="Nenhum usuário encontrado")
    
    return users

def atualizar_usuario(id_usuario: int, usuario: UsuarioBasico):
    mydb = get_database_connection()
    connection = mydb
    cursor = connection.cursor()

    query = "UPDATE sys.usuarios SET nome = %s, email = %s WHERE id_usuario = %s"
    values = (usuario.nome, usuario.email, id_usuario)

    with mydb.cursor() as cursor:
        cursor.execute(query, values)
        mydb.commit()

    return {"message": "Informações do usuário atualizadas com sucesso"}

def deletar_usuario(id_usuario: int):
    mydb = get_database_connection()
    connection = mydb
    cursor = connection.cursor()

    query = "DELETE FROM sys.usuarios WHERE id_usuario = %s"
    values = (id_usuario,)

    with mydb.cursor() as cursor:
        cursor.execute(query, values)
        mydb.commit()

    return {"message": "Usuário deletado com sucesso"}

def registrar_historia(historia_input, historia_gpt):
    mydb = get_database_connection()
    connection = mydb
    cursor = connection.cursor()

    query = "INSERT INTO sys.historias (titulo, descricao_input, descricao_gpt, categoria) VALUES (%s, %s, %s, %s)"
    values = (historia_input.titulo, historia_input.descricao, historia_gpt ,historia_input.categoria)

    with mydb.cursor() as cursor:
        cursor.execute(query, values)
        mydb.commit()

    return {"message": "História registrada com sucesso"}

def retornar_historias():
    mydb = get_database_connection()
    connection = mydb
    cursor = connection.cursor()

    query = "SELECT * FROM sys.historias"

    with mydb.cursor() as cursor:
        cursor.execute(query)
        historias = cursor.fetchall()

    if not historias:
        raise HTTPException(status_code=404, detail="Nenhuma história encontrada")
    
    return historias

def retornar_historia_por_id(id_historia: int):
    mydb = get_database_connection()
    connection = mydb
    cursor = connection.cursor()

    query = "SELECT * FROM sys.historias WHERE id_historia = %s"
    values = (id_historia,)

    with mydb.cursor() as cursor:
        cursor.execute(query, values)
        historia = cursor.fetchone()

    if not historia:
        raise HTTPException(status_code=404, detail="História não encontrada")
    
    return historia

def atualizar_historia(id_historia: int, historia_input):
    mydb = get_database_connection()
    connection = mydb
    cursor = connection.cursor()

    query = "UPDATE sys.historias SET titulo = %s, descricao_input = %s, categoria = %s WHERE id_historia = %s"

    values = (historia_input.titulo, historia_input.descricao, historia_input.categoria, id_historia)

    with mydb.cursor() as cursor:
        cursor.execute(query, values)
        mydb.commit()

    return {"message": "Informações da história atualizadas com sucesso"}

def deletar_historia(id_historia: int):
    mydb = get_database_connection()
    connection = mydb
    cursor = connection.cursor()

    query = "DELETE FROM sys.historias WHERE id_historia = %s"
    values = (id_historia,)

    with mydb.cursor() as cursor:
        cursor.execute(query, values)
        mydb.commit()

    return {"message": "História deletada com sucesso"}

