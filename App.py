import streamlit as st

# 1. Page Configuration (Must be the first command)
st.set_page_config(page_title="Happy Birthday Ludvig!", page_icon="🎉", layout="centered")

# 2. State Management (This remembers where the user is in the story)
if "entered" not in st.session_state:
    st.session_state.entered = False
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# 3. The Story Data (Giani's text and Pokémon GIFs)
slides = [
    {
        "text": "He is a 6 ft tall, funky, and dorky man with such glorious, blonde hairs.",
        "img": "https://media.giphy.com/media/13GjU3w8TfS7U4/giphy.gif" # Replace with actual favorites
    },
    {
        "text": "He is smart. But he is so much more, he is a bright student, driven, and disciplined.",
        "img": "https://media.giphy.com/media/uBnnM9HktV5z0RkZgH/giphy.gif"
    },
    {
        "text": "He is someone you can depend on. A person who will be there for you through tough times, be patient with you, and listen to you. Or maybe just to me (haha).",
        "img": "https://media.giphy.com/media/J0wePT3A0O1HCH901I/giphy.gif"
    },
    {
        "text": "He got annoyed pretty easily but he said having me around with him doesn’t annoy him as much (hehe). But this actually kinda another reason why we go well together bc I love being angry. He gets that anger and I don’t feel weird and alone when I am angry.",
        "img": "https://media.giphy.com/media/3o7TKrEzvPNBgWEigM/giphy.gif"
    },
    {
        "text": "He is someone who sits with my mess and still talks to it in the softest way.",
        "img": "https://media.giphy.com/media/vsyKKf1t22nmw/giphy.gif"
    },
    {
        "text": "I don’t really need AI for I have him when I am curious about some silly things.",
        "img": "https://media.giphy.com/media/fVnv2w8kHxxq1yq7L8/giphy.gif"
    },
    {
        "text": "He is the “Well, actually…” guy and I don’t mind at all. He thought that’s annoying, but I can learn a ton from his “Well, actually..”",
        "img": "https://media.giphy.com/media/U2nN0ridM4lXy/giphy.gif"
    },
    {
        "text": "He is a person with the strongest will and the gentlest heart.",
        "img": "https://media.giphy.com/media/W7N21x0xEMlC8/giphy.gif"
    },
    {
        "text": "Now that you have met him, please be kinder to him.",
        "img": "" # No image for conclusion slides
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

# 4. Custom CSS Injection for the Chaos, Colors, and Monét Vibe
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Quicksand:wght@500;700&display=swap');

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Base Font */
html, body, [class*="css"]  {
    font-family: 'Quicksand', sans-serif;
}

/* Customizing the Streamlit Buttons */
div.stButton > button:first-child {
    background-color: #f4e04d;
    color: #3a5a40;
    font-family: 'Caveat', cursive;
    font-size: 24px;
    border: 3px solid #bc6c25;
    border-radius: 50px;
    padding: 10px 40px;
    box-shadow: 4px 4px 0px #3a5a40;
    transition: all 0.3s ease;
    display: block;
    margin: 0 auto;
}

div.stButton > button:first-child:hover {
    transform: scale(1.05);
    background-color: #588157;
    color: #fefae0;
}

/* The Story Card */
.story-card {
    background-color: rgba(254, 250, 224, 0.95);
    border: 5px solid #bc6c25;
    border-radius: 20px;
    padding: 40px;
    text-align: center;
    box-shadow: 10px 10px 0px #3a5a40;
    margin-top: 50px;
    animation: fadeIn 1s ease-in;
}

.slide-text {
    font-size: 24px;
    color: #3a5a40;
    line-height: 1.6;
    margin-bottom: 20px;
}

.poke-img {
    max-width: 200px;
    animation: float 3s ease-in-out infinite;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0px); }
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# 5. Logic: Intro Screen vs Main World
if not st.session_state.entered:
    # Blank White Screen with Enter Button
    st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Enter"):
            st.session_state.entered = True
            st.rerun()

else:
    # Main Magical World Triggered
    # Inject background image and audio
    background_css = """
    <style>
    .stApp {
        background: linear-gradient(135deg, rgba(88,129,87,0.8), rgba(244,224,77,0.6), rgba(188,108,37,0.7)), url('https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=2070&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)
    
    # Auto-play Audio Hack (Streamlit doesn't auto-play audio well natively, this HTML injection works better)
    audio_html = """
    <audio autoplay loop>
        <source src="jazz.mp3" type="audio/mpeg">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

    # Render Current Slide
    current_idx = st.session_state.slide_index
    
    if current_idx < len(slides):
        st.markdown('<div class="story-card">', unsafe_allow_html=True)
        
        if current_idx == 0:
            st.markdown("<h1 style='font-family: Caveat, cursive; color: #bc6c25; font-size: 50px;'>Let's Meet Ludvig</h1>", unsafe_allow_html=True)
            
        slide_data = slides[current_idx]
        st.markdown(f'<p class="slide-text">{slide_data["text"]}</p>', unsafe_allow_html=True)
        
        if slide_data["img"]:
            st.markdown(f'<img class="poke-img" src="{slide_data["img"]}" alt="pokemon">', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Next"):
                st.session_state.slide_index += 1
                st.rerun()
                
    else:
        # Final Birthday Slide
        st.markdown('<div class="story-card">', unsafe_allow_html=True)
        st.markdown("<h1 style='font-family: Caveat, cursive; color: #bc6c25; font-size: 60px;'>HAPPY 26TH BIRTHDAY, LUDVIG!</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 40px; color: #3a5a40;'>I love you.</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

