class Topics:
    def __init__(self,name=None):
        self.name=name
    
    def set_topic(self,name):
        self.name=name
    
    def get_name(self):
        print(f'este es el nombre del topico {self.name}')
        return str(self.name)