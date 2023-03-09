options(jupyter.rich_display = F)
options(repr.matrix.max.cols=25, repr.matrix.max.rows=200)
library(data.table)
users <- fread("/anvil/projects/tdm/data/okcupid/filtered/users.csv")
questions <- fread("/anvil/projects/tdm/data/okcupid/filtered/questions.csv")
dim(users)
head(users)
dim(questions)
head(questions)


dim(questions)
head(questions)
grep("Google", questions$text)
questions[2172, ]
questions$text[grepl("Google", questions$text)]


dim(users)
head(users)
which(names(users) == "q170849")
users[ , 1193]
prop.table(table(users[[1193]], useNA="always"))


head(users[[2282]])
tapply(users[[1193]], users[[2282]], table)
tapply(users[[1193]], users[[2282]], function(x) {prop.table(table(x, useNA="always"))})

table(gsub("_[A-Va-z]*", "", users$gender_orientation))