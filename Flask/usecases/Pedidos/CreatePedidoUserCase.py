class CreatePedidoUserCase:
    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository

    def execute(self, pedido):
        # Aquí puedes agregar la lógica de negocio necesaria antes de crear el pedido
        return self.pedido_repository.create(pedido)