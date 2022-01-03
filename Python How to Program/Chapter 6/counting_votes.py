from collections import Counter

def get_vote_results(polls):
    votes_results = Counter(polls.split(','))
    print(votes_results)
    

poll = 'Ahmed,Abu,Ahmed,Abu,Ahmed,Ahmed,Abu'
get_vote_results(poll)