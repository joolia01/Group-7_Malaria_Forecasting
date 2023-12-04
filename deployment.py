import streamlit as st

def main():
    # Sidebar with user input as dropdown
    st.sidebar.header("User Input")
    options = ['Burkina Faso', 'Benin', 'Cabo Verde', "Cote d'Ivoire", 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Liberia', 'Mali', 'Mauritania', 'Niger', 'Nigeria', 'Senegal', 'Sierra Leone','Togo']
    user_input = st.sidebar.selectbox("Select an option:", options)

    # Main content
    st.title("Malaria Forecasting Application")

    # Condition based on user input
    if user_input == "Burkina Faso":
        st.image("Burkina Faso(2).png", caption="Burkina Faso", use_column_width=True)
    elif user_input == "Benin":
        st.image("Benin.png", caption="Benin", use_column_width=True)
    elif user_input == "Cabo Verde":
        st.image("Cabo Verde.png", caption="Cabo Verde", use_column_width=True)
    elif user_input == "Cote d'Ivoire":
        st.image("Cote dIvoire.png", caption="Cote d'Ivoire", use_column_width=True)
    elif user_input == "Gambia":
        st.image("Gambia.png", caption="Gambia", use_column_width=True)
    elif user_input == "Ghana":
        st.image("ghana.png", caption="Ghana", use_column_width=True)
    else:
        st.write("No image selected")

if __name__ == "__main__":
    main()
