import streamlit as st

class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0

teams = [
    Team("India"),
    Team("Australia"),
    Team("England"),
    Team("New Zealand"),
    Team("South Africa")
]

# Simulating some match results
results = [
    ("India", "Australia", "win"),  # India wins against Australia
    ("England", "New Zealand", "win"),  # England wins against New Zealand
    ("South Africa", "India", "win"),  # South Africa wins against India
    ("Australia", "England", "loss"),  # Australia loses against England
    ("New Zealand", "South Africa", "loss")  # New Zealand loses against South Africa
]

# Updating team points based on match results
for team1, team2, result in results:
    if result == "win":
        for team in teams:
            if team.name == team1:
                team.points += 2
            elif team.name == team2:
                team.points += 1
    elif result == "loss":
        for team in teams:
            if team.name == team1:
                team.points += 1
            elif team.name == team2:
                team.points += 2

# Sorting teams based on points
teams.sort(key=lambda x: x.points, reverse=True)

# Streamlit app
def main():
    st.title("ICC Ranking App")

    # Home page - ICC ranking
    st.header("ICC Ranking Table:")
    st.table({"Team": [f"{i}. {team.name}" for i, team in enumerate(teams, start=1)],
              "Points": [team.points for team in teams]})
# Company logo
    st.sidebar.image("icc.png", use_column_width=True)
    # About us page
    st.markdown("## About Us")
    st.write("("welcome to our website we give info about ICC TEAM RANKING")

    # Contact us page
    st.markdown("## Contact Us")
    st.write("For more info contact onthis email ahmedrayyan9713@gamil.com")

if __name__ == "__main__":
    main()
