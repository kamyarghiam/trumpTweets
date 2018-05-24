#project by Saransh Chopra and Kamyar Ghiam 

                  
import google.cloud.language
from trumpTweets import makeList

def analyze_sentiment(L):
    day_count=0
    day_total=0
    day_mag=0
    night_count=0
    night_total=0
    night_mag=0

    # Create a Language client.
    language_client = google.cloud.language.LanguageServiceClient()

    for i in range(len(L)):
        text = L[i][0]

        document = google.cloud.language.types.Document(
        content=text,
        type=google.cloud.language.enums.Document.Type.PLAIN_TEXT)

        # Use Language to detect the sentiment of the text.
        response = language_client.analyze_sentiment(document=document)
        sentiment = response.document_sentiment

        if (L[i][1] == "day"):
            day_count+=1
            day_total+=sentiment.score
            day_mag+=sentiment.magnitude
        else:
            night_count+=1
            night_total+=sentiment.score
            night_mag+=sentiment.magnitude
        print(i)

    day_avg_sentiment=day_total/day_count
    day_avg_mag=day_mag/day_count
    night_avg_sentiment=night_total/night_count
    night_avg_mag=night_mag/night_count

    return (day_avg_sentiment,day_avg_mag,night_avg_sentiment,night_avg_mag)

print(analyze_sentiment(makeList()))           
            