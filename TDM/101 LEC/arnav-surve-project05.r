myDF <- read.csv("/anvil/projects/tdm/data/election/escaped/itcont2020sample.txt", sep="|")
head(myDF)

class(myDF$TRANSACTION_DT)
library(lubridate, warn.conflicts=FALSE)
myDF$newdates <- mdy(myDF$TRANSACTION_DT)
head(myDF$newdates)
myresults <- tapply(myDF$TRANSACTION_DT, myDF$newdates, sum)
head(myresults)
plot(sort(unique(myDF$newdates)), myresults)

newDF <- subset(myDF, (newdates >= mdy("01/01/2019")) & (newdates <= mdy("05/15/2019")))
dim(myDF)
dim(newDF)
mynewresults <- tapply(newDF$TRANSACTION_DT, newDF$newdates, sum)
plot(sort(unique(newDF$newdates)), mynewresults)

v <- tapply(myDF$TRANSACTION_AMT, myDF$STATE, sum)
sort(v)
myDF$citystatepair <- paste(myDF$CITY, myDF$STATE, sep=',')
head(myDF$citystatepair)
w <- tapply(myDF$TRANSACTION_AMT, myDF$citystatepair, sum)
tail(sort(w, decreasing=TRUE), n=50)
class(myDF$NAME)
sum(myDF$TRANSACTION_AMT[grepl(", MARY", myDF$NAME)])
notemployed <- sum(myDF$TRANSACTION_AMT[myDF$EMPLOYER == "NOT EMPLOYED"], na.rm=TRUE)
employed <- sum(myDF$TRANSACTION_AMT[myDF$EMPLOYER == "EMPLOYED"], na.rm=TRUE)
v <- c(employed, notemployed)
names(v) <- c("EMPLOYED", "NOT EMPLOYED")
barplot(v)
v
head(sort(tapply(myDF$TRANSACTION_AMT, myDF$OCCUPATION, sum), decreasing=TRUE))
ceo <- subset(myDF, myDF$OCCUPATION == "CEO")
plot(ceo$TRANSACTION_AMT)
