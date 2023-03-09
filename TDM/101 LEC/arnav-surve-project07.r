library(data.table)

titles <- data.frame(fread("/anvil/projects/tdm/data/movies_and_tv/titles.csv"))
episodes <- data.frame(fread("/anvil/projects/tdm/data/movies_and_tv/episodes.csv"))
people <- data.frame(fread("/anvil/projects/tdm/data/movies_and_tv/people.csv"))
ratings <- data.frame(fread("/anvil/projects/tdm/data/movies_and_tv/ratings.csv"))

options(jupyter.rich_display = F)
head(titles)
head(episodes)
head(people)
head(ratings)
unique(unlist(strsplit(unique(titles$genres), ",")))
sort(table(titles[grepl("Comedy", titles$genres), ]$premiered), decreasing=TRUE)


resultDF <- merge(episodes, titles, by.x = "episode_title_id", by.y = "title_id")
head(resultDF)
dim(resultDF[resultDF$show_title_id == "tt0108778", ])
tempDF <- resultDF[resultDF$show_title_id == "tt0108778", ]
head(tempDF)
anotherDF <- head(merge(tempDF, titles, by.x = "show_title_id", by.y = "title_id"))
yetanotherDF <- merge(anotherDF, ratings, by.x = "episode_title_id", by.y = "title_id")
friendsDF <- merge(yetanotherDF, ratings, by.x = "show_title_id", by.y = "title_id")[ , c("primary_title.x", "primary_title.y", "rating.x", "rating.y")]
head(friendsDF)
names(friendsDF) <- c("episode_title", "show_title", "episode_rating", "show_rating")
head(friendsDF)
tail(friendsDF[order(friendsDF$episode_rating), ], n=7)


names(friendsDF) <- c("episode_title", "show_title", "episode_rating", "show_rating")
head(friendsDF)
season_number = 5
friendsDF[ (friendsDF$episode_rating > 9) & (friendsDF$season_number == 5), ]
subset(friendsDF, (friendsDF$episode_rating > 9) & (friendsDF$season_number == 5))
