class Singleton:
    _instance = None 

    def __new__(cls):
        # create new obj
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        # point to existing
        return cls._instance
    
# Example usage
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True, both variables point to the same object