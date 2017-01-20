"""Exercise: Create a class that can represent a MarkovChain
https://en.wikipedia.org/wiki/Markov_chain

Expected to have the following methods:

add(self, state_from, state_to):
This adds a single observed occurrence of a state change from/to.
returns None
NOTE: state_from can equal state_to

probability_table(self, state_from):
Return a dictionary of {state_to : probability, ...} which has the probabilities
that or each state_to given state_from. The probabilities should sum to unity.

most_probable(self, state_from):
Returns a tuple of most likely next states given state_from.
This is the keys in the probability_table (above) which have the highest
probabilities.

For example, a simple chain where that state flips from 'A' to 'B':

>>> c = MarkovChain.MarkovChain()
>>> c.add('A', 'B')
>>> c.add('B', 'A')
>>> c.probability_table('A')
{'B' : 1.0})
>>> c.probability_table('B')
{'A' : 1.0})
>>> c.most_probable('A')
('B',)
>>> c.most_probable('B')
('A',)

Created on 2 Apr 2015

@author: paulross
"""
import collections

class MarkovChain(object):
    def __init__(self):
        self._graph = collections.defaultdict(lambda: collections.defaultdict(int))
    
    def add(self, state_from, state_to):
        """This adds a single observed occurrence of a state change from/to
        and returns None"""
        self._graph[state_from][state_to] += 1
    
    def probability_table(self, state_from):
        """Return a dict of {state_to : probability, ...}.
        Returns empty dict if state_from unknown."""

        occurrence_table = self._graph[state_from]
        if not len(occurrence_table):
            return {}
        max_occurrence = max(occurrence_table.values())
        return {k: v / max_occurrence for k, v in occurrence_table.items()}  # PY3 division
    
    def most_probable(self, state_from):
        """Returns a tuple of most probable next states."""
        probability_table = self.probability_table(state_from)
        states = set()
        states_val=0
        for i, j in probability_table.items():
            if j > states_val:
                states = {i}
            elif j == states_val:
                states.add(i)
        return tuple(states)
