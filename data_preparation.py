import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier

from sklearn.model_selection import cross_validate, ShuffleSplit
from sklearn.metrics import classification_report, mean_squared_error

splitter = ShuffleSplit(n_splits=3, test_size=0.25, random_state=0)

def scores(X_train, y_train, X_test, y_test, model):

    model.fit(X_train, y_train)
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)
    
    baseline_scores = cross_validate(
        estimator=model,
        X=X_train,
        y=y_train,
        return_train_score=True,
        cv=splitter
    )
    
    print(model)
    print("")
    print("CV score:     {:.2%}".format(baseline_scores["test_score"].mean()))
    print("X-test score: {:.2%}".format(model.score(X_test, y_test)))
    print("RMSE:         {:.4}".format(mean_squared_error(y_test, y_hat_test, squared=False)))
    print("")
    print("Train score")
    print(classification_report(y_train, y_hat_train))
    
    print("")
    print("")
    print("X-test score")

    print("")
    print(classification_report(y_test, y_hat_test))
    
    print("")
    print("")
    
    pass