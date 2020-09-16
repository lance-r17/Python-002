from abc import ABCMeta, abstractmethod

# 动物基类
class Animal(metaclass=ABCMeta):
    above_average_body = ['中等', '大']

    # 属性包括类型、体型、性格
    def __init__(self, category, body, character):
        self.category = category
        self.body = body
        self.character = character

    # 是否属于凶猛动物属性
    @property
    def is_ferocious(self):
        return self.body in Animal.above_average_body and self.category == '食肉' and self.character == '凶猛'

# 猫类
class Cat(Animal):
    
    # 属性包括名字、类型、体型、性格
    def __init__(self, name, category, body, character):
        super().__init__(category, body, character)
        self.name = name
        self.call = '喵'

    # 是否适合作为宠物属性
    @property
    def is_pet(self):
        return not self.is_ferocious

# 狗类
class Dog(Animal):
    
    # 属性包括名字、类型、体型、性格
    def __init__(self, name, category, body, character):
        super().__init__(category, body, character)
        self.name = name
        self.call = '汪汪'

    # 是否适合作为宠物属性
    @property
    def is_pet(self):
        return not self.is_ferocious

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    # 若属性名为猫类或狗类，遍历并返回匹配类型的动物实例
    def __getattribute__(self, item):
        if item == Cat.__name__ or item == Dog.__name__:
            for a in self.animals.values():
                if item == type(a).__name__:
                    return a
        return super().__getattribute__(item)

    def add_animal(self, animal):
        if not self.animals.get(id(animal)):
            self.animals[id(animal)] = animal