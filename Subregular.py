def get_bigrams_str(s):
    """Get non-repeating list of bigrams from the string."""
    stack = []
    for it in range(len(s)-1):
        current_bigram = s[it] + s[it+1]
        if  current_bigram not in stack:
            stack.append(current_bigram)
    return stack

def get_trigrams_str(s):
    """ Get non-repeating list of trigrams from the string."""
    stack = []
    for it in range(len(s)-2):
        current_trigram = s[it:it+3]
        if current_trigram not in stack:
            stack.append(current_trigram)
    return stack

def get_substr(s, n):
    """  Get non-repeating list of n-grams from the string."""
    stack = []
    current_ngram = s[it:ti+n]
    for it in range(len(s)-(n-1)):
        if current_ngram not in stack:
            stack.append(current_ngram)
    return stack

def augment_str(s, n):
    """ Add according amount of edge markers to string."""
    return "ㅓ"*(n-1) + s + "ㅏ"*(n-1)

def get_substr(s, n):
    """ Get non-repeating list of n-grams from the string."""
    substrings = set(s[it:it+n] for it in range(len(s)-(n-1)))
    return substrings                          

def delete(string, tier):
    """
    Delete strings that are non-member of tier.
    Return tier-based strings only.
    """
    return "".join([it for it in string if it in tier])

from itertools import*
def get_subseq(s, n):
    """ Get non-repeating list of subequences of length n, from the string."""
    subseqs = set(''.join(c) for c in combinations(s, n))
    return subseqs                    

def ngram_comparison(ngrams, grammar):
    """Check if there is an intersection between a list of ngrams and a forbidden set of strings."""
    return ngrams.intersection(grammar) == set()

def ngram_checker(s, grammar, check = "sl", tier = None):
    """
    Check if the string is in a language based on a chosen subregular class.
    Three subregular classes: tsl, sl, and sp.
    
    Arguments:
    s  -- a string to be examined if it's in a language
    grammar -- a forbidden set of strings
    check -- chosen subregular class
    tier -- specified tier
    """
    # compute length of n-grams
    n = len(grammar[0])
    # Case 1: "tsl" with specified tier
    if check == "tsl" and tier:
        s = delete(s, tier)
    # Case 2: "sl" or "tsl" without specified tier (equivalent to "sl")
    if check == "sl" or check == "tsl":
        return ngram_comparison(get_substr(augment_str(s, n), n), grammar)
    # Case 3: else ("sp")
    return ngram_comparison(get_subseq(augment_str(s, n), n), grammar)

test_grammar = ["bbb"]
print(ngram_checker("abbaaabab", test_grammar, check = 'tsl', tier = "b"))
print(ngram_checker("abbaaabab", test_grammar))
print(ngram_checker("abbaaabab", test_grammar, check = 'sl'))
print(ngram_checker("abbaaabab", test_grammar, check = 'tsl'))
print(ngram_checker("abbaaabab", test_grammar, check = 'sp'))

