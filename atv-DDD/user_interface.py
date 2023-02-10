from ddd_service import DddService

class UserInterface():
    def __init__(self, ddd_service: DddService) -> None:
        self.ddd_service = ddd_service
        
    def encontrar(self, cod: int) -> str:
        cidade = self.ddd_service.encontrarCidade(cod)
        
        if cidade == "None":
            return "DDD não encontrado"

        return f"O DDD informado é da cidade: {self.ddd_service.encontrarCidade(cod)}"