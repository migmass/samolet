#Разработайте программу с использованием функтора, 
#которая при каждом вызове функции будет возвращать 
#следующее значение арифметической прогрессии на 
#основе параметров: начальное значение и шаг увеличения, 
#которые задаются при создании функтора.

class ArithmeticProgression:
    def __init__(self, start_value,step):
        self.curent_value=start_value #устанавливаем текущее значение
        self.step=step #задаем шаг програессии

    def __call__(self):
        result=self.curent_value
        self.curent_value +=self.step
        return result
    
ap=ArithmeticProgression(3,3)
for _ in range(5):
    print(ap())
