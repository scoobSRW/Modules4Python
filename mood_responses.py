def mood_responses(mood):
    mood = mood.lower()
    responses = {
        'happy': "I'm glad you're feeling happy! Keep spreading the positivity!",
        'mad': "That's too bad! Let me know if you need to talk!",
        'anxious': "I'm sorry. I hope things get better for you.",
        'sad': "That's a shame! You're such an amazing person. Remember this!",
        'angry': "I'm sorry. Let me know if you'd like to talk and we can process our emotions together.",
        'tired': "Get some rest! A healthy sleep schedule is important!",
        'excited': "WOO HOO! Got anything special coming up?",
        'bored': "What a shame! Maybe end the day off doing something you love?",
        'nervous': "I'm sorry. I hope things get better for you."
    }

    return responses.get(mood, "I don't quite understand that mood. How are you feeling today?")