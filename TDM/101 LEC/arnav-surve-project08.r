library(data.table)
titles <- data.frame(fread("/anvil/projects/tdm/data/movies_and_tv/titles.csv"))
episodes <- data.frame(fread("/anvil/projects/tdm/data/movies_and_tv/episodes.csv"))
people <- data.frame(fread("/anvil/projects/tdm/data/movies_and_tv/people.csv"))
ratings <- data.frame(fread("/anvil/projects/tdm/data/movies_and_tv/ratings.csv"))

table(titles$is_adult)
head(titles)

counts <- table(titles$is_adult, titles$type)
head(counts)

barplot(counts, main="Title Distribution by Adult Rating and Type of Media",
  xlab="Type of Movie", col=c("darkblue","red"),
  legend = rownames(counts), beside=TRUE)

plot(table(titles$premiered))


find_movie_with_at_least_rating <- function(titles_df, ratings_df, ratings_of_at_least) {
    results <- merge(ratings_df, titles_df, by.x = "title_id", by.y = "title_id")
    popular_movie_results <- results[results$type == "movie" & results$rating >= ratings_of_at_least, ]
    return(popular_movie_results)
}


find_movie_with_at_least_rating <- function(titles_df, ratings_df, ratings_of_at_least) { # Create a function that takes titles_df, ratings_df, and ratings_of_at_least as parameters
    results <- merge(ratings_df, titles_df, by.x = "title_id", by.y = "title_id") # Merge ratings_df and titles_df rows where their title IDs match
    popular_movie_results <- results[results$type == "movie" & results$rating >= ratings_of_at_least, ] # Assign movies with a minimum rating to popular_movie_results
    return(popular_movie_results) # Return popular movie results as output of function
}

my_selection <- find_movie_with_at_least_rating(titles, ratings, 7.6)
dim(my_selection)

find_movie_with_max_rating <- function(titles_df, ratings_df, ratings_max) {
    results <- merge(ratings_df, titles_df, by.x = "title_id", by.y = "title_id")
    popular_movie_results <- results[results$type == "movie" & results$rating < ratings_max, ]
    return(popular_movie_results)
}

max_selection <- find_movie_with_max_rating(titles, ratings, 5.0)
dim(max_selection)


find_highest_rating <- function(titles, ratings, genre) {
    results <- merge(ratings, titles, by.x = "title_id", by.y = "title_id")
    popular_movie_results <- results[results$type == "movie" & results$genres == genre, ]
    most_popular <- popular_movie_results[popular_movie_results$rating == max(popular_movie_results$rating), ]
    return(most_popular)
}

comedyDF <- find_highest_rating(titles, ratings, "Comedy")
comedyDF