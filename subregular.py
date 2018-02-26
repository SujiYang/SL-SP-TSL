#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_bigrams_str(s):
    stack = []
    for it in range(len(s)-1):
        if s[it]+s[it+1] not in stack:
            stack.append(s[it]+s[it+1])
    return stack

def get_trigrams_str(s):
    stack = []
    for it in range(len(s)-2):
        if s[it:it+3] not in stack:
            stack.append(s[it:it+3])
    return stack

def get_substr(s, n):
    stack = []
    for it in range(len(s)-(n-1)):
        if s[it:it+n] not in stack:
            stack.append(s[it:it+n])
    return stack

def augment_str(s, n):
    return "ㅓ"*(n-1) + s + "ㅏ"*(n-1)

def get_substr(s, n):
    substrings = set(s[it:it+n] for it in range(len(s)-(n-1)))
    return substrings                          

def delete(string, tier):
    return "".join([i for i in string if i in tier])
delete("aabcd", ["a", "c"])

from itertools import*
def get_subseq(s, n):
    subseqs = set(''.join(c) for c in combinations(s, n))
    return subseqs                    

def ngr_gmr_compare(ngrams, grammar):
    # intersection: ngrams 교집합 grammar (가 0일 경우: empty set(), True)
    return ngrams.intersection(grammar) == set()

def ngram_check(s, grammar, check = "sl", tier = none):
    # compute length of n-grams
    n = len(grammar[0])
    # choose evaluation function
    if check == "tsl" and tier:
        s = delete(string, tier)
    if check == "sl" or check == "tsl":
        return ngr_gmr_compare(get_substr(augment_str(s, n), n), grammar) 
    return ngr_gmr_compare(get_subseq(augment_str(s, n), n), grammar)

gr = ["bbb"]
print(ngram_check("abbaaabab", gr, check = 'tsl', tier = "b")
      
VN = ["an", "in", "on", "am", "im", "om"]
print(ngram_check("banana", VN))
print(ngram_check("baunaunau", VN))
print(ngram_check("baunaunau", VN, check="sp"))

NoFinalVOBS = ["bㅏ", "dㅏ", "gㅏ", "zㅏ", "vㅏ"]
print(ngram_check("rip", NoFinalVOBS))
print(ngram_check("lib", NoFinalVOBS))
print(ngram_check("zig", NoFinalVOBS))

NoFinalVOBSㅡCONT = ["bㅏ", "dㅏ", "gㅏ"]
print(ngram_check("rip", NoFinalVOBSㅡCONT))
print(ngram_check("rib", NoFinalVOBSㅡCONT))
print(ngram_check("lis", NoFinalVOBSㅡCONT))
print(ngram_check("liz", NoFinalVOBSㅡCONT))
print(ngram_check("zif", NoFinalVOBSㅡCONT))
print(ngram_check("ziv", NoFinalVOBSㅡCONT))

NoComplexOnset = ["pl","br","gl","al","au"]
print(ngram_check("play", NoComplexOnset))
print(ngram_check("pele", NoComplexOnset))
print(ngram_check("broom", NoComplexOnset))
print(ngram_check("burum", NoComplexOnset))
print(ngram_check("glass", NoComplexOnset))
print(ngram_check("galas", NoComplexOnset))

gr = ["bbb"]
print(ngram_check("abbaaabab", gr, check = 'tsl', tier = "b"))
