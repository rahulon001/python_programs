
def ipNumberSegments(ip):
    segment, segment_length, character = 1, 0, ''
    for character in ip:
        if character == '.':
            print("Segment {} contains {} characters". format(segment, segment_length))
            segment += 1
            segment_length = 0
        else:
            segment_length += 1
    if character != '.':
         print("Segment {} contains {} characters".format(segment, segment_length))


ip = input("Please enter an ip address:")
ipNumberSegments(ip)