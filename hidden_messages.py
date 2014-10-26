def digit_validation(required_valids, message):
    valid_words = 0
    current_word = []
    for idx, char in enumerate(message):
        current_word.append(char)
        if check_validity(valid_messages(''.join(current_word))) == "Valid":
            current_word = []
            valid_words += 1
    if valid_words >= int(required_valids) and len(current_word) == 0:
        return ''
    else:
        return 'Invalid'

def valid_messages(message):
    lowercase_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    upper_list = ['M', 'K', 'P', 'Q', 'Z']
    if message[:1].isdigit():
        return digit_validation(message[:1], message[1:])

    elif message[:1] in lowercase_list:
        return message[1:]

    elif message.startswith("Z") and len(message) > 1:
        return valid_messages(message[1:])

    elif message[:1] in upper_list and len(message) > 2:
        return valid_messages(valid_messages(message[1:]))

    else:
        return message

def check_validity(returned_message):
    if returned_message == '':
        return "Valid"
    return "Invalid"

def message_generator(message):
    messages = message.split(" ")
    for m in messages:
        yield m

def generator_handling(generator):
    while True:
        try:
            test_value = generator.next()
        except:
            break
        print test_value, check_validity(valid_messages(test_value))

generator_handling(message_generator("Khfa MZca Za Pa Zj Qa 3ZaZa 2ZaZa 2aaMa 5aaaaa 4aaaaa 1PZa K2aaa 2ZaMbb Mbb MbZa"))
