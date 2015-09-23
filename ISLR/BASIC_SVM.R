set.seed(1)
x=matrix(rnorm(20*2),ncol=2)
y=c(rep(-1,10),rep(1,10))
x[y==1,]=x[y==1,]+1
dat=data.frame(x=x,y=as.factor(y))
library(e1071)
svmfit=svm(y~.,data=dat,kernel="linear",cost=1,scale=FALSE)  
plot(svmfit,dat)        #plot the svm line 
tune.out=tune(svm,y~.,data=dat,kernel="linear",ranges=list(cost=c(0.001,0.01,0.1,1.5,10,100)))
summary(tune.out) #access cross-validation errors of each models
bestmod=tune.out$best.model
summary(bestmod)                       #Choose the best model based on generated data 
  #Use the model to predict class label of following test results


#Generate random dataset used to predict
xtest=matrix(rnorm(20*2),ncol=2)
ytest=sample(c(-1,1),20,rep=TRUE)
xtest[ytest==1,]=xtest[ytest==1,]+1   #when the row has 1 in ytest, add 1
testdat=data.frame(x=xtest,y=as.factor(ytest)) 
ypred=predict(bestmod,testdat)                   #Apply bestmod on testdata
table(predict=ypred,truth=testdat$y)


#########################SVM on non-linear boundary**************************
set.seed(1)
x=matrix(rnorm(200*2),ncol=2)
x[1:100,]=x[1:100,]+2
x[101:150,]=x[101:150,]-2
y=c(rep(1,150),rep(2,50))
dat=data.frame(x=x,y=as.factor(y))
train=sample(200,100)
svmfit=svm(y~.,data=dat[train,],kernel="radial",gamma=1,cost=1e5) #increase cost leading to irregular shape
plot(svmfit,dat[train,])
set.seed(1)
tune.out=tune(svm,y~.,data=dat[train,],kernel="radial",ranges=list(cost=c(0.1,1,10,100,1000),gamma=c(0.5,1,2,3,4))) #Cross-Validation to test different Cost/Gamma combinations
summary(tune.out)   
bestmod=tune.out$best.model                       
table(true=dat[-train,"y"],pred=predict(bestmod,newx=dat[-train,]))  #apply the bestmod on data

#################################SVM with multiple classes#########################
set.seed(1)
x=rbind(x,matrix(rnorm(50*2),ncol=2))
y=c(y,rep(0,50))
x[y==0,2]=x[y==0,2]+2
dat=data.frame(x=x,y=as.factor(y))
par(mfrow=c(1,1))                             #Arranging plots
plot(x,col=(y+1))
svmfit=svm(y~.,data=dat,kernel="radial",cost=10,gamma=1)
plot(svmfit,dat)
############################SVM with Gene Expression####################################
library(ISLR)
names(Khan)
dat=data.frame(x=Khan$xtrain,y=as.factor(Khan$ytrain))
out=svm(y~.,data=dat,kernel="linear",cost=10)                      #train the data
dat.te=data.frame(x=Khan$xtest,y=as.factor(Khan$ytest))
pred.te=predict(out,newdata=dat.te)
table(pred.te,dat.te$y)