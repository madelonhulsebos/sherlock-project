from unittest import TestCase
from sherlock.features.paragraph_vectors import tokenise, initialise_nltk, infer_paragraph_embeddings_features, \
    initialise_pretrained_model
import pandas as pd
from collections import OrderedDict
from tests.test_helper import assert_category_keys

DIM = 400


class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        initialise_nltk()
        initialise_pretrained_model(DIM)

    def test_tokenise(self):
        series = pd.Series(['$', 'B', 'Aab$', '$$ca', 'C$B$', 'cat', '-0.12'])

        result = tokenise(series)

        assert result == ['aab', 'ca', 'cb', 'cat', '012']

    def test_infer_paragraph_embeddings_features(self):
        s = pd.Series(['$', 'B', 'Aab$', '$$ca', 'C$B$', 'cat'])

        features = OrderedDict()

        infer_paragraph_embeddings_features(s, features, DIM, True)

        assert_category_keys('par', features)
