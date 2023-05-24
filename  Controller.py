import threading

class Controller:
    __instance = None
    __lock = threading.Lock()
    _number_selected = None

    @classmethod
    def instance(cls):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = cls()
        return cls.__instance
    
    @property
    def number_selected(self):
        return self._number_selected
    
    @number_selected.setter
    def number_selected(self, value):
        self._number_selected = value