# -*- coding: utf-8 -*-

def digit_validation(required_valids, message):
    '''
    Function tests values that have integers present and confirms the test through
    the valid method funtion
    '''
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
    '''
    Checks to see if messages fulfill the following criteria

    1. There are 15 valid characters in the protocol: the lower-case characters 'a' through 'j'
    and the uppercase characters 'Z', 'M', 'K', 'P', and 'Q'.
    2. Every lower-case character in isolation is a valid message, e.g., 'a' is a valid message.
    3. If σ is a valid message then so is Zσ.
    4. If σ and τ are valid messages then so are Mστ, Kστ, Pστ, and Qστ.
    '''
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
    '''
    If empty string is returned, the statement is valid (all characters passed the test)
    '''
    if returned_message == '':
        return "Valid"
    return "Invalid"

def message_generator(message):
    '''
    Messages can be separated by white space,
    The generator yields the messages as they are split.
    '''
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

if __name__ == '__main__':
    generator_handling(message_generator("Khfa MZca Za Pa Zj Qa 3ZaZa 2ZaZa 2aaMa 5aaaaa 1PZa K2aaa 2ZaMbb Mbb MbZa"))