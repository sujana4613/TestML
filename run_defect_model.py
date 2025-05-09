# -*- coding: utf-8 -*-
"""
Created on Fri May  9 00:11:26 2025

@author: sujan
"""

#This file is getting called from pre-commit hook, calling our trained model

#!/usr/bin/env python3
import subprocess
import joblib
import numpy as np
import sys

# Load ML model and vectorizer
try:
    model = joblib.load(r"C:\IITH_AIML\Python\programs\defect_model.pkl")
    vectorizer = joblib.load(r"C:\IITH_AIML\Python\programs\vectorizer.pkl")
except Exception as e:
    print(f"Could not load model/vectorizer: {e}")
    sys.exit(0)

# Get staged diff
diff_text = subprocess.getoutput("git diff")[:1000]
print(diff_text)

# If there's no diff, allow commit
if not diff_text.strip():
    print("No staged changes detected. Commit allowed.")
    sys.exit(0)

# Vectorize the diff
text_feat = vectorizer.transform([diff_text]).toarray()

# Predict
pred = model.predict(text_feat)[0]


if pred == 1:
    print("High risk of bug detected — commit blocked.")
    sys.exit(1)
else:
    print("Low risk — commit allowed.")
    sys.exit(0)
