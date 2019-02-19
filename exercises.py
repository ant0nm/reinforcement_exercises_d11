# exercise 1 - emotions
human_emotions = {"happiness": 2, "sadness": 1, "fear": 2, "anger": 1,
                    "surprise": 3, "disgust": 1, "shame": 1}
# print out the emotions
for emotion, degree in human_emotions.items():
    print("{} felt at level {}".format(emotion, degree))
