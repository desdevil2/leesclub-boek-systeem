from secrets import token_bytes



key = token_bytes(128)
print(str(key))