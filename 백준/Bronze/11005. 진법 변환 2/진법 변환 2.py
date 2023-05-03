def convertBase(decimalNumber, base):
    if decimalNumber == 0:
        print('0')
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    while decimalNumber > 0:
        remainder = decimalNumber % base
        result = alphabet[remainder] + result
        decimalNumber //= base
    return result

N, B = map(int, input().split())
print(convertBase(N,B))
        
