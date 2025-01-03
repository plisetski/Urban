# Условная конструкция. Операторы if, elif, else

# name = input('Введите ваше имя: ')
# if name == 'Urban':
#     print('Здравствуйте, администратор')
# elif name == 'Vlad':
#     print('Здравствуйте, преподаватель')
# else:
#     print('Привет', name)

# number = int(input('Введите число: ')) # Fizz, Buzz, FizzBuzz
# if number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print('Число не подходит.')

print('Вывести три числа')
first = int(input('Первое: '))
second = int(input('Второе: '))
third = int(input('Третье: '))
if first == second and first == third: # Как вариант - if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)


