library (MASS)
library (ISLR)
fix(Boston)  #Show data in spradsheet-liked
names (Boston)  #Show items
attach(Boston)
lm.fit=lm(medv~lstat) #Conduct linear regression
summary(lm.fit)  #Summary of the linear regression
coef(lm.fit)  #Access the result of linear regression intercept & coefficient
confint(lm.fit)  #Obtain confidence interval for the coefficient estimates
plot(lstat,medv)
abline(lm.fit)  #plot the lm.fit result
par(mfrow=c(2,2))   #splitting the result into four different parts,dividing into 2x2 panels
plot(lm.fit) 
lm.fit=lm(medv~lstat+age,data=Boston)  #Multiple Regression   >summary(lm.fit)
summary(lm.fit)$r.sq   #show R-squared
summary(lm.fit)$sigma  #show RSE
lm.fit1=lm(medv~.-age,data=Boston) #Run multiple regression with all variables BUT one, taking high p-value out
summary(lm(medv~lstat*age,data=Boston)) #include interaction lstat*age
lm.fit2=lm(medv~lstat+age+I(lstat^2))  #Regression on non-linear variable.  medv/lstat/lstat^2
anova(lm.fit,lm.fit2) # Analysis of variance table, H0:two regressions are equivalently good/ H1: the second is better. p-value too small, reject H0
lm.fit5=lm(medv~poly(lstat,5)) #Shows the result of 5th order polynomial regression
lm.log=lm(medv~log(rm),data=Boston) #log transformation in Regression




