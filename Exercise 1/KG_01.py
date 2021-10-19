from rdflib import Graph


def read_rdf():
    g = Graph()
    g.parse("simpsons.ttl")

    return f"The model has {len(g)} triples."


if __name__ == '__main__':
    print(read_rdf())
