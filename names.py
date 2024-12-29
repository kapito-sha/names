calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    info = (len(string), string.upper(), string.lower())
    count_calls()
    return info
def is_contains(string, list_to_search):
    string = string.lower()
    for i in range(len(list_to_search)):
        if type(list_to_search[i]) == str:
            list_to_search[i] = list_to_search[i].lower()
        else:
            continue
    for i in range(len(list_to_search)):
        if list_to_search[i] == string:
            result = True
            break
        else:
            result = False
            continue
    count_calls()
    return result
print(string_info('Quokka'))
print(string_info('I love my cats Cherchik and Lunya'))
print(is_contains('WOW', ['wow', 'blablabla', 'xexexe'])) # Urban ~ urBAN
print(is_contains('zeus', ['olimp', 'thor'])) # No matches
print(calls)




