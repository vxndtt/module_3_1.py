calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    n = string
    result = (len(n), n.upper(), n.lower())
    return result


def is_contains(string, list_to_search):
    count_calls()
    string = str(string.lower())
    list_to_search = list(list_to_search)
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string:
            result = True
            break
        else:
            result = False
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Banana', ['ban', 'BaNaNA', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(string_info('Cloud'))
print(calls)
