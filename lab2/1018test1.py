from numpy import dot
from numpy.linalg import norm
from scipy import spatial

query_doc = [1, 2, 7, 0]
document_1 = [1, 5, 0, 0]
sim_1 = 1 - spatial.distance.cosine(query_doc, document_1)
sim_2 = dot(query_doc, document_1)/(norm(query_doc)*norm(document_1))
print(sim_1)
print(sim_2)
