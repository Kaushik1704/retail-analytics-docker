from src.model import RetailModel
import numpy as np

def test_prediction():
    model = RetailModel()
    model.model.coef_ = np.array([2.0])
    model.model.intercept_ = 0
    pred = model.predict([[10]])
    assert pred[0] == 20
