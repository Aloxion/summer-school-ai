Task3
================

``` r
# Load required library
# install.packages("MASS")
model_multiple = readRDS('../task2/model_multiple.rds')
library(MASS)

# Use stepAIC to select the best variables
step.model <- stepAIC(model_multiple, direction = "both", trace = FALSE)
```

    ## Warning: glm.fit: fitted probabilities numerically 0 or 1 occurred
    ## Warning: glm.fit: fitted probabilities numerically 0 or 1 occurred
    ## Warning: glm.fit: fitted probabilities numerically 0 or 1 occurred

``` r
summary(step.model)
```

    ## 
    ## Call:
    ## glm(formula = metastasis ~ Urin_ret + psa + age_at_prostate_cancer_diagnosis + 
    ##     albumin + lymphocyte + creatinine, family = "binomial", data = merged_all)
    ## 
    ## Coefficients:
    ##                                   Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)                      -7.580838   0.782646  -9.686  < 2e-16 ***
    ## Urin_ret                          1.002559   0.150634   6.656 2.82e-11 ***
    ## psa                               0.000652   0.000158   4.127 3.67e-05 ***
    ## age_at_prostate_cancer_diagnosis  0.076336   0.008799   8.676  < 2e-16 ***
    ## albumin                           0.022292   0.006214   3.587 0.000334 ***
    ## lymphocyte                        0.015576   0.004397   3.542 0.000397 ***
    ## creatinine                       -1.158552   0.490132  -2.364 0.018091 *  
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 1518.9  on 1158  degrees of freedom
    ## Residual deviance: 1306.6  on 1152  degrees of freedom
    ## AIC: 1320.6
    ## 
    ## Number of Fisher Scoring iterations: 6

``` r
# Calculate predicted probabilities from the improved model
probabilities <- predict(step.model, new_data = merged_all, type = "response")

# Create a data frame with observed and predicted classes for the confusion matrix
observed.classes <- as.factor(merged_all$metastasis)
predicted.classes <- as.factor(ifelse(probabilities >= 0.5, 1, 0))

pred.results <- data.frame(
  observed.classes,
  probabilities,
  predicted.classes
)

# Use the 'caret' package to get a detailed confusion matrix
# install.packages("caret")
library(caret)
```

    ## Loading required package: ggplot2

    ## Loading required package: lattice

``` r
confusionMatrix(data = predicted.classes, reference = observed.classes)
```

    ## Confusion Matrix and Statistics
    ## 
    ##           Reference
    ## Prediction   0   1
    ##          0 645 245
    ##          1  93 176
    ##                                           
    ##                Accuracy : 0.7084          
    ##                  95% CI : (0.6813, 0.7344)
    ##     No Information Rate : 0.6368          
    ##     P-Value [Acc > NIR] : 1.536e-07       
    ##                                           
    ##                   Kappa : 0.3166          
    ##                                           
    ##  Mcnemar's Test P-Value : < 2.2e-16       
    ##                                           
    ##             Sensitivity : 0.8740          
    ##             Specificity : 0.4181          
    ##          Pos Pred Value : 0.7247          
    ##          Neg Pred Value : 0.6543          
    ##              Prevalence : 0.6368          
    ##          Detection Rate : 0.5565          
    ##    Detection Prevalence : 0.7679          
    ##       Balanced Accuracy : 0.6460          
    ##                                           
    ##        'Positive' Class : 0               
    ## 
