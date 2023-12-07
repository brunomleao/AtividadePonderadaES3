import requests

class TestAPI():
    base_url = "http://127.0.0.1:8000"

    def GET_Usuarios(self):
        response = requests.get(f"{self.base_url}/usuarios")
        
        if response.status_code == 200:
            print("Teste de listagem de usuários: OK")
        else:
            print("Teste de listagem de usuários: Falhou")

    def POST_Usuario(self):
        response = requests.post(f"{self.base_url}/registrar-usuario", json={
    "nome": "Bruno Leao",
    "email": "usuariobrunoleao@email.com",
    "senha": "blabla"
})
            
        if response.status_code == 200:
            print("Teste de criação de usuário: OK")
        elif response.status_code == 400:
            print("Teste de criação de usuário: E-Mail já cadastrado, OK")
        else:
            print("Teste de criação de usuário: Falhou")

    def GET_Usuario(self):
        response = requests.get(f"{self.base_url}/usuarios/18")
        
        if response.status_code == 200:
            print("Teste de listagem de usuário: OK")
        else:
            print("Teste de listagem de usuário: Falhou")

    def PUT_Usuario(self):
        response = requests.put(f"{self.base_url}/usuarios/17", json={
    "nome": "Bruno Leao",
    "email": "bruno@gmail.com",
    })
        
        if response.status_code == 200:
            print("Teste de atualização de usuário: OK")
        else:
            print("Teste de atualização de usuário: Falhou")

    def DELETE_Usuario(self):
        response = requests.delete(f"{self.base_url}/usuarios/17")
        
        if response.status_code == 200:
            print("Teste de remoção de usuário: OK")
        else:
            print("Teste de remoção de usuário: Falhou")

    def LOGIN_Usuario(self):
        response = requests.post(f"{self.base_url}/login", data={
    "username": "bruno_leao02@hotmail.com",
    "password": "israel"
})
        
        if response.status_code == 200:
            print("Teste de login de usuário: OK")
        else:
            print("Teste de login de usuário: Falhou")

    def CRIAR_Historia(self):
        print("Teste de criação de história iniciado, aguarde...")
        response = requests.post(f"{self.base_url}/criar-historia", json={
    "titulo": "era uma vez a chapeuzinho vermelho",
    "descricao": "era uma vez a chapeuzinho",
    "categoria": "terror"
}, headers={"Authorization" : "Bearer 14"})
        
        if response.status_code == 200:
            print("Teste de criação de história: OK")
        else:
            print("Teste de criação de história: Falhou")

    def LISTAR_Historias(self):
        response = requests.get(f"{self.base_url}/historias")
        
        if response.status_code == 200:
            print("Teste de listagem de histórias: OK")
        else:
            print("Teste de listagem de histórias: Falhou")

    def LISTAR_Historia(self):
        response = requests.get(f"{self.base_url}/historias/2")
        
        if response.status_code == 200:
            print("Teste de listagem de história: OK")
        else:
            print("Teste de listagem de história: Falhou")

    def ATUALIZAR_Historia(self):
        response = requests.put(f"{self.base_url}/historias/1", json={
    "titulo": "era uma vez a chapeuzinho vermelho",
    "descricao": "era uma vez a chapeuzinho",
    "categoria": "terror"
})
        
        if response.status_code == 200:
            print("Teste de atualização de história: OK")
        else:
            print("Teste de atualização de história: Falhou")

    def DELETAR_Historia(self):
        response = requests.delete(f"{self.base_url}/historias/1")
        
        if response.status_code == 200:
            print("Teste de remoção de história: OK")
        else:
            print("Teste de remoção de história: Falhou")
    





test = TestAPI()
test.GET_Usuarios()
test.GET_Usuario()
test.POST_Usuario()
test.PUT_Usuario()
test.DELETE_Usuario()
test.LOGIN_Usuario()
test.CRIAR_Historia()
test.LISTAR_Historias()
test.LISTAR_Historia()
test.ATUALIZAR_Historia()
test.DELETAR_Historia()

    

# Executar os testes

