lst = [1,2,3,4,5,6,7,8,9]
n = 5

def rotateBack(lst,n):
    """
        Backward rotation
        Store the first  elements in a temp array
        Assign the new array from n + start elements
    """
    return lst[n:] + lst[:n]
def rotateForward(lst,n):
    """
        Forward rotation
        Store the first n elements in a temp array
        Assign the new array from n + start elements
    """
    return lst[-n:] + lst[:-n]

# write main function to exec __main__()
if __name__ == "__main__":
    print(rotateBack(lst,n))
