# credit_score_data
## Multi-Class Classification Model
This project focuses on building a multi-class classification model to predict the credit score category (Standard, Poor, or Good) based on a set of customer features.

## Steps Taken
1. Data Preprocessing
Dropped high cardinality and redundant features such as ID, Customer_ID, Name, and SSN.
For the high cardinality Type_of_Loan column, applied the following:
Kept the column due to its predictive potential.
Set a threshold of 60, labeling values below this as 'multiple_loans'.
Applied frequency encoding, transforming the column into integer values.
2. Model Building
Decision Tree Classifier:
Added one-hot encoding for categorical variables in the pipeline.
Addressed overfitting with hyperparameter tuning using random search (scoring='f1_samples' for imbalanced, multiclass dataset).
Applied feature selection using SelectFromModel (threshold = 'median') after analyzing feature importances.
Random Forest Classifier:
Built a Random Forest model and repeated the same process (feature selection + hyperparameter tuning).
Achieved the following improvements:
Accuracy: 0.69 → 0.72
Matthews Correlation Coefficient (MCC): 0.484 → 0.552
F1 Scores: Greater than 0.6 for all classes
3. Model Evaluation
Test Data Performance:

Accuracy: 0.73
MCC: 0.569
Key Insights:

The MCC on test data is slightly higher than on train data, indicating good generalization.
The small difference between training and test performance suggests stability and no significant overfitting.
The higher MCC on the test set suggests the model is learning general patterns effectively.
Conclusion
The Random Forest classifier is performing well, achieving strong generalization on unseen data, and providing valuable insights into customer credit scores.
