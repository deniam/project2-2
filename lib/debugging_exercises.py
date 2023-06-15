# def say_hello(name):
#     return f"hello {name}"

# print(say_hello('kay'))
# # Intended output:
# #
# # > say_hello("kay")
# # => "hello kay"

def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    print(f"Encrypted: {encrypted}")
    cipher = make_cipher(key)
    print(f"Cipher is {cipher}")
    plaintext_chars = []
    for i in encrypted:
        print(f"ORD(i): {ord(i)}")
        plain_char = cipher[(65 - ord(i))*(-1)]
        print(f"Plain char {plain_char}")
        plaintext_chars.append(plain_char)
        print(f"Plaintext_chars: {plaintext_chars}")
    return "".join(plaintext_chars)
    

def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 27)]
    cipher_with_duplicates = list(key) + alphabet
    # print(f"Cipher with duplicated: {cipher_with_duplicates}")


    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    # print(f"Cipher: {cipher}")
    return cipher
    

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
