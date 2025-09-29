import dash
from dash import dcc, html, Input, Output
import numpy as np
import plotly.express as px

app = dash.Dash(__name__)

# Jeu de données initial
x = np.linspace(0, 10, 500)

app.layout = html.Div([
    html.H1("Interactive sine"),

    html.Label("Fréquence"),
    dcc.Slider(
        id="freq-slider",
        min=0.5, max=5, step=0.1, value=1.0,
        marks={i: f"{i}" for i in range(1, 6)}
    ),

    html.Label("Phase"),
    dcc.Slider(
        id="phase-slider",
        min=0, max=2*np.pi, step=0.1, value=0.0,
        marks={0: "0", int(np.pi): "π", int(2*np.pi): "2π"}
    ),

    dcc.Graph(id="graph")
])

@app.callback(
    Output("graph", "figure"),
    [Input("freq-slider", "value"),
     Input("phase-slider", "value")]
)
def update_graph(freq, phase):
    df = pd.DataFrame({"x": x, "y": np.sin(freq * x + phase)})
    fig = px.line(df, x="x", y="y", title=f"sin({freq:.1f}·x + {phase:.2f})")
    return fig

server = app.server  # nécessaire pour Render

if __name__ == "__main__":
    app.run(debug=True)
