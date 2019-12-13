'''
word counter

'''

def word_count(word_list):
    d = {}
    words = word_list.split()
    for word in words:
        if word not in d:
            d[word] = 0
        d[word] += 1
    print(d)


w = "I should note that the code used in this blog post and in the video above is available on my github. Please let me know if you have any questions either here, on youtube, or through Twitter! If you want to learn how to utilize the Pandas, Matplotlib, or Seaborn libraries, please consider taking my Python for Data Visualization LinkedIn Learning course."
word_count(w)
