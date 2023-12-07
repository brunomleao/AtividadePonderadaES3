from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    email: str
    senha: str

class UsuarioBasico(BaseModel):
    email: str
    nome: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Login(BaseModel):
    email: str
    senha: str

class Historia(BaseModel):
    titulo: str
    descricao: str
    categoria: str
