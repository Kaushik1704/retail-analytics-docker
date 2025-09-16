import pandas as pd
from model import RetailModel

if __name__ == "__main__":
    # Sample dataset
    data = pd.DataFrame({
        'store_traffic': [100, 150, 200, 250],
        'sales': [500, 700, 900, 1100]
    })

    X = data[['store_traffic']]
    y = data['sales']

    model = RetailModel()
    model.train(X, y)
    model.save()
    print("✅ Model trained and saved!")
