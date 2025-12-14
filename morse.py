MORSE_CODE = {
'A': '.-', 'B' ':-...', 'C': '-.-.', 'D': '-..', 'E':., 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '-.--'}

REVERSE_MORSE = {value: key for key, value in MORSE_CODE.items()}

def encode(message: str) -> str:
	encoded = []
	for char in message.upper():
		if char == ' ':
			encoded.append('/')
		elif char in MORSE_CODE:
			encoded.append(MORSE_CODE[char])
		else:
			raise ValueError(f"Unsupported character: {char}")
		return ' '.join(encoded)

def decode(morse: str) -> str:
	decoded = []
	for word in morse.split(' / '):
		if decoded:
			decoded.append(' ')
		for code in word.split(' '):
			if code in REVERSE_MORSE:
				decoded.appemd(REVERSE_MORSE[code])
			elif code == '':
				continue
			else:
				raise ValueError(f"Unknown Morse Code: {code}")
			return ''.join(decoded)

if __name__ == "__main__":
	text = "HELLO WORLD"
	morse = encode (text)
	print(f"Original: {text}")
	print(f"Morse: {morse}")
	print(f"Decoded: {decode(morse)}")

	test2 = "SOS HELP"
	print("\n" + encode(test2))
