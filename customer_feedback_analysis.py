def calculate_positive_feedback_percentage(python_ratings):
    if not python_ratings:  
        return 0.0
    
    positive_rating=0
    for rating in python_ratings:
        if rating>3:
            positive_rating+=1
            
    positive_percentage=(positive_rating/len(python_ratings))*100
    return positive_percentage

python_ratings = [5, 4, 3, 5, 2, 4, 1, 5]

positive_feedback_percentage = calculate_positive_feedback_percentage(python_ratings)

print(f"Positive Feedback: {positive_feedback_percentage}%")
