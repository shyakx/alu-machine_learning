# Word Embeddings

Word embeddings are a type of word representation that allows words to be represented as vectors in a continuous vector space. They capture semantic and syntactic relationships between words, enabling machines to understand text more effectively.

## Key Concepts

- **Vector Representation:** Each word is mapped to a high-dimensional vector.
- **Semantic Similarity:** Words with similar meanings have vectors that are close together.
- **Dimensionality Reduction:** Embeddings reduce the complexity of representing words compared to one-hot encoding.

## Popular Word Embedding Techniques

- **Word2Vec:** Predicts context words from a target word (Skip-gram) or vice versa (CBOW).
- **GloVe:** Uses global word-word co-occurrence statistics to learn embeddings.
- **FastText:** Extends Word2Vec by representing words as bags of character n-grams.

## Applications

- Text classification
- Sentiment analysis
- Machine translation
- Information retrieval

## Example Usage (Python with Gensim)

```python
from gensim.models import Word2Vec

sentences = [["machine", "learning", "is", "fun"], ["word", "embeddings", "capture", "meaning"]]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

vector = model.wv['machine']
similar_words = model.wv.most_similar('learning')
```

## References

- [Word2Vec Paper](https://arxiv.org/abs/1301.3781)
- [GloVe Paper](https://nlp.stanford.edu/pubs/glove.pdf)
- [Gensim Documentation](https://radimrehurek.com/gensim/)
