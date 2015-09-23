library(ISLR)
glm.fit=glm(mpg~horsepower,data=Auto)  #if family=binomial, then its a logistic regression, otherwise, its just a linear regression
coef(glm.fit)
#We use glm not lm, becos we need to use cv.glm later to perform LOOCV
library(boot)
glm.fit=glm(mpg~horsepower,data=Auto)
cv.err=cv.glm(Auto,glm.fit)
cv.err$delta  #It produces the LOOCV statistic 

##################Use LOOCV to test polynomial regression#############
cv.error=rep(0,5)
for (i in 1:5){
  glm.fit=glm(mpg~poly(horsepower,i),data=Auto)
  cv.error[i]=cv.glm(Auto,glm.fit)$delta[1]
}

