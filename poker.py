# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:15:36 2019

@author: DELL
"""
#python flask
h=('1H','2H','3H','4H','5')
def poker(hands):
    return max(hands,key=hand_rank)

def straight(ranks):
    #ranks1=ranks.sorted() ranks are coming in sorted order reversed
    '''f=0,g=-1
    for(i in ranks):
        if(g!=(i-1)):
            f+=1
        if(f>1):
            return False
        else:
            return True'''
    if len(set(ranks))==5 and (max(ranks)-min(ranks)==4):
        return True
    return False

def flush(suits):
    if len(set(suits))==1:
        return True
    return False

def kind(n,ranks):
    for i in ranks:
        if ranks.count(i)==n:
            return i
        return None
    
def two_pairs(ranks):
    hicard=kind(2,ranks)
    locard=kind(2,tuple(reversed(ranks)))
    if hicard != locard:
        return(hicard,locard)
    return None

def card_ranks(hand):
    ranks=['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks
    
def card_suits(hand):
    return [s for r,s in hand]

def hand_rank(hand):
    ranks=card_ranks(hand)
    suits=card_suits(hand)
    
    if straight(ranks) and flush(suits):
        return(8,max(ranks))
    elif kind(4,ranks):
        return(7,kind(4,ranks),kind(1,ranks))
    elif kind(3,ranks) and kind(2,ranks) :
        return(6,kind(3,ranks),kind(2,ranks))
        
if __name__=="__main__":
    assert(straight([6,5,4,3,2])==True)
    assert(straight([6,5,5,3,2])==True)