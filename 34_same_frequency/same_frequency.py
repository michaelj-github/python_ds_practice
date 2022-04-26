def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    return len(str(num1)) == len(str(num2)) and set(list(str(num1))) - set(list(str(num2))) == set()

    # if len(str(num1)) == len(str(num2)) and set(list(str(num1))) - set(list(str(num2))) == set():
    #     print(True)
    #     return True
    # print(False)
    # return False

# print(same_frequency(551122, 221515))
# print(same_frequency(321142, 3212215))
# print(same_frequency(1212, 2211))
# print(same_frequency(123123, 322311))
# print(same_frequency(123456789, 234568791))
# print(same_frequency(123456789123456789, 234523456879168791))
# print(same_frequency(123456789123456789, 2345234568279168791))
