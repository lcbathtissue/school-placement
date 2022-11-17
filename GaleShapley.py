# GALESHAPLEY MATCHING ==> Joey Whelan
# https://github.com/joeywhelan/gale-shapley/blob/main/gs.py

def gale_shapley(prefs, proposers):
    matches = []
    while len(proposers) > 0:  # terminating condition - all proposers are matched
        proposer = proposers.pop(0)  # Each round - proposer is popped from the free list
        proposee = prefs[proposer].pop(0)  # Each round - the proposer's top preference is popped
        matchLen = len(matches)
        found = False

        for index in range(matchLen):
            match = matches[index]
            if proposee in match:  # proposee is already matched
                found = True
                temp = match.copy()
                temp.remove(proposee)
                matchee = temp.pop()
                if prefs[proposee].index(proposer) < prefs[proposee].index(matchee):  # proposer is a higher preference
                    matches.remove(match)  # remove old match
                    matches.append([proposer, proposee])  # create new match with proposer
                    proposers.append(matchee)  # add the previous proposer to the free list of proposers
                else:
                    proposers.append(proposer)  # proposer wasn't a higher prefence, so gets put back on free list
                break
            else:
                continue
        if not found:  # proposee was not previously matched so is automatically matched to proposer
            matches.append([proposer, proposee])
        else:
            continue
    return matches