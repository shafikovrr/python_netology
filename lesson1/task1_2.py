print('#####Расчет периметра и площади квадрата')
length = input('Введите значение длинны стороны квадрата:', )
length = abs(int(length))
perimeter = 4 * length
print('Периметр:', perimeter)
print('Расчет периметра и площади квадрата')
area = length * length
print('Площадь квадрата:', area)

print('#####Расчет периметра и площади прямоугольника:')
length = int(input('Введите длину прямоугольника:', ))
length = abs(length)
width = int(input('Введите ширину прямоугольника:', ))
width = abs(width)
print('Периметр прямоугольника:', 2 * (length + width))
print('Площадь прямоугольника:', length ** 2)
