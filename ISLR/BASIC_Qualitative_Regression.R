library (MASS)
library (ISLR)
fix(Carseats) 
names(Carseats)
lm.fit=lm(Sales~.+Income:Advertising +Price:Age,data=Carseats ) #Run Regression in variables including qualitative ones
contrasts(ShelveLoc)
Loadlibraries()
# Rhas created a ShelveLocGood dummy variable that takes on a value of 1 if the shelving location is good, and 0 otherwise. It has also created a ShelveLocMediumdummy variable that equals 1 if the shelving location is medium, and 0 otherwise.
