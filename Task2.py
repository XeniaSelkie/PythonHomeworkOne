# Найдите сумму цифр трехзначного числа.

threeDigitNumber = int(input("Введите трёхзначное число: "))
sumDigit = (threeDigitNumber // 100) + (threeDigitNumber // 10 % 10) + (threeDigitNumber % 10)
print(f'Сумма цифр данного числа: {sumDigit}')