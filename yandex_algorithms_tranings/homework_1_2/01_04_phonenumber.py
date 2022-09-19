new = input()
exist1 = input()
exist2 = input()
exist3 = input()

def getCodeAndNumber(n):
    cn = n.replace('(', '').replace(')', '').replace('-', '').replace('+', '')
    return ('495', cn) if len(cn) == 7 else (cn[1:4], cn[4:])

newCode, newNumber = getCodeAndNumber(new)

for num in [exist1, exist2, exist3]:
    c, n = getCodeAndNumber(num)
    print('NO' if (c != newCode or n != newNumber) else 'YES')

# 8(495)430-23-97
# +7-4-9-5-43-023-97 # YES
# 4-3-0-2-3-9-7 # YES
# 8-495-430 # NO

# 86406361642
# 83341994118 # NO
# 86406361642 # YES
# 83341994118 # NO

# +78047952807
# +78047952807 # YES
# +76147514928 # NO
# 88047952807 # YES
