# задача 2.4
# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

     
s = "Hi! Hello!"
def remove_exclamation_marks(s):
     return s.replace('!', '')
 print(remove_exclamation_marks(s))
