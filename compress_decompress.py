'''
Write a program to compress a string and send it a over a network and decompress it on the receivers end
'''

import zlib

text1 = "Hello world"

text = bytes(text1, 'utf-8')

compressed_data = zlib.compress(text, level = -1)
print("Compressed: ", compressed_data)

decompressed_data = zlib.decompress(compressed_data)
print("Decompressed: ", decompressed_data.decode('utf-8'))