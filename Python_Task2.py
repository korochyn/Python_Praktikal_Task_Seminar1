# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Ведите трехзначное число: '))
summ = int(number/100) + int((number-int(number/100)*100)/10) + (number - int(number/100)*100 - int((number-int(number/100)*100)/10)*10) 
print(summ)