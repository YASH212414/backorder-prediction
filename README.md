# backorder-prediction

1. **Data Preparation:**
   - Combined training and test datasets for cross-validation.
   - Recoded binary variables as 0/1 for consistency.

2. **Handling Class Imbalance:**
   - Utilized oversampling and undersampling techniques from the Imbalanced-Learn (imblearn) library.
     - Oversampling techniques: Synthetic Minority Oversampling Technique (SMOTE), Adaptive Synthetic sampling (ADASYN).
     - Undersampling techniques: Near miss under sampling, Tomek link, Under sampling with cluster centroids, Under Sampling with Neighbourhood Cleaning rule.

3. **Feature Engineering:**
   - Dropped the 'sku' column as it is a unique identifier.
   - Handled missing values using median imputation.
   - Handled positive skewness in data using different techniques like log transform + normalization and Robust Scalar.

4. **Model Building and Hyperparameter Tuning:**
   - Built classification models using algorithms like Logistic Regression, Decision Trees, Random Forest, K-Nearest Neighbors, Gaussian Naive Bayes, and XGBoost.
   - Performed hyperparameter tuning for Decision Tree using GridSearchCV.
   - Utilized Randomized Search CV to find the best hyperparameters for Random Forest and XGBoost.
   - Applied cross-validation for K-Nearest Neighbors and Gaussian Naive Bayes.

5. **Model Evaluation:**
   - Evaluated each model's performance using metrics like accuracy, precision, recall, and AUC-ROC.
   - Visualized confusion matrices for each model.

6. **Summary and Analysis:**
   - Created a DataFrame (df_evaluation) to summarize the performance metrics of all models.
   - Analyzed the significance of precision and recall in the context of these classifiers.
   - Identified the classifier with the highest precision, recall, and AUC-ROC scores.
   - Discussed the importance of these metrics in various scenarios, such as fraud detection, medical diagnosis, and security threats.

By following these steps, you systematically prepared the data, built various classifiers, tuned their hyperparameters, evaluated their performance, and analyzed the results to draw meaningful insights.
