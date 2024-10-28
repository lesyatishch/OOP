"""Создать базовый класс – работник, и производные классы – 
лужащий с почасовой оплатой, служащий в штате и служащий с процентной ставкой. 
Определить функцию начисления зарплаты."""

#Базовый класс - работник
class Employee:
    def __init__(self, name):
        if isinstance(name, str) == False:
            raise ValueError("Некорректное значение")
        self._name = name
    def Get_name(self):
        return self._name
    def Calculate_salary(self):
        return 0

#Работник с почасовой оплатой        
class Hourly_employee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        if isinstance(hourly_rate, (int, float)) == False or isinstance(hours_worked, (int, float)) == False:
            raise ValueError("Некорректное значение")
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def Calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked

#Работник штата
class Department_employee(Employee): 
    def __init__(self, name, salary):
        super().__init__(name)
        if isinstance(salary, (int, float)) == False:
            raise ValueError("Некорректное значение")
        self._salary = salary

    def Calculate_salary(self):
        return self._salary

#Работник с процентной ставкой
class Percent_employee(Department_employee):
    def __init__(self, name, salary, percent_rate, sales):
        super().__init__(name, salary)
        if isinstance(percent_rate, (int, float)) == False or isinstance(sales, (int, float)) == False:
            raise ValueError("Некорректное значение")
        self.__percent_rate = percent_rate
        self.__sales = sales

    def Calculate_salary(self):
        return self._salary + (self.__percent_rate * self.__sales)


emp1 = Hourly_employee("Андрей Максимов", 800, 60)
print("Имя почасового работника:", emp1.Get_name())
print("Зарплата почасового работника:", emp1.Calculate_salary())
emp2 = Department_employee("Мария Петрова", 35000)
print("Имя работника штата:", emp2.Get_name())
print("Зарплата работника штата:", emp2.Calculate_salary())
emp3 = Percent_employee("Алексей Иванов", 20000, 0.4, 58000)
print("Имя работника с процентной ставкой:", emp3.Get_name())
print("Зарплата работника с процентной ставкой:", emp3.Calculate_salary())