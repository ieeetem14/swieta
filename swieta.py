import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, Ellipse

def draw_santa(body_color, hat_color, show_gifts):
    """
    Rysuje Mikołaja i prezenty na podstawie wybranych kolorów i widoczności.
    """
    # Tworzenie figury Matplotlib
    fig, ax = plt.subplots(figsize=(6, 8))
    ax.set_aspect("equal")
    ax.axis("off")

    # KORPUS MIKOŁAJA
    # --------------------
    # Tułów
    body = Rectangle((-1.2, -1.0), 2.4, 2.2, color=body_color)
    ax.add_patch(body)
    # Kołnierz (biały pasek przy szyi)
    collar = Rectangle((-1.2, 1.0), 2.4, 0.2, color="white")
    ax.add_patch(collar)
    # Pasek
    belt = Rectangle((-1.2, 0.0), 2.4, 0.2, color="black")
    ax.add_patch(belt)

    # Klamra paska
    buckle = Rectangle((-0.3, 0.02), 0.6, 0.16, edgecolor="yellow", facecolor="none", linewidth=2)
    ax.add_patch(buckle)

    # Guziki
    for y in [0.7, 0.4, 0.1]:
        button = Circle((0, y), 0.05, color="black")
        ax.add_patch(button)

    # NOGI I BUTY
    # --------------------
    # Nogi (używają koloru korpusu)
    left_leg = Rectangle((-0.7, -1.5), 0.6, 0.5, color=body_color)
    right_leg = Rectangle((0.1, -1.5), 0.6, 0.5, color=body_color)
    ax.add_patch(left_leg)
    ax.add_patch(right_leg)

    # Buty
    left_boot = Rectangle((-0.8, -1.8), 0.8, 0.3, color="black")
    right_boot = Rectangle((0.0, -1.8), 0.8, 0.3, color="black")
    ax.add_patch(left_boot)
    ax.add_patch(right_boot)

    # --------------------
    # RĘCE
    # --------------------
    # Ręce (używają koloru korpusu)
    left_arm = Rectangle((-1.8, 0.5), 0.6, 1.0, angle=10, color=body_color)
    right_arm = Rectangle((1.2, 0.5), 0.6, 1.0, angle=-10, color=body_color)
    ax.add_patch(left_arm)
    ax.add_patch(right_arm)

    # Rękawiczki
    left_glove = Circle((-1.8, 0.5), 0.25, color="brown")
    right_glove = Circle((1.8, 0.5), 0.25, color="brown")
    ax.add_patch(left_glove)
    ax.add_patch(right_glove)

    # --------------------
    # GŁOWA
    # --------------------
    # Głowa
    head = Circle((0, 1.6), 0.6, color="#ffddb3")  # jasny kolor skóry
    ax.add_patch(head)

    # Broda
    beard = Ellipse((0, 1.3), 1.0, 0.9, color="white")
    ax.add_patch(beard)

    # Wąsy
    moustache_left = Ellipse((-0.15, 1.45), 0.5, 0.2, angle=15, color="white")
    moustache_right = Ellipse((0.15, 1.45), 0.5, 0.2, angle=-15, color="white")
    ax.add_patch(moustache_left)
    ax.add_patch(moustache_right)

    # Nos
    nose = Circle((0, 1.5), 0.08, color="#e0a070")
    ax.add_patch(nose)

    # Oczy
    left_eye = Circle((-0.2, 1.7), 0.06, color="white")
    right_eye = Circle((0.2, 1.7), 0.06, color="white")
    left_pupil = Circle((-0.2, 1.7), 0.03, color="black")
    right_pupil = Circle((0.2, 1.7), 0.03, color="black")
    ax.add_patch(left_eye)
    ax.add_patch(right_eye)
    ax.add_patch(left_pupil)
    ax.add_patch(right_pupil)

    # Uśmiech (prosta linia)
    ax.plot([-0.2, 0, 0.2], [1.32, 1.28, 1.32], color="black", linewidth=2)

    # CZAPKA
    # --------------------
    # Czerwona część czapki
    hat = Polygon([(-0.8, 1.9), (0.8, 1.9), (0, 2.6)], closed=True, color=hat_color)
    ax.add_patch(hat)

    # Biały pasek czapki
    hat_band = Rectangle((-0.8, 1.8), 1.6, 0.15, color="white")
    ax.add_patch(hat_band)

    # Pompom
    pompom = Circle((0, 2.65), 0.15, color="white")
    ax.add_patch(pompom)

    # --------------------
    # TŁO / PREZENTY (opcjonalne)
    # --------------------
    if show_gifts:
        # Prezent 1 (zielony)
        gift_box_1 = Rectangle((1.6, -0.6), 0.6, 0.6, color="green")
        gift_ribbon_1_vertical = Rectangle((1.86, -0.6), 0.08, 0.6, color="yellow")
        gift_ribbon_1_horizontal = Rectangle((1.6, -0.32), 0.6, 0.08, color="yellow")
        ax.add_patch(gift_box_1)
        ax.add_patch(gift_ribbon_1_vertical)
        ax.add_patch(gift_ribbon_1_horizontal)

        # Prezent 2 (niebieski)
        gift_box_2 = Rectangle((-2.2, -0.8), 0.5, 0.5, color="blue")
        gift_ribbon_2_vertical = Rectangle((-1.99, -0.8), 0.08, 0.5, color="silver")
        gift_ribbon_2_horizontal = Rectangle((-2.2, -0.59), 0.5, 0.08, color="silver")
        ax.add_patch(gift_box_2)
        ax.add_patch(gift_ribbon_2_vertical)
        ax.add_patch(gift_ribbon_2_horizontal)

        # Prosty prezent 3 (czerwony)
        gift_box_3 = Rectangle((-1.0, -1.8), 0.7, 0.4, color="red")
        gift_ribbon_3_vertical = Rectangle((-0.69, -1.8), 0.08, 0.4, color="gold")
        gift_ribbon_3_horizontal = Rectangle((-1.0, -1.64), 0.7, 0.08, color="gold")
        ax.add_patch(gift_box_3)
        ax.add_patch(gift_ribbon_3_vertical)
        ax.add_patch(gift_ribbon_3_horizontal)

    # Zakres osi, żeby wszystko było widać
    ax.set_xlim(-2.2, 2.4)
    ax.set_ylim(-2.0, 3.0)

    return fig

# ==============================================================================
# STRUKTURA APLIKACJI STREAMLIT
# ==============================================================================

st.set_page_config(layout="centered")
st.title("🎅 Kreator Mikołaja (Matplotlib w Streamlit)")

st.sidebar.header("Opcje personalizacji")

# Wybór koloru ubrania (tułów, ręce, nogi)
body_color_choice = st.sidebar.color_picker(
    "Kolor Ubrania Mikołaja", 
    "#FF0000" # Domyślnie czerwony
)

# Wybór koloru czapki
hat_color_choice = st.sidebar.color_picker(
    "Kolor Czapki Mikołaja", 
    "#FF0000" # Domyślnie czerwony
)

# Opcja włączenia/wyłączenia prezentów
show_gifts_toggle = st.sidebar.checkbox(
    "Pokaż Prezenty", 
    value=True # Domyślnie włączone
)

# Generowanie i wyświetlanie rysunku
santa_figure = draw_santa(body_color_choice, hat_color_choice, show_gifts_toggle)
st.pyplot(santa_figure)

st.sidebar.markdown(
    """
    ---
    **Instrukcja uruchomienia:**
    1. Zapisz kod jako `app.py`.
    2. Uruchom w terminalu: `streamlit run app.py`
    """
)
