from morse_dict import MORSE_CODE_DICT


def encrypt(message):
    cipher = ''
    for letter in message:
		if letter != ' ':
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			cipher += ' '

	return cipher

