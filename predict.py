import pandas as pd
import lightgbm as lb
from graphs import Graph


def train(self, x, y):
    x = x
    y = y
    model = lb.LGBMClassifier(
        boosting_type="gbdt",
        n_jobs=-1,
        learning_rate=0.0003,
        random_state=41,
        n_estimators=300,
    )
    model.fit()
    predict = model.predict(10)
    return predict
