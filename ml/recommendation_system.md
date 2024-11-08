# Google ML Course - Recommendation System

- [link](https://developers.google.com/machine-learning/recommendation)

## Recommendations: what and why?

- home page recommendations
- related item recommendations
- item (document)
- query (context)
- embedding -> vector representation

components:

- candiate generation
- scoring
- re-ranking

## Candidate generation

- content-based filtering -> uses simlarity between items
- collaborative filtering -> uses similarities between queries and items

- map item and query to an embedding vector in embedding space E=R^d
- similarity measures s: E x E -> R s(q, x)
    - cosine similarity: s(q, x)= cos(q, x))
    - dot product: s(q, x) = q^T x
    - euclidean distance: s(q, x) = ||q-x||^2

- simlarity to movies the user has liked in the past
- movies that similar users liked
