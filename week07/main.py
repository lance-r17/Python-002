
from zoo import Zoo, Cat

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')