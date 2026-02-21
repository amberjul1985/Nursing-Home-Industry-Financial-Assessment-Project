import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve

df = pd.read_csv("FinalClean_151.csv")
df_numeric = df.select_dtypes(include='number')

X = df_numeric.drop(columns=['Score_High'])
y = df_numeric['Score_High']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_train_pred = rf_model.predict(X_train)
rf_test_pred = rf_model.predict(X_test)
rf_test_proba = rf_model.predict_proba(X_test)[:, 1]

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_train_pred = dt_model.predict(X_train)
dt_test_pred = dt_model.predict(X_test)
dt_test_proba = dt_model.predict_proba(X_test)[:, 1]

lr_model = LogisticRegression(max_iter=2000)
lr_model.fit(X_train, y_train)
lr_train_pred = lr_model.predict(X_train)
lr_test_pred = lr_model.predict(X_test)
lr_test_proba = lr_model.predict_proba(X_test)[:, 1]

models = ['RandomForest', 'DecisionTree', 'LogisticRegression']
train_accuracies = [accuracy_score(y_train, rf_train_pred),
                    accuracy_score(y_train, dt_train_pred),
                    accuracy_score(y_train, lr_train_pred)]
test_accuracies = [accuracy_score(y_test, rf_test_pred),
                   accuracy_score(y_test, dt_test_pred),
                   accuracy_score(y_test, lr_test_pred)]
auroc_scores = [roc_auc_score(y_test, rf_test_proba),
                roc_auc_score(y_test, dt_test_proba),
                roc_auc_score(y_test, lr_test_proba)]
results_df = pd.DataFrame({'Model': models,
                           'Training Accuracy': [f"{x:.4f}" for x in train_accuracies],
                           'Testing Accuracy': [f"{x:.4f}" for x in test_accuracies],
                           'AUROC Score': [f"{x:.4f}" for x in auroc_scores]})
# Print the table
print("Model Performance Comparison:")
print(results_df)
