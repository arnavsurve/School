eventsDF <- read.csv("/anvil/projects/tdm/data/olympics/athlete_events.csv")
head(eventsDF)
table(eventsDF$Year)
head(sort(table(eventsDF$Team), decreasing=TRUE), n=50)
length(table(eventsDF$Team))

mean(eventsDF$Height, na.rm=TRUE)
sort(tapply(eventsDF$Height, eventsDF$Team, mean, na.rm=TRUE), decreasing=TRUE)
suppressWarnings(sort(tapply(eventsDF$Age, eventsDF$Team, max, na.rm=TRUE), decreasing=TRUE))
sort(tapply(eventsDF$Weight, eventsDF$Team, sum, na.rm=TRUE), decreasing=TRUE)

deathrecordsDF <- read.csv("/anvil/projects/tdm/data/death_records/DeathRecords.csv")
str(deathrecordsDF)
head(deathrecordsDF$DayOfWeekOfDeath, n=100)
deathrecordsDF$mydays <- factor(deathrecordsDF$DayOfWeekOfDeath, levels=c(1:7,9), labels=c("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Unknown"))
head(deathrecordsDF)

tapply(deathrecordsDF$Age, deathrecordsDF$Sex, mean)
table(deathrecordsDF$MaritalStatus[deathrecordsDF$Sex == "F"])
table(deathrecordsDF$MaritalStatus[deathrecordsDF$Sex == "M"])
tapply(deathrecordsDF$MaritalStatus, deathrecordsDF$Sex, table)

plot(sort(eventsDF$Weight))
plot(deathrecordsDF$Age, deathrecordsDF$DayOfWeekOfDeath)
