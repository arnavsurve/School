options(jupyter.rich_display = F)
options(repr.matrix.max.cols=100, repr.matrix.max.rows=200)
library(data.table)

county <- fread("/anvil/projects/tdm/data/zillow/County_time_series.csv")
dim(county)
library(lubridate)
month(head(county$Date))
day(head(county$Date))
year(head(county$Date))
county$month <- month(county$Date)
county$day <- day(county$Date)
county$year <- year(county$Date)
head(county)
county$mdy <- paste0(county$month, "/", county$date, "/", county$year, "/")
length(table(county$year))
v <- tapply(county$MedianListingPricePerSqft_3Bedroom, county$year, mean, na.rm=TRUE)
w <- tapply(county$MedianListingPricePerSqft_1Bedroom, county$year, mean, na.rm=TRUE)
plot(names(v), v, type="l", ylim=c(0,300))
lines(names(w), w, type="l")

dim(county)
names(county)[grep("ier", names(county))]
head(county$ZHVI_BottomTier)
head(county$ZHVI_MiddleTier)
head(county$ZHVI_TopTier)
tapply(county$ZHVI_TopTier, county$year, mean, na.rm=TRUE)
v <- tapply(county$ZHVI_TopTier, county$year, mean, na.rm=TRUE)
plot(names(v), v, type="l")
tapply(county$ZHVI_BottomTier, county$year, mean, na.rm=TRUE)["2014"]
mean(county$ZHVI_BottomTier[county$year == "2014"], na.rm=TRUE)
tapply(county$ZHVI_MiddleTier, county$year, mean, na.rm=TRUE)["2010"]
mean(county$ZHVI_MiddleTier[county$year == "2010"], na.rm=TRUE)

v <- tapply(county$ZHVI_TopTier, county$year, mean, na.rm=TRUE)
v
w <- tapply(county$ZHVI_MiddleTier, county$year, mean, na.rm=TRUE)
w
x <- tapply(county$ZHVI_BottomTier, county$year, mean, na.rm=TRUE)
x
plot(names(v), v, type="l", ylim=c(0,300000))
lines(names(w), w, type="l")
lines(names(x), x, type="l")

v <- tapply(county$ZHVI_TopTier, county$month, mean, na.rm=TRUE)
w <- tapply(county$ZHVI_MiddleTier, county$month, mean, na.rm=TRUE)
x <- tapply(county$ZHVI_BottomTier, county$month, mean, na.rm=TRUE)
plot(names(v), v, type="l", ylim=c(0,250000))
lines(names(w), w, type="l")
lines(names(x), x, type="l")