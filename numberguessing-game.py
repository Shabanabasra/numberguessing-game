import streamlit as st
import random

# Initialize session state variables
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(50, 100)
    st.session_state.attempts_taken = 0
    st.session_state.max_attempts = 5

# Streamlit UI
st.title("🎯 Number Guessing Game")
st.write("Guess a number between **50 and 100**.")
st.write(f"You have **{st.session_state.max_attempts - st.session_state.attempts_taken}** attempts left.")

# User input
user_guess = st.number_input("Enter your guess:", min_value=50, max_value=100, step=1, format="%d")

if st.button("Submit Guess"):
    st.session_state.attempts_taken += 1  # Increment attempts

    if user_guess == st.session_state.number_to_guess:
        st.success(f"🎉 Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts_taken} attempts!")
        st.session_state.number_to_guess = random.randint(50, 100)  # Reset game
        st.session_state.attempts_taken = 0
    elif st.session_state.attempts_taken >= st.session_state.max_attempts:
        st.error(f"😢 Out of attempts! The number was {st.session_state.number_to_guess}. Try again!")
        st.session_state.number_to_guess = random.randint(50, 100)  # Reset game
        st.session_state.attempts_taken = 0
    elif user_guess > st.session_state.number_to_guess:
        st.warning("Your guess is **too high**! Try again.")
    else:
        st.warning("Your guess is **too low**! Try again.")

# Show attempts taken
st.write(f"Attempts used: **{st.session_state.attempts_taken}/{st.session_state.max_attempts}**")