from dash import html
from pages.utils import navbar

def layout():
    return html.Div([
        # Navbar
        navbar(),

        # Home Page Content
        html.Div([
            html.H1("Welcome to the Pokémon Dashboard"),
            html.P("Explore detailed Pokémon data, compare stats, and build your ultimate team."),
            html.Img(src="assets/pokemon_logo.jpeg", alt="Pokémon Logo", className="logo"),
        ], className='home-content')
    ])
