import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Happy Birthday Lui!", page_icon="🎉", layout="centered")

# 2. The Complete Story Data (Nothing missing!)
story_blocks = [
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
    }
]

# 3. New Aesthetic CSS (Monét, Better Fonts, Readable Text)
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Boogaloo&family=Outfit:wght@400;700&display=swap');

/* Hide Streamlit clutter */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Monét Japanese Bridge Background with a dark overlay to make text pop */
.stApp {
    background: linear-gradient(rgba(58, 90, 64, 0.85), rgba(88, 129, 87, 0.85)), 
                url('https://upload.wikimedia.org/wikipedia/commons/3/33/Claude_Monet_-_Water_Lilies_and_Japanese_Bridge_-_1899.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Beautiful, clean text boxes */
.story-card {
    background-color: rgba(254, 250, 224, 0.95); /* Soft yellow-white */
    border-left: 8px solid #bc6c25; /* Brown accent line */
    border-radius: 15px;
    padding: 30px;
    margin-bottom: 40px;
    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.3);
}

.story-text {
    font-family: 'Outfit', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #3a5a40; /* Dark Green */
    line-height: 1.6;
    text-align: center;
}

/* Funky Headers */
.main-title {
    font-family: 'Boogaloo', cursive;
    color: #f4e04d; /* Yellow */
    font-size: 65px;
    text-align: center;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
    margin-bottom: 40px;
    margin-top: 20px;
}

.bday-title {
    font-family: 'Boogaloo', cursive;
    color: #bc6c25;
    font-size: 70px;
    text-align: center;
    line-height: 1.1;
}

/* Audio Player Styling */
audio {
    width: 100%;
    margin-bottom: 30px;
    border-radius: 10px;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# 4. The Page Content
st.markdown("<div class='main-title'>Let's Meet Lui...</div>", unsafe_allow_html=True)

# Guaranteed Jazz Audio Player (Using a live web link so it never fails)
st.markdown("""
<audio autoplay controls>
  <source src="https://cdn.pixabay.com/download/audio/2022/01/18/audio_d0a13f69d2.mp3?filename=smooth-jazz-114705.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
""", unsafe_allow_html=True)
st.caption("🎷 Press play for some Jazz!")
st.write("---")

# Render all the Pokemon/Story Blocks seamlessly
for block in story_blocks:
    st.markdown(f"""
    <div class='story-card'>
        <div class='story-text'>{block["text"]}</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(block["img"], use_container_width=True)
    st.write("<br>", unsafe_allow_html=True)

st.write("---")

# The Conclusion Messages
st.markdown("""
<div class='story-card' style='border-left: 8px solid #588157;'>
    <div class='story-text'>Now that you have met him, please be kinder to him.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='story-card' style='border-left: 8px solid #588157;'>
    <div class='story-text'>Please give him a little break and don’t let his head stuck in his ass.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='story-card' style='border-left: 8px solid #588157;'>
    <div class='story-text'>Please give him a little clap in each of his wins, big or small.</div>
</div>
""", unsafe_allow_html=True)

# The Grand Finale
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class='story-card' style='background-color: #f4e04d; border-left: 8px solid #bc6c25; box-shadow: 0px 10px 20px rgba(0,0,0,0.5);'>
    <div class='bday-title'>HAPPY 26TH BIRTHDAY, LUI!</div>
    <div class='story-text' style='font-size: 35px; margin-top: 15px;'>I love you.</div>
</div>
""", unsafe_allow_html=True)

# The Balloon Button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🎈 Click for Birthday Magic! 🎈"):
        st.balloons()
