"""
Kelvin Bilali, 7054436
Enrico Milutzki, 6671784
Jan Willruth, 6768273
"""
from rdflib import Graph


g = Graph()
g.parse("simpsons.ttl")

print(f"The model has {len(g)} triples.")
