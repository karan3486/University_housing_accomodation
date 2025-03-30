from abc import ABC, abstractmethod

class IRepository(ABC):
    
    @abstractmethod
    def save(self,obj: object) ->  bool: pass
    
    @abstractmethod
    def delete(self, id: int) -> bool: pass 

    @abstractmethod
    def update(self, old_obj:object , new_obj: object)->bool :pass  

    @abstractmethod
    def get_by_id(self, id: int) -> object: pass

    @abstractmethod
    def  get_all(self) -> object: pass