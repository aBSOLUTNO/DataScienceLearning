from multiprocessing.sharedctypes import Value
from sets import Set


# Defining sets and using some processing on them.
SetA = Set(['Red', 'Blue', 'Green', 'Black'])
SetB = Set(['Black', 'Green', 'Yellow', 'Orange'])
SetX = SetA.union(SetB)
SetY = SetA.intersection(SetB)
SetZ = SetA.difference(SetB)


print('{0}\n{1}\n{2}'.format(SetX, SetY, SetZ))

def DoSum(Value1, Value2):
    return Value1 + Value2

the_answer = DoSum(2,3)

print(the_answer)


#Making a function with unlimited arguments.
def DisplayMulti(ArgCount = 0, *VarArgs):
    print('You passed ' + str(ArgCount) + ' arguments', VarArgs)

DisplayMulti(2, True, 2+2)


# Logic on variables trough for loop.
def DisplayMultiInFor(*VarArgs):
    for Arg in VarArgs:
        if Arg.upper() == 'CONT':
            continue
            print('Continue Arguemnt:' + Arg)
        elif Arg.upper() == 'BREAK':
            break
        print ('Break Argument: ' + Arg)
        print('Good Argument: ' + Arg)

DisplayMultiInFor('Hello','Cont', 'Goodbye', 'First','Break', 'Last')

#Making tuples and printing them.
MyTuple = (1,2,3,(4,5,6,(7,8,9)))

for Value1 in MyTuple:
    if type(Value1) == int:
        print(Value1)
    else:
        for Value2 in Value1:
            if type(Value2) == int:
                print("\t", Value2)
            else:
                for Value3 in Value2:
                    print("\t\t", Value3)


#Defining useful iterations.
ListA = ['Orange', 'Yellow', 'Green', 'Brown']
ListB = [1,2,3,4]

# Accessing from index until index.
for Value in ListB[1:3]:
    print(Value)

#Parallel processing of list.
for Value1, Value2 in zip(ListA, ListB):
    print(Value1, '\t', Value2)






