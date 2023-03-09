library(data.table)
myDF <- fread("/anvil/projects/tdm/data/election/escaped/itcont2020sample.txt")
head(myDF)
benfords_law <- function(digit) { log((digit+1)/digit)/log(10) }
benfords_law(1)
digits <- 1:9
digits
plot(sapply(digits, benfords_law))

options(jupyter.rich_display = F)
options(repr.matrix.max.cols=25, repr.matrix.max.rows=200)
head(myDF)
firstdigit <- table(substr(myDF$TRANSACTION_AMT, 1, 1))[3:11]
plot(firstdigit)

myDF$Employed <- TRUE
myDF$Employed[myDF$EMPLOYER == "NOT EMPLOYED"] <- FALSE
myDF$Employed[myDF$OCCUPATION == "NOT EMPLOYED"] <- FALSE
table(myDF$Employed)
myemployerfunction <- function(tempDF) {
    tempDF$Employed <- TRUE
    tempDF$Employed[myDF$EMPLOYER == "NOT EMPLOYED"] <- FALSE
    tempDF$Employed[myDF$OCCUPATION == "NOT EMPLOYED"] <- FALSE
    return(tempDF)
}
head(myemployerfunction(myDF))
table(myemployerfunction(myDF)$Employed)

myemployerfunction <- function(tempDF) { # Function has 1 argument
    tempDF$Employed <- TRUE # Set Employed column with default values true
    tempDF$Employed[myDF$EMPLOYER == "NOT EMPLOYED"] <- FALSE # If employer was not employed, set index to false
    tempDF$Employed[myDF$OCCUPATION == "NOT EMPLOYED"] <- FALSE # If occupation was not employed, set index to false
    return(tempDF)
}
plot(table(myemployerfunction(myDF)$Employed))

head(myDF)
head(myDF$STATE, n=50)
caRatio <- function(tempDF, includes) {
    tempDF$state <- FALSE
    tempDF$state[myDF$STATE == 'CA'] <- includes
    return(tempDF)
}
table(caRatio(myDF, TRUE))