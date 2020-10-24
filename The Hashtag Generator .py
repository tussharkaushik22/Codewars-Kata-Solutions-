#this is simple and easy solution you can try to short up the code if you understood this one easily. 


def generate_hashtag(s):
    #your code here
    if len(s) > 140 or len(s) == 0:
        return False
    s = s.split()
    l = []
    for i in s:
        i = i.capitalize()
        l.append(i)
    l = "#"+"".join(l)
    return l
