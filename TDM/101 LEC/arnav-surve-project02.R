myDF <- read.csv("/anvil/projects/tdm/data/flights/subset/1995.csv", stringsAsFactors = TRUE)
dim(myDF)
head(myDF)
str(myDF)

#takes the selected information from the dataframe and puts it into a new vector called `myairports`
myairports <- myDF$Origin
summary(myairports)

departs <- myDF$Origin
head(departs, n=250)
summary(departs)

arrivals <- myDF$Dest
summary(arrivals)

head(departs[894])
head(arrivals[894])

dist <- myDF$Distance[myDF$Distance < 200]
length(dist)

sort(table(myDF$UniqueCarrier))

tail(sort(table(myDF$TailNum)), n=11)

deptimes <- head(myDF$DepTime, n=350)
plot(deptimes, cex=1.3)
