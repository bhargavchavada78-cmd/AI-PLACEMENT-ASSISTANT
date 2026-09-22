def calculate_confidence(
        answer_score,
        speech_score_value,
        video_score
):
    confidence = (
        answer_score * 0.45

        +

        speech_score_value * 0.35

        +

        video_score * 0.20
    )
    return round(
        confidence,
        2
    )

def  confidence_label(score):
    if score >= 80:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"
def confidence_feedback(score):
    if score>=80:
        return "Excellent performance! You have demonstrated strong confidence in your answers and delivery."
    elif score>=50:
        return "good performance! You have shown a decent level of confidence, but there is room for improvement." 
    else:
        return "Needs improvement. Consider practicing your answers and delivery to boost your confidence."
          
    