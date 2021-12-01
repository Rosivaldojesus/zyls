from plotly.offline import plot
import plotly.graph_objs as go



#Gráfico 01
def Plot1d():
    fig = go.Figure()
    scatter = go.Scatter(x=["Segunda", 'Terça', 'Quarta', 'Quinta'], y=[0, 10, 17, 8],
                         mode='lines', name='test',
                         opacity=0.8, marker_color='green')
    fig.add_trace(scatter)
    div = plot(fig, output_type='div')

    return div