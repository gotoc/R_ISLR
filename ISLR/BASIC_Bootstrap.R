library(boot)

alpha.fn=function(data,index){
  X=data$X[index]
  Y=data$Y[index]
  return ((var(Y)-cov(X,Y))/(var(X)+var(Y)-2*cov(X,Y)))
}

alpha.fn(Portfolio,1:100) #estimate alpha using 100 observations

set.seed(1)
alpha.fn(Portfolio,sample(100,100,replace=T))  
#Randomly select 100 obs from range 1 to 100 with replacement; 
#construct a bootstrap and recompute alpha based on new data set
boot(Portfolio,alpha.fn,R=1000)
#Boot function automated function 1000

boot.fn=function (data,index)
  return (coef(lm(mpg~horsepower,data=data,subset=index)))  
#use boot.fn function to create bootstrap estimate for intercept & slope by randomly sampling from among observation with replacements

set.seed(1)
boot.fn(Auto,sample(392,392,replace=T))
