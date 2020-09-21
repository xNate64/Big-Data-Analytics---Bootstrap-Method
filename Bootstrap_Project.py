import pandas as pd
import numpy as np


### Question 9 ###
###a
#Calculate sample mean
df3 = pd.read_csv('Boston.csv', index_col=0).dropna()
mu_hat = np.mean(df3.medv)
print("The sample mean is " + str(mu_hat))

###b
#Calculate sample standard error
se_muhat = np.std(df3.medv) / (len(df3.medv)**0.5)
print("The standard error of the sample mean is " + str(se_muhat))

###c
#Estimate the standard error of the sample mean
sample_list = [0] * 1000
np.random.seed(16)
for i in range (1,1000):
        df3sample = df3.sample(frac=1, replace=True)
        sample_list[i-1] = np.mean(df3sample.medv)
        
error=0
for i in range(1,1000):
    error += (sample_list[i-1] - np.mean(df3sample.medv))**2

total_error = ((1/999)*error)**0.5
print("The standard error of the sample mean using bootstrap is " + str(total_error))  

print("The differece of the standard errors is " + str(total_error - se_muhat))

###d
#Create a 95% CI for the standard error of the sample mean
mu_CI_L = mu_hat - 2*total_error
mu_CI_U = mu_hat + 2*total_error 
print("A 95% confidence interval for mu using the bootstrap method is " + str(mu_CI_L) + " to " + str(mu_CI_U))

print("A 95% confidence interval for mu using the calcualted standard error is " + str(mu_hat - 2*se_muhat) + " to " + str(mu_hat + 2*se_muhat))

###e
#calculate the sample median
med_hat = np.median(df3.medv)
print("The sample median is " + str(med_hat))   
 
###f
#Calculate the standard error of the sample median using bootstrap
np.random.seed(256)
for i in range (1,1000):
        df3sample = df3.sample(frac=1, replace=True)
        sample_list[i-1] = np.median(df3sample.medv)
  
np.median(sample_list)      

error=0
for i in range(1, 1000):
    error += (sample_list[i-1] - np.median(df3sample.medv))**2 

total_error = ((1/999)*error)**0.5
print("The estimated standard error of the sample mean using bootstrap is " + str(total_error))

###g
#Calcuate 10th percentile
print("The 10th percentile is " + str(np.percentile(df3.medv,10)))

###h
#Calcuate the standard error of the sample 10th percentile
np.random.seed(1024)
for i in range (1,1000):
        df3sample = df3.sample(frac=1, replace=True)
        sample_list[i-1] = np.percentile(df3sample.medv, 10)
  
sample_list  
error=0
for i in range(1,1000):
    error += (sample_list[i-1] - np.percentile(df3sample.medv,10))**2 


total_error = ((1/999)*error)**0.5
print("The estimated standard error of the sample 10th percentile using bootstrap is " + str(total_error))

