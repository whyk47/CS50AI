# Shopping Purchase Prediction Documentation

### Overview
This project involves building an AI model to predict whether online shopping customers will complete a purchase. The model uses a k nearest-neighbor classifier to predict a user's purchasing intent based on their session data, such as pages visited, browsing time, and other user attributes.

### Usage
1. Install the scikit-learn package
2. Run `shopping.py`, specifying the data file.
```bash
$ pip install scikit-learn
$ python shopping.py shopping.csv
```
This will:
1. Load the data from shopping.csv.
2. Train a KNN classifier on the data.
3. Evaluate the model's performance using sensitivity and specificity metrics.
4. Output the results: correct predictions, incorrect predictions, true positive rate, and true negative rate.

### Example Output
```bash
Correct: 4088
Incorrect: 844
True Positive Rate: 41.02%
True Negative Rate: 90.55%
```

### Evaluation Metrics
- True Positive Rate (Sensitivity): The proportion of users who made a purchase and were correctly identified by the classifier.
- True Negative Rate (Specificity): The proportion of users who did not make a purchase and were correctly identified by the classifier.
