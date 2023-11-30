import threading

class Token: #token que e passado entre os nos do anel
    def __init__(self, value):
        self.value = value

class Node(threading.Thread): #representa cada no do anel. Cada no e executado em uma thread separada e possui um identificador, um token e uma referencia para o proximo no no anel
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.token = None
        self.next_node = None

    def run(self): #verifica se possui o token. Se possuir, entra na secao critica e imprime uma mensagem. Caso contrario, passa o token para o proximo no
        while True:
            if self.token is not None:
                if self.token.value == self.id:
                    print(f"Nodo {self.id} na secao critica com {self.token}\n")
                    self.token = None
                    print(f"Nodo {self.id} agora com {self.token}\n")
                else:
                    self.pass_token()
            #else:
            #    self.receive_token(self.next_node.token)

    def pass_token(self): #passa o token para o proximo no
        self.next_node.receive_token(self.token)
        print(f"Seguiu para o proximo {self.next_node.id} com token: \n", self.token)
        self.token = None

    def receive_token(self, token): #recebe o token de um no anterior
        if token is not None:
            self.token = token
            print("Recebeu token: \n", token)

    def set_next_node(self, next_node): #seta para o proximo nodo
        self.next_node = next_node
        print("Proximo: \n", next_node)

def main(): #sao criados os nos e configuradas as referencias para o proximo no. Em seguida, cada no e iniciado em uma thread separada
    num_nodes = 7
    nodes = []

    for i in range(num_nodes):
        #next_node = nodes[i].set_next_node(nodes[(i + 1) % num_nodes])
        node = Node(i)
        nodes.append(node)

    for i in range(num_nodes):
            nodes[i].set_next_node(nodes[(i + 1) % num_nodes])


    for node in nodes:
        node.token = Token(node.id) # define o token inicial para cada no
        threading.Thread(target=node.run).start()

if __name__ == "__main__":
    main()