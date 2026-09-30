def calculate_rectangle(width, height):
    return width*height

def calculate_perimeter(width, height):
    return 2*(width+height)

def describe_rectangle(width, height, unit="см"):
    s=calculate_rectangle(width,height)
    per=calculate_perimeter(width,height)
    print(f"Прямоугольник {width}*{height} {unit},")
    print(f"Площадь {s} кв.{unit},")
    print(f"Периметр {per} {unit}.")

describe_rectangle(5,10)
describe_rectangle(3,4,"м")