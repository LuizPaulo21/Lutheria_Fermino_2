class CreatePedidoUseCase:
    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository

    def execute(self, pedido):
        return self.pedido_repository.create(pedido)