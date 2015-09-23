library(MASS)
library(ISLR)
library(class)
train=(Year<2005)
train.X=cbind(Lag1,Lag2)[train,]  #Use cbine to combine the Lag1, Lag2 leg
test.X=cbind(Lag1,Lag2)[!train,]
train.Direction=Direction[train]

set.seed(1)
knn.pred=knn(train.X,test.X,train.Direction,k=1)   #Apply Knn,set k=1
table(knn.pred,Direction.2005)

knn.pred=knn(train.X,test.X,train.Direction,k=3)   #Apply Knn, set k=3
table(knn.pred,Direction.2005)
mean(knn.pred==Direction.2005)
