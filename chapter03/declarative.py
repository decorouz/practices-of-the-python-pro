import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    marker={'color': 'red', 'symbol': 104},
    mode='markers+lines',
    text=['one', 'two', 'three'],
    name='1st Trace',
)
