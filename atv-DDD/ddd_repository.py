from cod_ddd import DDD

class DddRepository():
    def __init__(self) -> None:
        self.ddd_repository: list[DDD] = []
        
    def getDDD(self, cod: int) -> str:
        for d in self.ddd_repository:
            if(cod == d.cod):
              return d.cidade
        
    def append(self, ddd_repository: DDD) -> None:
        self.ddd_repository.append(ddd_repository)
        
    def checar_se_existe_o_ddd(self, cod: int) -> bool:
        for d in self.ddd_repository:
            if cod == d.cod:
                return True
            
        return False