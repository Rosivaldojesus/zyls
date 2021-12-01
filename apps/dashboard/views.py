
from django.views.generic import TemplateView
import plotly.graph_objs as go
from plotly.offline import plot
from .ploty import Plot1d



class Graph(TemplateView):
    template_name = 'dashboard/graph.html'

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)

        x = [-2,0,4,6,7]
        y = [q**2-q+3 for q in x]
        trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': 10},
                            mode="lines",  name='1st Trace')

        data=go.Data([trace1])
        layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context





class Graph_a(TemplateView):
    template_name = 'dashboard/graph_a.html'


    def get_context_data(self, **kwargs):
        context = super(Graph_a, self).get_context_data(**kwargs)

        fig = go.Figure()
        scatter = go.Scatter(x=["Segunda",'Terça', 'Quarta', 'Quinta'], y=[0, 10, 17, 8],
                             mode='lines', name='test',
                             opacity=0.8, marker_color='green'
        )

        fig.add_trace(scatter)
        div = plot(fig, output_type='div')

        context['graph'] = div

        return context