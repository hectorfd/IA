class Monitor:
    count_monitor = 0
    def __init__(self, brand, size):
        Monitor.count_monitor += 1
        self.id_monitor = Monitor.count_monitor
        self.brand = brand
        self.size = size
        
    @classmethod
    def get_total_monitors(cls):
        return cls.count_monitor
    
    # metodo para presentar informacion
    def __str__(self):
        return f"Id: {self.id_monitor}, Brand: {self.brand}, Size: {self.size}"
    
        