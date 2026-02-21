import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score

# -------------------------------
# Load and preprocess data
# -------------------------------
df = pd.read_csv("FinalClean_151.csv")
df_numeric = df.select_dtypes(include='number')

# -------------------------------
# Manually select features
# -------------------------------
# selected_features = [
#     # ⬇️ Add the column names you want here
#     'survey_rating', 'DeficiencyCount', 'quality_rating', 'staffing_rating', 'cmplnt_cnt']

selected_features = ['DeficiencyCount',
                     'quality_rating', 'staffing_rating', 'adj_total']

# Define X and y
X = df_numeric[selected_features]
y = df_numeric['Score_High']

# -------------------------------
# Train/test split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Scale the Data
# -------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -------------------------------
# Train Models
# -------------------------------
# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_train_pred = rf_model.predict(X_train)
rf_test_pred = rf_model.predict(X_test)
rf_test_proba = rf_model.predict_proba(X_test)[:, 1]

# Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_train_pred = dt_model.predict(X_train)
dt_test_pred = dt_model.predict(X_test)
dt_test_proba = dt_model.predict_proba(X_test)[:, 1]

# Logistic Regression
lr_model = LogisticRegression(max_iter=5000, solver='saga')
lr_model.fit(X_train_scaled, y_train)
lr_train_pred = lr_model.predict(X_train_scaled)
lr_test_pred = lr_model.predict(X_test_scaled)
lr_test_proba = lr_model.predict_proba(X_test_scaled)[:, 1]

# -------------------------------
# Evaluate and Compare Models
# -------------------------------
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

results_df = pd.DataFrame({
    'Model': models,
    'Training Accuracy': [f"{x:.4f}" for x in train_accuracies],
    'Testing Accuracy': [f"{x:.4f}" for x in test_accuracies],
    'AUROC Score': [f"{x:.4f}" for x in auroc_scores]
})

# Print the results
print("\nModel Performance Comparison:")
print(results_df)
