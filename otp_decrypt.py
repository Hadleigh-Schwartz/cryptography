def hex_to_ascii(hex_string):
	hex_string = hex_string.replace("0x","")
	bytes_object = bytes.fromhex(hex_string)
	return bytes_object.decode("ASCII")



def crib_drag(message1, message2, crib):
	max_len = min(len(message1), len(message2))
	crib_len = len(crib)

	i = 0
	while i + crib_len < max_len:
		piece1 = "0x"
		piece2 = "0x"
		j = i


		while j < i + crib_len:
			piece1 = piece1 + message1[j] + message1[j + 1] 
			piece2 = piece2 + message2[j] + message2[j + 1]
			j = j + 2

		
		hex_piece1 = int(piece1, 16)
		hex_piece2 = int(piece2, 16)
		hex_crib = int(crib, 16)


		potential_key = hex_crib ^ hex_piece1;

		potential_m2 = potential_key ^ hex_piece2;


		#only printing if something that could be an enclish word is produced 
		word = hex_to_ascii(hex(potential_m2)) 
		if word.isalpha():
			print(word + " from m1 " + piece1 + " and m2 " + piece2)


		i = i + 2


def ascii_to_hex(message):
	binary = hex(int.from_bytes(message.encode(), 'big'));
	return binary



			
file1 = open("09.txt", "r")
file2 = open("15.txt", "r")
message1 = file1.read()
message2 = file2.read()

crib = ascii_to_hex("have").replace("0x","")
crib_drag(message1, message2, crib)