# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):

    if len(sequence)==1:
        return list(sequence)
    
    current_permutation=[]
    previous_permutation=get_permutations(sequence[1:])
    for each_seq in previous_permutation:
        each_seq_list=list(each_seq)
        for i in range(len(each_seq)+1):
            each_seq_list_copy=each_seq_list[:]
            each_seq_list_copy.insert(i,sequence[0])
            current_permutation.append("".join(each_seq_list_copy))
            
    return current_permutation

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    print(get_permutations('abcd'))
