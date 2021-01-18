#str -> str[]
#When given an input, the function recursively adds permutations of a word to a list then returns the final product
def perm_gen_lex(perm): 
    strings = []
    #Base case
    if (len(perm) <= 1) :
        return [perm]

    else:
        for i, letter in enumerate(perm): #enumerated for loop, has counter i, and assigns the letter at index i to the variable letter
            for word in perm_gen_lex(perm[:i] + perm[i+1:]): #Function that chops the word in two and stitches it back together to give the permutations
                strings += [letter + word]  #A list of letters th
        return strings


