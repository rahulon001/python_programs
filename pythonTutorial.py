with open("binary", "wb") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))

with open("binary", 'rb') as bin_file:
    for b in bin_file:
        print(b)


#pickling

# import pickle
#
# imelda = (
#     'more mayhem',
#     'imelda may',
#     '2011',
#     ((1, 'pulling the rug'),
#      (2, 'Not pulling the rug'),
#      (3, 'always pulling the rug')))
#
# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)
#
# with open("imelda.pickle", 'rb') as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)
#
# print(imelda2)


import shelve
with shelve.open('shelfTest') as fruit:
    pass

