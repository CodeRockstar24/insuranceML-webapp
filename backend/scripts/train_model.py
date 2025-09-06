import pandas as pd
import numpy as np
import pickle
from xgboost import XGBRegressor
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_squared_error  
import os 
# Load encoded data
csv_path = r"C:\Users\elroy\OneDrive\Desktop\insuranceML\backend\data\insurance_data.csv"
data = pd.read_csv(csv_path) 
# Split features and target
X = data.drop('charges', axis=1)
y = data['charges']
# Initialize XGBoost regressor
xgb_model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

# K-Fold Cross Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
rmse_scores = []

for train_index, val_index in kf.split(X):
    X_train, X_val = X.iloc[train_index], X.iloc[val_index]
    y_train, y_val = y.iloc[train_index], y.iloc[val_index]

    xgb_model.fit(X_train, y_train)
    y_pred = xgb_model.predict(X_val)
    rmse = np.sqrt(mean_squared_error(y_val, y_pred))   # RMSE
    rmse_scores.append(rmse)

print("RMSE scores for each fold:", rmse_scores)
print("Mean RMSE:", np.mean(rmse_scores))

# Train final model on full dataset
xgb_model.fit(X, y)
# Save the trained model
model_path = r"C:\Users\elroy\OneDrive\Desktop\insuranceML\backend\model\insurance_model.pkl"
with open(model_path, 'wb') as f:
    pickle.dump(xgb_model, f) 

relative_rsme =np.mean(rmse_scores)/12110.359656
print("Relative RSME:", relative_rsme)