# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
 # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
 # Вам требуется написать программу, которая проверяет счастливость билета.

ticketNumber = int(input("Введите номер билета: "))
firstHalf = ticketNumber // 1000
secondHalf = ticketNumber % 1000
sumDigitFirstHalf = (firstHalf // 100) + (firstHalf // 10 % 10) + (firstHalf % 10)
sumDigitSecondHalf = (secondHalf // 100) + (secondHalf // 10 % 10) + (secondHalf % 10)

if sumDigitFirstHalf == sumDigitSecondHalf:
    print("Этот билет счастливый")
else:
    print("Этот билет не счастливый")    