library(ISLR)
fix(Hitters)
sum(is.na(Hitters$Salary))        #how many entries are N/A
Hitters=na.omit(Hitters)          #Omit N/As
sum(is.na(Hitters$Salary))        #How many N/A now?

library(leaps)          
regfit.full=regsubsets(Salary~.,Hitters)        #regsubset function performs the best subset selection
summary(regfit.full)                            #best is qualified using RSS here
reg.summary=summary(regfit.full)
names(reg.summary)
reg.summary$rsq

par(mfrow=c(2,2))
plot(reg.summary$rss,xlab="Number of variables",ylab="RSS",type="l")        #Plot RSS
plot(reg.summary$adjr2,xlab="Number of Variables",ylab="Adjusted Rsq",type="l")  #Plot Adjusted Rsquared
which.max(reg.summary$adjr2)
points(8,reg.summary$adjr2[8],col="red",cex=2,pch=20)  #Print the point in the line
coef(regfit.full,6)

regfit.fwd=regsubsets(Salary~.,data=Hitters,nvmax=19,method="forward")

