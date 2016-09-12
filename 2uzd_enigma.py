k1 = 15
k2 = 19

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lambda1 = [5, 3, 2, 0, 17, 10, 8, 24, 20, 11, 1, 12, 9, 22, 16, 6, 25, 4, 18, 21, 7, 13, 15, 23, 19, 14]
lambda2 = [10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
cypher1 = [4, 5, 24, 24, 15, 3, 21, 7, 17, 16, 11, 7, 13, 7, 24, 20, 11, 10, 17, 3, 23, 18, 16, 14, 12, 5, 20, 24, 5, 5, 0, 11, 9, 17, 8, 12, 1, 6, 24, 19, 9, 4, 5, 4, 8, 4, 14, 18, 3, 16, 10, 13, 23, 22, 5]

cypher2 = [23, 14, 8, 12, 20, 5, 13, 24, 1, 24, 5, 14, 5, 2, 3, 21, 12, 25, 3, 6, 8, 13, 3, 4, 8, 5, 6, 13, 7, 15, 8, 2, 25, 9, 25, 23, 24, 20, 12, 22, 11, 2, 18, 17, 15, 17, 15, 6, 3, 17, 24, 20, 7, 20, 19]

sigma = [2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]

def convertWordToNumbers(text):
    numbers = []
    for t in text:
        numbers.append(abc.index(t))
    return numbers

def encrypt(text):
    cypher = ''
    for i in range(0, len(text)):
        t = text[i]

        m1 = i % 26
        m2 = (i - m1) / 26

        c = (t + m1 + k1) % 26
        c = lambda1[c]
        c = (c - m1 - k1) % 26
        c = (c + m2 + k2) % 26
        c = lambda2[c]
        c = (c - m2 - k2) % 26

        cypher += abc[c]

    return cypher

def decrypt(cypher):
    text = ''
    for i in range(0, len(cypher)):
        c = cypher[i]

        m1 = i % 26
        m2 = (i - m1) / 26

        t = (c + m2 + k2) % 26
        t = lambda2.index(t)
        t = (t - m2 - k2) % 26
        t = (t + m1 + k1) % 26
        t = lambda1.index(t)
        t = (t - m1 - k1) % 26

        text += abc[t]
    return text

def decryptWithReflection(cypher):
    encryptedNumberList = convertWordToNumbers(encrypt(cypher))
    reflectedNumberList = []
    for i in range(0, len(cypher)):
        reflectedNumberList.append(sigma.index(encryptedNumberList[i]))
    return decrypt(reflectedNumberList)


# Pirmasis sifras
decrypt(cypher1);

# Antrasis sifras
decryptWithReflection(cypher2)

# Testas
testString = "LABADIENA"
assert decrypt(convertWordToNumbers(encrypt(convertWordToNumbers(testString)))) == testString

