names = ['zhao', 'leng', 'yang']

print(f'{names[0].title()} has a supper tonight')
print(f'{names[1].title()} has a supper tonight')
print(f'{names[2].title()} has a supper tonight')

names[2] = 'Liu'
print('----------------')
print(f'{names[0].title()} has a supper tonight')
print(f'{names[1].title()} has a supper tonight')
print(f'{names[2].title()} has a supper tonight')

names.insert(0, 'yang')
names.insert(2, 'li')
names.append('zhang')
print('----------------')
print(f'{names[0].title()} has a supper tonight')
print(f'{names[1].title()} has a supper tonight')
print(f'{names[2].title()} has a supper tonight')
print(f'{names[3].title()} has a supper tonight')
print(f'{names[4].title()} has a supper tonight')
print(f'{names[5].title()} has a supper tonight')
print(f'Amount {len(names)} persons')

print('----------------')
delete = names.pop();
print(f'Sorry {delete.title()}')
delete = names.pop();
print(f'Sorry {delete.title()}')
delete = names.pop();
print(f'Sorry {delete.title()}')
delete = names.pop();
print(f'Sorry {delete.title()}')

print('----------------')
print(f'{names[0].title()} has a supper tonight')
print(f'{names[1].title()} has a supper tonight')

print('----------------')
del names[0]
del names[0]
print(names)
