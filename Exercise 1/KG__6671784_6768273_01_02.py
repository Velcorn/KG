from rdflib import Graph


g = Graph()
g.parse("simpsons.ttl")

print(f"The model has {len(g)} triples.")
