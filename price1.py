def get_summ(one, two, delimiter = '&'):
    string = (f'{one} {delimiter} {two}')
    return(string)
learn_python = get_summ('Learn', 'python')
print(learn_python.upper())






'''Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит их к строке и отдает
объединенными через разделитель delimiter
Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение
на экран
Сделайте так, чтобы результирующая строка выводилась заглавными буквами'''
