#ex 9-1
#
# def good():
#     return ['Harry', 'Ron', 'Hermione']

# ranger = (number for number in range(10) if number % 2 == 1)
#
# for x in ranger:
#     print(x)

#ex 9-2
cnts = 0
def get_odds():
    for number in range(10):
        if number % 2:
            yield number

odds = get_odds()
for i in odds:
    cnts = cnts + 1
    if cnts == 3:
        print(i)

