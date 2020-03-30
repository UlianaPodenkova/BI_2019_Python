# 1)Составить список из чисел от 1 до 1000, которые имеют в своём составе 7.
list_with7 = [el for el in range(1, 1001) if '7' in str(el)]
print(list_with7)

# 2)Взять предложение Would it save you a lot of time if I just gave up and went mad now? и сделать его же без гласных
initial_sentence = 'Would it save you a lot of time if I just gave up and went mad now?'
new_sentence = [x for x in initial_sentence if x not in 'aeoiuyAEOUIY']
print(*new_sentence, sep='')

# 3)Для The ships hung in the sky in much the same way that bricks don't сост.словарь, где слову соотв его длина.
phrase = "The ships hung in the sky in much the same way that bricks don't"
dict_lenwd = dict([(el, len(el)) for el in phrase.split(' ')])
print(dict_lenwd)

# 4)Для чисел от 1 до 1000 наибольшая цифра, на которую они делятся (1-9).
maximum_divisor = [max([x for x in range(1, 10) if el % x == 0]) for el in range(1, 1001)]
print(maximum_divisor)

# 5)Список всех чисел от 1 до 1000, не имеющих делителей среди чисел от 2 до 9.
no_divisors = [el for el in range(1, 1001) if el not in [i for i in range(1, 1001) for x in range(2, 10) if i % x == 0]]
print(no_divisors)
