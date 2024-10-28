"""Создать базовый класс с функцией – сумма прогрессии.
Создать производные классы: арифметическая прогрессия и геометрическая прогрессия. 
Каждый класс имеет два поля типа double. Первое – первый член прогрессии, второе – 
постоянная разность (для арифметической) и постоянное отношение (для геометрической). 
Определить функцию вычисления суммы, где параметром является количество элементов прогрессии. """

#Базовый класс - прогрессия
class Progression:
    def __init__(self, first, constant):
        if isinstance(first, (int, float)) == False or isinstance(constant, (int, float)) == False:
            raise ValueError("Некорректное значение")
        self._first = first          #первый член прогрессии
        self._constant = constant    #постоянная разность/отношение

    def Sum(self, num):
        return 0

#Арифметическая прогрессия
class Arithmetic_progression(Progression):
    def Sum(self, num):
        if isinstance(num, (int)) == False:
            raise ValueError("Некорректное значение")
        if num <= 0:
            return 0
        return num / 2 * (2 * self._first + (num - 1) * self._constant)

#Геометрическая прогрессия
class Geometric_progression(Progression):
    def Sum(self, num):
        if isinstance(num, (int)) == False:
            raise ValueError("Некорректное значение")
        if num <= 0:
            return 0
        if self._constant == 1:
            return self._first* num
        return self._first * (1 - self._constant ** num) / (1 - self._constant)


arithm = Arithmetic_progression(2, 3) 
print("Сумма первых 10 членов арифметической прогрессии: ", arithm.Sum(10))
geom = Geometric_progression(2, 3) 
print("Сумма первых 10 членов геометрической прогрессии: ", geom.Sum(10))
