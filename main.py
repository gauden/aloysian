import streamlit as st
import re


@st.cache_data
def load_data():
    with open("data/enable1.txt", "r") as file:
        words = file.read().splitlines()
    cleaned_words = [word for word in words]
    return cleaned_words

def main():
    st.title("Hello from pattern-matching aloysian!")

    word_list = load_data()
    
    user_input = st.text_input("Enter a regex pattern to search for words:")
    user_input = user_input.strip().replace("-", ".")

    if user_input:
        try:
            pattern = re.compile(f"^{user_input}$")
            matched_words = [word for word in word_list if pattern.search(word)]
            st.write(f"Found {len(matched_words)} words matching the pattern:")
            for word in matched_words:
                st.write(word)
        except re.error:
            st.error("Invalid regex pattern. Please try again.")


if __name__ == "__main__":
    main()
