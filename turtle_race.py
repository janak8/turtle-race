import streamlit as st
import random
import time

# Turtle colors and initialization
colors = ["🟥 Red", "🟧 Orange", "🟨 Yellow", "🟩 Green", "🟦 Blue", "🟪 Purple"]
turtle_positions = {color: 0 for color in colors}  # Track progress of each "turtle"
race_started = False

# Game Title and Instructions
st.title("Turtle Race Game 🐢")
st.write("Place your bet on a turtle and watch it race to the finish line!")

# User input for the bet
user_bet = st.selectbox("Which turtle will win the race? Pick a color:", colors)

# Start the race button
if st.button("Start Race"):
    race_started = True

if race_started:
    st.write("The race has started! 🏁")
    placeholders = {color: st.empty() for color in colors}  # Placeholders for each "turtle"

    # Simulate the race
    winner = None
    while not winner:
        for color in colors:
            turtle_positions[color] += random.randint(1, 10)  # Random step forward
            placeholders[color].text(f"{color}: {'🐢' * (turtle_positions[color] // 10)}")  # Show progress
            if turtle_positions[color] >= 140:  # Race ends when one turtle reaches 100
                winner = color
                break
        time.sleep(0.3)  # Add a delay for animation effect

    # Announce the winner
    if winner == user_bet:
        st.success(f"🎉 You've won! The {winner} turtle is the winner!")
    else:
        st.error(f"😢 You've lost! The {winner} turtle is the winner!")

    # Reset positions for a new race
    turtle_positions = {color: 0 for color in colors}
