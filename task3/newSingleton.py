class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Инициализаця экземпляра может быть выполнена здесь
        return cls._instance
    
# Пример использования
obj1=Singleton()
obj2=Singleton()

print(obj1 is obj2)