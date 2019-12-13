
# def EndcodeIt(ascii,a,b,c):
#     for i in range(len(ascii)):
#         if(i % 3 == 0):
#             ascii[i] = (ascii[i] + a) % 256
#         if(i % 3 == 1):
#             ascii[i] = (ascii[i] + b) % 256
#         if (i % 3 == 2):
#             ascii[i] = (ascii[i] + c) % 256
#     return ascii


# def encodingString(myString, MyAdjustments):
#     myArray = []
#     for i in range(len(myString)):
#         myArray.append(chr(i))
#     myArray = EndcodeIt(myArray, MyAdjustments[0], MyAdjustments[1], MyAdjustments[2])
#     myEncodedString = ""
#     for i in range(len(myArray)):
#         myEncodedString += chr(myArray[i])
#     return myEncodedString


# a = "5 106 74 41 116 10 221 72 77 43 108 80 30 121 83 41 102 82 38 116 76 48 37 68 44 119 254 48 116 74 51 110 76 36 37 82 37 106 254 4 102 75 31 110 82 221 104 70 30 113 74 34 115 69 34 51 254 13 113 67 30 120 67 221 120 67 43 105 254 54 116 83 47 37 81 44 113 83 49 110 77 43 37 63 43 105 254 0 91 254 49 116 254 38 104 63 43 104 77 33 106 30 36 102 75 31 110 82 47 106 81 34 102 80 32 109 12 32 116 75 221 118 83 44 121 71 43 108 254 47 106 68 34 119 67 43 104 67 247 37 64 244 53 22 35 103 21 35 106 18 235"
# l = a.split(' ')
# print(l)
# a = []
# for i in l:
#
#     a.append(int(i))
# print(''.join(chr(i) for i in a))
#
# print(EndcodeIt("Hello World",10,20,30))
