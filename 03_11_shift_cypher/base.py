def encode(plaintext, shift):
    return 'string'


def decode(cypher_text, shift):
    return 'string'


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
