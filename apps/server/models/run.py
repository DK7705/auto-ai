import joblib
import inspect
import numpy as np
import pandas as pd

model = joblib.load("./0a7e7df2c106604cc39aacbf.joblib")

if hasattr(model, "steps"):
    print("Pipeline steps:")
    for step_name, step_obj in model.steps:
        print(f"Step name: {step_name}")
        print(f"Step type: {type(step_obj).__name__}")
        print(f"Step object: {step_obj}\n")
else:
    print("Model is not a pipeline.")

