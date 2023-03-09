list.files("/anvil/projects/tdm/data/disney")
myDF <- read.csv("/anvil/projects/tdm/data/disney/7_dwarfs_train.csv", stringsAsFactors = TRUE)
head(myDF, n=21)
dim(myDF)
str(myDF)

table(myDF$SPOSTMIN, useNA="always")
sum(is.na(myDF$SPOSTMIN))

## Kernel throwing error, solved by rereading csv into myDF again
myDF <- read.csv("/anvil/projects/tdm/data/disney/7_dwarfs_train.csv", stringsAsFactors=TRUE)
newDF <- subset(myDF, !is.na(myDF$SPOSTMIN))
head(newDF, n=50)

length(myDF$date[myDF$date == "12/25/2021"])
mean(myDF$SACTMIN[myDF$date == "12/25/2021"], na.rm=TRUE)
mean(myDF$SACTMIN[myDF$date == "05/26/2021"], na.rm=TRUE)

head(myDF)

jul4DF <- myDF$SPOSTMIN[substr(myDF$date, 0, 5) == "07/04" & myDF$SPOSTMIN != -999]
nyDF <- myDF$SPOSTMIN[substr(myDF$date, 0, 5) == "01/01"]
christmasDF <- myDF$SPOSTMIN[substr(myDF$date, 0, 5) == "12/25"]

mean(na.omit(jul4DF))
mean(na.omit(nyDF))
mean(na.omit(christmasDF))

summary(myDF$date)

length(myDF$SPOSTMIN)
length(newDF$SPOSTMIN)

myhours <- (myDF$SPOSTMIN + newDF$SPOSTMIN)/60
head(myhours)
length(myhours)

newDF$SPOSTMIN[1]/60
myDF$SPOSTMIN[313997]/60
myhours[313997]

library(lubridate)
myDF$weekday <- wday(myDF$datetime, label=TRUE)
head(sort(myDF$SACTMIN))
mean(myDF$SACTMIN[myDF$weekday=="Mon" & myDF$SACTMIN!=-92918], na.rm=TRUE)
mean(myDF$SACTMIN[myDF$weekday=="Tue" & myDF$SACTMIN!=-92918], na.rm=TRUE)
mean(myDF$SACTMIN[myDF$weekday=="Wed" & myDF$SACTMIN!=-92918], na.rm=TRUE)
mean(myDF$SACTMIN[myDF$weekday=="Thu" & myDF$SACTMIN!=-92918], na.rm=TRUE)
mean(myDF$SACTMIN[myDF$weekday=="Fri" & myDF$SACTMIN!=-92918], na.rm=TRUE)
mean(myDF$SACTMIN[myDF$weekday=="Sat" & myDF$SACTMIN!=-92918], na.rm=TRUE)
mean(myDF$SACTMIN[myDF$weekday=="Sun" & myDF$SACTMIN!=-92918], na.rm=TRUE)

summary((myDF$weekday))

chartvals <- tapply(myDF$SACTMIN[myDF$SACTMIN != -92918], myDF$weekday[myDF$SACTMIN != -92918], mean, na.rm=TRUE)
chartvals

dotchart(chartvals)
plot(chartvals)
