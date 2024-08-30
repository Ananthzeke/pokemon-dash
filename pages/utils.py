# utils/navbar.py
import dash_bootstrap_components as dbc
from dash import html, dcc

def navbar():
    return html.Nav([
        dcc.Link('Home', href='/', className='nav-link'),
        dcc.Link('Data Explorer', href='/explorer', className='nav-link'),
        dcc.Link('Comparison Tool', href='/comparison', className='nav-link'),
        dcc.Link('Team Builder', href='/team-builder', className='nav-link'),
    ], className='navbar')
