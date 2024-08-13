encode_msg=123478990745361
last_letter= encode_msg % 26
decode_msg= chr(last_letter + 65)
print(f"Display the last letter of the encoded message:",decode_msg)