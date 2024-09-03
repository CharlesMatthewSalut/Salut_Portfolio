import streamlit as st

st.sidebar.image("1.jpg", width=200)
st.sidebar.title("Charles Matthew M. Salut")
section = st.sidebar.radio("Go to", ["Profile", "Hobbies", "Socials"])

st.title("My Autobiography")

if section == "Profile":
    st.header("🌱About me:")
    st.write("""
            Age: 19 years old
            \nAddress: Kingswood Lipata Minglanilla Cebu
            \nBirthdate: 25th of April 2002
            \nBirthplace: Cebu Chong Hua Hospital

            Traits
            • Hard to get along with
            • Impatient
            • Lazy
            • Resourceful
             
            Favorites
            • Food: Red Velvet Cake🍰
            • Thing: Computer🖥️
            • Place: Japan🎌
            
            Rule #32
            ENJOY THE LITTLE THINGS
            -Zombieland
             """)
    
elif section == "Hobbies":
    st.header("🎯Hobbies")
    col1, col2 = st.columns(2)
    with col1:
        st.write("🚀Hobby 1")
        st.write("Sports")
        st.image("download.png", width=150)
        st.image("download (1).png", width=150)
        st.image("2.jpg", width=150)
    with col2:
        st.write("🚀Hobby 2")
        st.write("Videogames")
        st.image("download (2).png", width=150)
        st.image("download (3).png", width=150)
        st.image("download (4).png", width=150)


elif section == "Socials":
    st.header("🌐Socials")
    st.write("Connect with me on social media:")
    st.markdown("ⓕ[Facebook](https://www.facebook.com/charles.salut/)")
    st.markdown("📧[Email](charlesmatthew.salut@cit.edu)")
    st.markdown("</>[GitHub](https://github.com/CharlesMatthewSalut)")
