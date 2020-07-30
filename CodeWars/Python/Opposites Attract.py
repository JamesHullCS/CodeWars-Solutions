# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

# James Hull

# Original Solution
def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0 or flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    return False

# Revised Solution
def lovefunc( flower1, flower2 ):
    return flower1 % 2 != flower2 % 2