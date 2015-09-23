library(ISLR)
pairs(Smarket)
attach(Smarket)

cor(Smarket[,-9]) #Cor function provides matrix that contains all of pairwise collerations among predicitons
glm.fit=glm(Direction~Lag1+Lag2+Lag3+Lag4+Lag5+Volume, data=Smarket,family=binomial)
#Run logistic regression on variables in Market dataset. family=binomial 
coef(glm.fit)
#Lag 1 Negative coefficient means: if market had positive return yesterday, it's less likely to go up today.
summary (glm.fit)$coef[,4]
glm.probs=predict(glm.fit,type="response")  
glm.probs[1:10]
#Predict function tells the probability market will go up based on P(Y=1|X). type="response".
#RUn contrasts() to find out the value means up or down
contrasts(Direction)
glm.pred=rep("Down",1250)
glm.pred[glm.probs>.5]="Up"   #Convert the probability >0.5 as Up


##########################Asess how well logistic regression held out data###################
train=(Year<2005) #train is the data prior to 2005
Smarket.2005=Smarket[!train,] #Smarket.2005 is the data which is not "Train",which means not prior to 2005
glm.fit=glm(Direction~Lag1+Lag2+Lag3+Lag4+Lag5+Volume,data=Smarket,family=binomial,subset=train)
#Fit the data prior to 2005, use logistic regression
glm.probs=predict(glm.fit,Smarket.2005,type="response")
#Use the glm.fit model to apply on Year 2005 data

debug()
contrasts(Direction.2005)  #Find out who is the default in Direction.2005 dataset
glm.pred=rep("Down",252)  #Find out who are the downs 
glm.pred[glm.probs>.5]="Up" #Define which are the ups
table(glm.pred,Direction.2005) 
mean(glm.pred==Direction.2005)      
mean(glm.pred!=Direction.2005)      #test error rate


###################Logistic Regression using two lags instead of five lags###############
glm.fit=glm(Direction~Lag1+Lag2,data=Smarket,family=binomial,subset=train)
glm.probs=predict(glm.fit,Smarket.2005,type="response")
glm.pred=rep("Down",252)
glm.pred[glm.probs>.5]="Up"
table(glm.pred,Direction.2005)
mean(glm.pred==Direction.2005)

