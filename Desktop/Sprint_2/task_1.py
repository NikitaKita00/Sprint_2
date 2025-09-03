shelf1 = ['клубничное варенье', 'вишнёвое варенье']
shelf2 = ['грушевое варенье', 'абрикосовое варенье']

closet = [shelf1, shelf2]

print('Привет, Карлсон!')
print('Смотри, у меня с собой:')

for shelf in closet:
    for jam in shelf:
        print(jam)