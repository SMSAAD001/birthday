import streamlit as st
import time
import base64
import os

# Set Page Config
st.set_page_config(page_title="Happy Birthday Naba!", page_icon="🎉")

def main():
    st.title("💖 Happy Birthday, Naba! 🎂🎈")

    # Heartbeat Animation (SVG)
    myocardium_svg = '''
    <svg viewBox="0 0 200 100" width="200" height="100">
        <polyline points="0,50 20,50 30,20 40,80 50,30 60,70 70,50 100,50 120,50 130,20 140,80 150,30 160,70 170,50 200,50" 
                  stroke="red" stroke-width="3" fill="none" stroke-linejoin="round">
            <animate attributeName="stroke-width" values="3;6;3" dur="0.5s" repeatCount="indefinite"/>
            <animate attributeName="stroke" values="red;darkred;red" dur="0.5s" repeatCount="indefinite"/>
        </polyline>
    </svg>
    '''
    st.markdown(f"""<div style='text-align:center;'> {myocardium_svg} </div>""", unsafe_allow_html=True)

    # Secure Access
    password = st.text_input("Enter Security Key to Unlock Surprise", type="password")

    if password == "safa":
        if st.button("Open Surprise 🎁"):
            time.sleep(1)

            # Display Image Grid with Animation
            image_url = "https://res.cloudinary.com/di2nwhfma/image/upload/v1742115481/ag316aascsygct4dpelp.jpg"
            grid_html = f"""
            <div style="display: flex; justify-content: center;">
                <img src="{image_url}" width="300" style="border-radius: 15px; box-shadow: 0px 0px 20px 5px pink; animation: glow 1.5s infinite alternate;">
            </div>
            <style>
                @keyframes glow {{
                    from {{ box-shadow: 0px 0px 10px 2px pink; }}
                    to {{ box-shadow: 0px 0px 25px 10px red; }}
                }}
            </style>
            """
            st.markdown(grid_html, unsafe_allow_html=True)

            # Play "Tu Hi Haqeeqat" Ringtone (Hidden)
            audio_file = "tu_hi_haqeeqat.mp3"  # Make sure this file is in your project directory
            if os.path.exists(audio_file):
                with open(audio_file, "rb") as file:
                    audio_bytes = file.read()
                    audio_base64 = base64.b64encode(audio_bytes).decode()

                st.markdown(f"""
                <audio autoplay style="display: none;">
                    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                </audio>
                """, unsafe_allow_html=True)
            else:
                st.error("Audio file not found! Please upload it or check the file path.")

            # Birthday Message
            st.markdown(
                """
                ## ❤️ A Special Letter to You ❤️
                
                My Dearest Naba, Laddu lu, Shonu lu, Janu lu

                On this wonderful day, I just want to remind you how incredibly special you are to me. Every moment with you is a blessing, and I cherish every laugh, every memory, and every dream we share.

                You are the light of my life, my happiness, and my greatest love. With you, every day feels brighter, every challenge seems easier, and every joy feels infinite. Your kindness, your warmth, and your love fill my heart in ways words can never fully express.

                Laddu lu, Shonu lu, Janu lu, you are my sweetest happiness, my heart’s favorite melody, and the most precious part of my life. I am endlessly grateful to have you by my side, and I promise to cherish you, support you, and love you more with every passing day.

                May this day bring you all the joy and happiness you deserve, and may our love continue to grow deeper with each heartbeat.

                With all my love, forever and always,  
                **Saad ❤️**
                """
            )

            st.balloons()
    else:
        st.warning("Enter the correct security key to unlock the surprise!")

if __name__ == "__main__":
    main()
