list.files("/anvil/projects/tdm/data/craigslist")
myDF <- read.csv("/anvil/projects/tdm/data/craigslist/vehicles.csv", stringsAsFactors = TRUE)

options(repr.matrix.max.cols=25, repr.matrix.max.rows=200)
options(jupyter.rich_display=F)
head(myDF)

head(myDF$region, n=50)
unique(myDF$region)
length(myDF$year[myDF$year>=2011])
table(myDF$year)

table(myDF$condition, useNA="always")
myDF$newflag <- NA
myDF$newflag[myDF$condition == "like new"] <- TRUE
myDF$newflag[myDF$condition != "like new"] <- FALSE
table(myDF$newflag, useNA="always")

myDF$pricecategory <- NA
myDF$pricecategory[myDF$price <= 1500] <- "cheap"
myDF$pricecategory[(myDF$price > 1500) & (myDF$price <= 10000)] <- "average"
myDF$pricecategory[myDF$price > 10000] <- "expensive"
table(myDF$pricecategory, useNA="always")

table(myDF$newflag)
myDF$newpricecategory <- cut(myDF$price, breaks = c(-Inf,1500,10000,Inf), labels=c("cheap", "average", "expensive"))
head(myDF$newpricecategory)
sum(myDF$newpricecategory != myDF$pricecategory)
myDF$odometerage <- cut(myDF$odometer, breaks=c(-Inf,5000,10000,Inf), labels=c("new", "middle age", "old"))
table(myDF$odometerage, useNA="no")

myIndy <- subset(myDF, (region=="indianapolis")&(!is.na(long))&(!is.na(lat)))
dim(myIndy)
head(sort(table(myDF$region), decreasing=TRUE))
popularRegion <- subset(myDF, region=="springfield")
dim(popularRegion)
myRegion <- subset(myDF, region=="bend")
dim(myRegion)

library(leaflet)
library(sf)
options(jupyter.rich_display = T)
points <- st_as_sf(myIndy, coords=c("long", "lat"), crs=4326)
addCircleMarkers(addTiles(leaflet(myIndy)), radius=1)
addCircleMarkers(addTiles(leaflet(popularRegion)), radius=1)
addCircleMarkers(addTiles(leaflet(myRegion)), radius=1)
