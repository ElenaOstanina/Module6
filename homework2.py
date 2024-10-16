class Vehicle:
    __COLOR_VARIANTS=['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'


    def get_color(self):
        return f'Цвет: {self.__color}'


    def print_info(self):
        print (self.get_model())
        print (self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
        return "OK"
    def set_color(self, new_color):

        if new_color.upper:
            new_color = new_color.lower()

        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')




class Sedan(Vehicle):
    PASSENGERS_LIMIT = 5




v1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

result1 = v1.get_model()
result2 = v1.get_horsepower()
result3 = v1.get_color()
print (v1.print_info())

v1.set_color('Pink')
v1.set_color('BLACK')
v1.owner = 'Vasyok'

print (v1.print_info())