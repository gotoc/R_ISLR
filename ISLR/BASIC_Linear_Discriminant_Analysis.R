library(MASS)
library(ISLR)
attach(Smarket)

train=(Year<2005)   #Before 2005 is all set up as training set. 
Smarket.2005=Smarket[!train,]

lda.fit=lda(Direction~Lag1+Lag2,data=Smarket,subset=train) #Fit the training set using lda. Direction is the response
lda.pred=predict(lda.fit,Smarket.2005)#Applie fit to test set: Smarket.2005
lda.class=lda.pred$class             
table(lda.class,Direction.2005)      
mean(lda.class==Direction.2005) 
sum(lda.pred$posterior[,1]>=.5)    #Count the ones >0.5 
sum(lda.pred$posterior[,1]<.5)
lda.pred$posterior[1:20,1]
sum(lda.pred$posterior[,1]>0.9)

##################################Quaradtic Discriminant Analysis############
qda.fit=qda(Direction~Lag1+Lag2,data=Smarket,subset=train)
qda.class=predict(qda.fit,Smarket.2005)$class
table(qda.class,Direction.2005)
mean(qda.class==Direction.2005)

