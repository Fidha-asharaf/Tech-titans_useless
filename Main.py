import random

# Define song recommendations for each mood
songs = {
    "happy": [
        "Happy - Pharrell Williams",
        "Walking on Sunshine - Katrina and the Waves",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Good Vibrations - The Beach Boys",
    ],
    "sad": [
        "Someone Like You - Adele",
        "Let Her Go - Passenger",
        "Fix You - Coldplay",
        "Tears Dry on Their Own - Amy Winehouse",
    ],
    "relaxed": [
        "Weightless - Marconi Union",
        "Sunset Lover - Petit Biscuit",
        "Lovely Day - Bill Withers",
        "Dreams - Fleetwood Mac",
    ],
    "energetic": [
        "Eye of the Tiger - Survivor",
        "Can’t Hold Us - Macklemore & Ryan Lewis",
        "Stronger - Kanye West",
        "We Will Rock You - Queen",
    ],
}

# Ask user for their current mood
def get_user_mood():
    mood = input("How are you feeling? (happy, sad, relaxed, energetic): ").strip().lower()
    return mood

# Recommend a song based on the mood
def recommend_song(mood):
    if mood in songs:
        song_choice = random.choice(songs[mood])
        print(f"Since you're feeling {mood}, I recommend: {song_choice}")
    else:
        print("Sorry, I don't have any recommendations for that mood.")

# Main program
def main():
    mood = get_user_mood()
    recommend_song(mood)

# Run the program
if __name__ == "__main__":
    main()
