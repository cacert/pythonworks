def a():
    sentence = "the quick brown fox jumps over the lazy dog"
    words = sentence.split()
    word_lengths = []
    for word in words:
        if word != "the":
            word_lengths.append(len(word))

def b():
    sentence = "the quick brown fox jumps over the lazy dog"
    words=sentence.split()
    words_length= [len(word) for word in words if word != 'the']
    return words_length

def c():
    nums=[10,11,-11,-22,-33]
    numsp = [num for num in nums if num > 0 ]
    return numsp


import sys
try:
    print(c())
    raise Exception("kasim")
except Exception as errno:
    sys.stderr.write(str(errno))
