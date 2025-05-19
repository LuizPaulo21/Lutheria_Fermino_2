class DeleteProdutoUseCase:
    def __init__(self, produtoRepository):
        self.produtoRepository = produtoRepository

    def execute(self, id):
        return self.produtoRepository.delete(id)