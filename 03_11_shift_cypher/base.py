import time


def encode(plaintext, shift):
    b = bytearray(plaintext, 'utf-8')
    for i in range(len(plaintext)):
        c = b[i]
        if c > 64 and c < 91:
            b[i] = (c - 65 + shift) % 26 + 65
        elif c > 96 and c < 123:
            b[i] = (c - 97 + shift) % 26 + 97
    return b.decode()

def decode(cypher_text, shift):
    return encode(cypher_text, -shift)

# Basic Test
assert encode('Identity theft is not a joke, Jim!', 5) == "Nijsynyd ymjky nx sty f otpj, Onr!"
assert encode('Bears, beets, Battlestar Galactica', 30) == "Fievw, fiixw, Fexxpiwxev Kepegxmge"
assert encode('I want people to be afraid of how much they love me.', 8) == "Q eivb xmwxtm bw jm inziql wn pwe uckp bpmg twdm um."
print('Encode Tests Passed')

assert decode('Z bevn vortkcp nyrk kf uf. Slk ze r dlty dfiv ivrc jvejv, Z yru ef zuvr nyrk kf uf.', 17) == 'I knew exactly what to do. But in a much more real sense, I had no idea what to do.'
assert decode("L grq'w kdwh lw. L mxvw grq'w olnh lw dw doo dqg lw'v whuuleoh", 3) == "I don't hate it. I just don't like it at all and it's terrible"
assert decode('Ufm gq Hsqrgac Zcytcp?', 24) == "Who is Justice Beaver?"
print('Decode Tests Passed')

# Complete Tests
# This import statement can go a bit wonky? Make sure your file is in the submission folder when running this
# from tests import full_test
# full_test(encode, decode)

start = time.time()
# Basic Test
encode('Identity theft is not a joke, Jim!', 5) 
encode('Bears, beets, Battlestar Galactica', 30)
encode('I want people to be afraid of how much they love me.', 8)

decode('Z bevn vortkcp nyrk kf uf. Slk ze r dlty dfiv ivrc jvejv, Z yru ef zuvr nyrk kf uf.', 17)
decode("L grq'w kdwh lw. L mxvw grq'w olnh lw dw doo dqg lw'v whuuleoh", 3)
decode('Ufm gq Hsqrgac Zcytcp?', 24)
#print('Decode Tests Passed')
end = time.time()
print('time:', end - start)
