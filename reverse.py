def reverse(string):
    s1=''
    if string[0]=='0':
        for i in range(-len(string)+1,0):
            s1=s1+string[-i]
    else:
        pass

    return s1