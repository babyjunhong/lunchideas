import random
import streamlit as st

# ----- List of 100 Lunch Ideas (Singapore / Chinatown) -----
LUNCH_IDEAS = [
    "Chicken Rice", "Laksa", "Char Kway Teow", "Hainanese Pork Chop", "Bak Kut Teh",
    "Wanton Mee", "Chilli Crab", "Fish Head Curry", "Nasi Lemak", "Roti Prata",
    "Mee Goreng", "Fried Hokkien Mee", "Beef Hor Fun", "Satay", "Yong Tau Foo",
    "Bak Chor Mee", "Claypot Chicken Rice", "Curry Chicken Bee Hoon", "Braised Duck", "Fried Carrot Cake",
    "Sambal Stingray", "Popiah", "Mee Siam", "Fried Oyster Omelette", "Kway Chap",
    "Teochew Porridge", "Chwee Kueh", "Hokkien Mee", "Lor Mee", "Roast Duck",
    "Curry Puff", "Chicken Curry", "Fried Bee Hoon", "Mee Rebus", "Chap Chye",
    "Rojak", "Kway Teow Soup", "Nasi Padang", "Fried Rice", "Claypot Tofu",
    "Fried Fish", "Braised Pork Belly", "Popiah Goreng", "Mee Soto", "Dry Mee Siam",
    "Vegetarian Bee Hoon", "Fish Soup", "Prawn Mee", "Kway Teow Char", "Rendang Chicken",
    "Mee Pok", "Kolo Mee", "Bak Kut Teh Soup", "Oyster Mee Hoon", "Fried Noodles",
    "Fried Rice Vermicelli", "Sliced Fish Soup", "Curry Fish Head", "Chicken Satay", "Laksa Soup",
    "Prawn Omelette", "Grilled Stingray", "Sambal Chicken", "Fried Wanton", "Mee Hoon Soup",
    "Yam Ring", "Fried Chicken Cutlet", "Braised Beef Brisket", "Curry Vegetable", "Steamed Fish",
    "Roast Pork", "Black Pepper Chicken", "Fried Tofu", "Popiah Salad", "Curry Squid",
    "Singapore Fried Mee Tai Mak", "Fried Carrot Cake Black", "Chicken Satay Skewers", "Sweet and Sour Fish",
    "BBQ Pork Char Siew", "Dim Sum Platter", "Fried Prawn Roll", "Fried Rice with Salted Egg", "Nasi Goreng Kampung",
    "Fried Chicken Wings", "Claypot Laksa", "Chilli Pan Mee", "Spicy Tofu", "Mee Soto Ayam",
    "Curry Mee", "Seafood Hor Fun", "Roti John", "Beef Rendang", "Mee Hoon Kway",
    "Vegetarian Curry", "Fried Hokkien Prawn Mee", "Roast Chicken", "Fish Ball Noodles", "Mee Pok Dry"
]

# ----- Streamlit Interface -----
# Custom CSS for button, font, and lunch box
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed&display=swap');

/* Center button */
div.stButton > button {
    display: block;
    margin: 0 auto;
    width: 200px;
    height: 50px;
    background-color: #FFC0CB;
    color: black;
    font-size: 18px;
    font-family: 'Roboto Condensed', sans-serif;
    border-radius: 5px;
}

.title {
    font-family: 'Roboto Condensed', sans-serif;
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
}
.sub-title {
    font-family: 'Roboto Condensed', sans-serif;
    font-size: 32px;
    color: #555555;
    text-align: center;
    margin-bottom: 40px;
}
.lunch-box {
    font-family: 'Roboto Condensed', sans-serif;
    font-size: 28px;
    text-align: center;
    margin-top: 20px;
    padding: 20px;
    background-color: #FFDEE9;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Titles
st.markdown("<div class=\"title\">🍴 LETS LUNCH!</div>", unsafe_allow_html=True)

# Centered GO! button
if st.button("What should we have for lunch!"):
    lunch_choice = random.choice(LUNCH_IDEAS)
    st.markdown(f'<div class="lunch-box">{lunch_choice}</div>', unsafe_allow_html=True)
