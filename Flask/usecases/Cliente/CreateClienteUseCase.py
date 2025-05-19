
class CreateClienteUseCase:
    def __init__(self, cliente_repository):
        self.cliente_repository = cliente_repository

    def execute(self, cliente_data):
        # Validação de dados
        if not cliente_data.get('name'):
            raise ValueError("Name is required")
        if not cliente_data.get('email'):
            raise ValueError("Email is required")

        # Cria novo cliente
        new_cliente = self.cliente_repository.create(cliente_data)
        return new_cliente