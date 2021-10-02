import copy

def main():
    #list is mutable values
    #a string value is immutable which cant be changed.

    name = 'Zophia a cat'
    newName = name[0:7] + 'the ' + name[8:12]
    print(newName)

    #list assigned to a variable
    #just a reference to memory access

    #mutable u just store reference

    #deepcopy
    #shallowcopy remember from c++

    spam = ['a','b','c','d']
    test = copy.deepcopy(spam)

    #line continuation
    x = ['a',
         'b',
         'c,',
         'd',
         'e']

if __name__ == '__main__':
    main()
