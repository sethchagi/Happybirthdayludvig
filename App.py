import streamlit as st
import os

# 1. Page Config
st.set_page_config(page_title="Happy Birthday Ludvig!", page_icon="🎉", layout="centered")

# 2. State Management
if "entered" not in st.session_state:
    st.session_state.entered = False
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# 3. The Story Data (Using direct web URLs so they NEVER break)
slides = [
    {
        "text": "He is a 6 ft tall, funky, and dorky man with such glorious, blonde hairs.",
        "img": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3E1c29kM3M3bWd6YWN4Z3B5dG9yZ3M0a3N6bHJqMmZyZmR6ZWU1NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13GjU3w8TfS7U4/giphy.webp" 
    },
    {
        "text": "He is smart. But he is so much more, he is a bright student, driven, and disciplined.",
        "img": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2pxbnhyMndyMndwMHR5aHN6dTN0Z3p6bzNweW11MjQ5b2Y4Z3Y0ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uBnnM9HktV5z0RkZgH/giphy.webp"
    },
    {
        "text": "He is someone you can depend on. A person who will be there for you through tough times, be patient with you, and listen to you. Or maybe just to me (haha).",
        "img": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2Q1bXZtZDN5M2ZzeHl6bXZzZ3M0NXJ6dDczeDRqYmJxbzZ1YnZ3biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/J0wePT3A0O1HCH901I/giphy.webp"
    },
    {
        "text": "He got annoyed pretty easily but he said having me around with him doesn’t annoy him as much (hehe). But this actually kinda another reason why we go well together bc I love being angry. He gets that anger and I don’t feel weird and alone when I am angry.",
        "img": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHJzY3R5M2M1NzJxdWV6NWV4cXZxcWN6ZWQxeGFwcjM5aHpydHZqMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKrEzvPNBgWEigM/giphy.webp"
    },
    {
        "text": "He is someone who sits with my mess and still talks to it in the softest way.",
        "img": "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXZ6eXQxNjQydDN1ZDRxdHJrNThxdTZqZ3RpeHByM2txZXJmZXVvMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vsyKKf1t22nmw/giphy.webp"
    },
    {
        "text": "I don’t really need AI for I have him when I am curious about some silly things.",
        "img": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXV5YXQ2enU5d3l6ZnIzbXd4ZWd0bW10eG8yMnB6ZXR5bWp2cndwMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fVnv2w8kHxxq1yq7L8/giphy.webp"
    },
    {
        "text": "He is the “Well, actually…” guy and I don’t mind at all. He thought that’s annoying, but I can learn a ton from his “Well, actually..”",
        "img": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Z6Z3Q3N3B6NXU5MzF1MnhxZXZ0eWc4dTNteWV6N3B6cWl2eGFvNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/U2nN0ridM4lXy/giphy.webp"
    },
    {
        "text": "He is a person with the strongest will and the gentlest heart.",
        "img": "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHZ2azV1aDNyeDV5ZHg4eHV3bnd6dnhwbXR6ZnJ5a3VwYm16em43bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/W7N21x0xEMlC8/giphy.webp"
    },
    {
        "text": "Now that you have met him, please be kinder to him.",
        "img": ""
    },
    {
        "text": "Please give him a little break and don’t let his head stuck in his ass.",
        "img": ""
    },
    {
        "text": "Please give him a little clap in each of his wins, big or small.",
        "img": ""
    }
]

# 4. Super Funky Centered CSS
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Quicksand:wght@700&display=swap');

/* Hide Streamlit clutter */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Funky Polka Dot Background using his favorite colors */
.stApp {
    background-color: #fefae0;
    background-image: radial-gradient(#bc6c25 3px, transparent 3px), radial-gradient(#bc6c25 3px, transparent 3px);
    background-size: 60px 60px;
    background-position: 0 0, 30px 30px;
}

/* Chunky, perfectly centered text boxes */
.story-box {
    background-color: #588157; /* Green */
    color: #fefae0;
    border: 5px solid #3a5a40; /* Darker Green */
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    font-family: 'Quicksand', sans-serif;
    font-size: 26px;
    font-weight: 700;
    box-shadow: 10px 10px 0px #f4e04d; /* Yellow shadow */
    margin: 20px auto;
}

.intro-title {
    font-family: 'Caveat', cursive;
    color: #bc6c25;
    font-size: 60px;
    text-align: center;
    text-shadow: 3px 3px 0px #f4e04d;
    margin-bottom: 20px;
}

.bday-title {
    font-family: 'Caveat', cursive;
    color: #fefae0;
    font-size: 70px;
    text-align: center;
    margin-bottom: 0px;
}

/* Force Streamlit buttons to be perfectly centered */
div.stButton {
    display: flex;
    justify-content: center;
}

div.stButton > button:first-child {
    background-color: #f4e04d;
    color: #3a5a40;
    font-family: 'Caveat', cursive;
    font-size: 30px;
    border: 4px solid #bc6c25;
    border-radius: 50px;
    padding: 10px 50px;
    box-shadow: 5px 5px 0px #3a5a40;
    transition: all 0.2s ease;
}

div.stButton > button:first-child:hover {
    transform: translateY(4px);
    box-shadow: 1px 1px 0px #3a5a40;
    background-color: #bc6c25;
    color: #fefae0;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# 5. Logic
if not st.session_state.entered:
    # Dead center spacing for the intro
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<div class='intro-title'>Ready to meet Ludvig?</div>", unsafe_allow_html=True)
    if st.button("ENTER THE CHAOS"):
        st.session_state.entered = True
        st.rerun()

else:
    # BULLETPROOF AUDIO PLAYER
    # This checks if the file exists first. If it doesn't, it skips the audio so the app doesn't crash!
    if os.path.exists("jazz.mp3"):
        st.audio("jazz.mp3", format="audio/mpeg", autoplay=True)
        st.caption("🎵 Click play if the jazz doesn't start automatically!")
    else:
        st.warning("⚠️ Heads up: Streamlit couldn't find 'jazz.mp3' in your GitHub. Check the spelling/capitalization! But the show must go on...")
    
    current_idx = st.session_state.slide_index
    
    if current_idx < len(slides):
        slide_data = slides[current_idx]
        
        # Text Box
        st.markdown(f"<div class='story-box'>{slide_data['text']}</div>", unsafe_allow_html=True)
        
        # Perfectly Centered Image
        if slide_data["img"]:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(slide_data["img"], use_container_width=True)
                
        # Spacing
        st.write("")
        
        # Next Button
        if st.button("Next"):
            st.session_state.slide_index += 1
            st.rerun()
            
    else:
        # Grand Finale
        st.balloons() # Triggers Streamlit's built in balloon animation!
        st.markdown("""
        <div class='story-box' style='background-color: #bc6c25; border-color: #f4e04d; box-shadow: 10px 10px 0px #3a5a40;'>
            <div class='bday-title'>HAPPY 26TH BIRTHDAY, LUDVIG!</div>
            <p style='font-size: 35px; margin-top: 10px;'>I love you.</p>
        </div>
        """, unsafe_allow_html=True)
