Task4
================

``` r
# Load required library
library(caret)
```

    ## Loading required package: ggplot2

    ## Loading required package: lattice

``` r
library(dplyr)
```

    ## 
    ## Attaching package: 'dplyr'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

``` r
# Convert the outcome variable to a factor
merged_all$metastasis <- factor(merged_all$metastasis)

# Set up the ten-fold cross-validation
train.control <- trainControl(
  method = "cv",  
  number = 10,   
  savePredictions = TRUE
)

set.seed(123) # Set a seed for reproducibility

# Train the final model using cross-validation
# Ensure the outcome is a factor
final.model.cv <- train(
  metastasis ~ Urin_ret + psa + age_at_prostate_cancer_diagnosis + albumin + lymphocyte + creatinine, 
  data = merged_all,
  method = "glm",
  family = "binomial",
  trControl = train.control
)
```

    ## Warning: glm.fit: fitted probabilities numerically 0 or 1 occurred
    ## Warning: glm.fit: fitted probabilities numerically 0 or 1 occurred
    ## Warning: glm.fit: fitted probabilities numerically 0 or 1 occurred
    ## Warning: glm.fit: fitted probabilities numerically 0 or 1 occurred

``` r
# Summarize the results of the cross-validation
print(final.model.cv)
```

    ## Generalized Linear Model 
    ## 
    ## 1159 samples
    ##    6 predictor
    ##    2 classes: '0', '1' 
    ## 
    ## No pre-processing
    ## Resampling: Cross-Validated (10 fold) 
    ## Summary of sample sizes: 1043, 1043, 1043, 1042, 1043, 1044, ... 
    ## Resampling results:
    ## 
    ##   Accuracy  Kappa    
    ##   0.708354  0.3136131

``` r
# Inspect the results for each fold
pred_fold <- final.model.cv$pred

# Now the 'pred' and 'obs' columns will be factors, and the confusionMatrix
# function should work as expected.
confusionMatrix(data = pred_fold$pred, reference = pred_fold$obs)
```

    ## Confusion Matrix and Statistics
    ## 
    ##           Reference
    ## Prediction   0   1
    ##          0 648 248
    ##          1  90 173
    ##                                           
    ##                Accuracy : 0.7084          
    ##                  95% CI : (0.6813, 0.7344)
    ##     No Information Rate : 0.6368          
    ##     P-Value [Acc > NIR] : 1.536e-07       
    ##                                           
    ##                   Kappa : 0.3143          
    ##                                           
    ##  Mcnemar's Test P-Value : < 2.2e-16       
    ##                                           
    ##             Sensitivity : 0.8780          
    ##             Specificity : 0.4109          
    ##          Pos Pred Value : 0.7232          
    ##          Neg Pred Value : 0.6578          
    ##              Prevalence : 0.6368          
    ##          Detection Rate : 0.5591          
    ##    Detection Prevalence : 0.7731          
    ##       Balanced Accuracy : 0.6445          
    ##                                           
    ##        'Positive' Class : 0               
    ## 

``` r
# You can also re-run the accuracy calculation per fold:
pred_fold$equal <- ifelse(pred_fold$pred == pred_fold$obs, 1, 0)
eachfold_accuracy <- pred_fold %>%
  group_by(Resample) %>%
  summarise(Accuracy = mean(equal))

print(eachfold_accuracy)
```

    ## # A tibble: 10 × 2
    ##    Resample Accuracy
    ##    <chr>       <dbl>
    ##  1 Fold01      0.793
    ##  2 Fold02      0.724
    ##  3 Fold03      0.698
    ##  4 Fold04      0.709
    ##  5 Fold05      0.707
    ##  6 Fold06      0.687
    ##  7 Fold07      0.672
    ##  8 Fold08      0.672
    ##  9 Fold09      0.713
    ## 10 Fold10      0.707

``` r
# Evaluate the model's predictive performance on the cross-validated results
confusionMatrix(data = as.factor(pred_fold$pred), reference = as.factor(pred_fold$obs))
```

    ## Confusion Matrix and Statistics
    ## 
    ##           Reference
    ## Prediction   0   1
    ##          0 648 248
    ##          1  90 173
    ##                                           
    ##                Accuracy : 0.7084          
    ##                  95% CI : (0.6813, 0.7344)
    ##     No Information Rate : 0.6368          
    ##     P-Value [Acc > NIR] : 1.536e-07       
    ##                                           
    ##                   Kappa : 0.3143          
    ##                                           
    ##  Mcnemar's Test P-Value : < 2.2e-16       
    ##                                           
    ##             Sensitivity : 0.8780          
    ##             Specificity : 0.4109          
    ##          Pos Pred Value : 0.7232          
    ##          Neg Pred Value : 0.6578          
    ##              Prevalence : 0.6368          
    ##          Detection Rate : 0.5591          
    ##    Detection Prevalence : 0.7731          
    ##       Balanced Accuracy : 0.6445          
    ##                                           
    ##        'Positive' Class : 0               
    ## 
