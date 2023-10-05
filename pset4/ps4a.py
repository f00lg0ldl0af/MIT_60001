# Problem Set 4A
# Name: pbj
# Collaborators:
# Time Spent: 2 days

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # base case: return a list with that single character 
    if len(sequence) == 1:
        return [sequence]
    
    # simpler version of the problem: think 2 characters in sequence
    else:
        permutations = []
        letter = sequence[0]
        # get all remaining chars except first char
        for subseq in get_permutations(sequence[1:]):
            len_subseq = len(subseq) + 1  
            # Different ways of inserting first char into each permutation of remaining chars
            for i in range(len_subseq):
                newstr = subseq[:i] + letter + subseq[i:]
                # print(newstr) ; test
                permutations.append(newstr)
                
        return permutations # this is the value returned for every get_permutations(sequence[1:]) called

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    # test 1 
    example_input = 'fa'
    print('Input:', example_input)
    print('Expected output:', ['fa','af'])
    print('Actual Output:', get_permutations(example_input))
    print("----------------------------------------------------------------------")

    # test 2
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected output:', ['abc','acb','bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print("----------------------------------------------------------------------")

    # test 3
    example_input = 'bust'
    print('Input:', example_input)
    print('Expected output:', ['bust', 'ubst', 'usbt', 'ustb',
                               'bsut', 'sbut', 'subt', 'sutb',
                               'bstu', 'sbtu', 'stbu', 'stub',  
                               'buts', 'ubts', 'utbs', 'utsb',
                               'btus', 'tbus', 'tubs', 'tusb', 
                               'btsu', 'tbsu', 'tsbu', 'tsub'
                               ])
    print('Actual Output:', get_permutations(example_input))
    print("----------------------------------------------------------------------")

