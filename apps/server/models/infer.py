import joblib
import inspect
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import GradientBoostingClassifier

# Load the model
model = joblib.load("./0a7e7df2c106604cc39aacbf.joblib")

# ---- Test Case 1: Check pipeline steps ----
assert hasattr(model, "steps"), "Model should be a pipeline"
assert isinstance(model, Pipeline), "Model should be of type Pipeline"

expected_steps = ["preprocessor", "model"]
assert [name for name, _ in model.steps] == expected_steps, "Pipeline step names mismatch"

print("Test Case 1 Passed: Pipeline steps and names are correct.")

# ---- Test Case 2: Check preprocessor is a ColumnTransformer ----
preprocessor = model.named_steps["preprocessor"]
assert isinstance(preprocessor, ColumnTransformer), "Preprocessor should be ColumnTransformer"
assert len(preprocessor.transformers) == 2, "Preprocessor should have two transformers"

print("Test Case 2 Passed: Preprocessor is ColumnTransformer with correct transformers.")

# ---- Test Case 3: Check numerical transformer pipeline ----
num_transformer = preprocessor.transformers_[0][1]
assert isinstance(num_transformer, Pipeline), "Numerical transformer should be Pipeline"
num_steps = [type(step).__name__ for _, step in num_transformer.steps]
assert num_steps == ["SimpleImputer", "StandardScaler"], "Numerical transformer steps mismatch"

print("Test Case 3 Passed: Numerical transformer pipeline is correct.")

# ---- Test Case 4: Check categorical transformer pipeline ----
cat_transformer = preprocessor.transformers_[1][1]
assert isinstance(cat_transformer, Pipeline), "Categorical transformer should be Pipeline"
cat_steps = [type(step).__name__ for _, step in cat_transformer.steps]
assert cat_steps == ["SimpleImputer", "OneHotEncoder"], "Categorical transformer steps mismatch"

print("Test Case 4 Passed: Categorical transformer pipeline is correct.")

# ---- Test Case 5: Check model type ----
final_model = model.named_steps["model"]
assert isinstance(final_model, GradientBoostingClassifier), "Final model should be GradientBoostingClassifier"
assert final_model.max_depth == 5, "Model max_depth should be 5"
assert final_model.random_state == 42, "Model random_state should be 42"

print("Test Case 5 Passed: Model type and parameters are correct.")

# ---- Test Case 6: Check transformation output shape ----
sample_data = pd.DataFrame({
    "CustomerID": [9999, 1],
    "Age": [45, 18],  # older vs younger
    "Tenure": [60, 1],  # long tenure vs new customer
    "Usage Frequency": [30, 1],  # frequent vs rare usage
    "Support Calls": [0, 10],  # no support calls vs many complaints
    "Payment Delay": [0, 15],  # no delays vs long delays
    "Total Spend": [5000.0, 10.0],  # very high spend vs very low
    "Last Interaction": [1, 365],  # recent vs long ago
    "Gender": ["Female", "Male"],
    "Subscription Type": ["Premium", "Basic"],
    "Contract Length": ["24 Months", "1 Month"]
})

transformed = preprocessor.transform(sample_data)
assert transformed.shape[0] == 2, "Transformed output row count should match input"
print(f"Test Case 6 Passed: Transformation output shape is {transformed.shape}")

# ---- Test Case 7: Check model prediction works ----
predictions = model.predict(sample_data)
assert predictions.shape[0] == 2, "Prediction output size should match input rows"
print(f"Test Case 7 Passed: Model predictions successful -> {predictions}")
