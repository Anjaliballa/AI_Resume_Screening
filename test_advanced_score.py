from recommender.similarity import calculate_final_score


score = calculate_final_score(
    90,
    100,
    80,
    0
)


print("Final Match Score:", score)