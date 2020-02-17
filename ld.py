list1 = [3, 5, 7, 9, 10.5]
print(list1)
list1.append('Python')
print(len(list1))
print(list1[0])
print(list1[-1])
print(list1[1:4])
list1.remove('Python')
print(list1)

dict1 = {'city': 'Москва', 'temperature': '20'}
print(dict1['city'])
dict1['temperature'] =  int(dict1["temperature"]) - 5
print(dict1) 
print(dict1.get('country', 'Россия'))
dict1['date'] = '27.05.2019'
print(len(dict1))

