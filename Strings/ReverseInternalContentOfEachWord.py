# Reverse Internal content of String

def reverseInternalContent(string):
    output=[]#hello world
    str_list=string.split()
    for elem in str_list:
        #word=elem[:: -1]
        output.append(elem[:: -1])
    print("Answer is ",' '.join(output))

reverseInternalContent('hello world')

