from dash import Dash
from index import layout, register_callbacks

app = Dash(__name__, suppress_callback_exceptions=True)
app.layout = layout

# Register callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
