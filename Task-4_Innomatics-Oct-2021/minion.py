######################'The Minion Game'.#####################
# Kevin and Stuart want to play the 'The Minion Game'.
# Hint : A player gets +1 point for each occurrence of the substring in the string S.

def minion_game(string):         #Defining the function.
    s = string
    s1 = 0
    s2 = 0
    vowel = 'AEIOU'
    for i in range(len(s)):      #Logic has been used.
        if s[i] not in vowel:
            s1 = s1 + (len(s)-i)
        else:
            s2 = s2 + (len(s)-i)
    if s1 > s2:
        print("Stuart",s1)       #Print the result.
    elif s2 > s1:
        print("Kevin",s2)
    else:
        print("Draw")

if __name__ == '__main__':       #Main Function.
    s = input()
    minion_game(s)               #Calling the minion_game().