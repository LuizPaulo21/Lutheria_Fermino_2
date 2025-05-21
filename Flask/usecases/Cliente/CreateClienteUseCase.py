from repositories import clienteRepository #importando o repositório de cliente (interface)


class CreateClienteUseCase:
    def __init__(self, cliente_repository: clienteRepository):
        
        self.cliente_repository = cliente_repository

    def execute(self, cliente_data: dict) -> dict:

        try:
            # Cria novo cliente
            novo_cliente = self.cliente_repository.create_cliente(cliente_data)
            return novo_cliente
        except Exception as e:
            # Lida com exceções, como falha na criação do cliente
            print(f"Erro ao criar cliente: {e}")
            return None

