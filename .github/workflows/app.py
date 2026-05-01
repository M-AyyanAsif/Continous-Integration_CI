import streamlit as st

# Define functions first (so they can be tested)
def square_func(n):
    return n ** 2

def cube_func(n):
    return n ** 3

def fifth_power_func(n):
    return n ** 5

# This block ensures the UI only runs when you run "streamlit run app.py"
if __name__ == "__main__":
    st.title("Power Calculator")
    st.write("Enter a number to calculate its square, cube, and fifth power.")

    n = st.number_input("Enter an integer", value=1, step=1)

    # Use the functions for calculations
    st.write(f"The square of {n} is: {square_func(n)}")
    st.write(f"The cube of {n} is: {cube_func(n)}")
    st.write(f"The fifth power of {n} is: {fifth_power_func(n)}")