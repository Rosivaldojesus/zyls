from django.shortcuts import render
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
    by_days = []

    def get_context_data(self, **kwargs):
        context = super(Graph_a, self).get_context_data(**kwargs)

        fig = go.Figure()
        scatter = go.Scatter(x=[x['day']
   for x in by_days
                                ], y=[0, 10, 17, 8],
                             mode='lines', name='test',
                             opacity=0.8, marker_color='green'
        )

        fig.add_trace(scatter)
        div = plot(fig, output_type='div')

        context['graph'] = div

        return context








def Graph_b(request):

    # from plotly.offline import plot
    # import plotly.graph_objs as go
    #
    # fig = go.Figure()
    # scatter = go.Scatter(x=[0, 1, 2, 3], y=[0, 1, 2, 3],
    #                      mode='lines', name='test',
    #                      opacity=0.8, marker_color='green')
    # fig.add_trace(scatter)
    # plt_div = plot(fig, output_type='div')

    import plotly.express as px
    from pandas import DataFrame

    df1 = DataFrame(dict(time=[10, 20, 30], sales=[10, 8, 30]))
    df2 = DataFrame(dict(market=[4, 2, 5]))
    plt_div = px.bar(df1, x=df1.time, y=df2.market, color=df1.sales)


    context = {
        'plt_div': plt_div
    }

    return render(request, 'dashboard/graph_b.html', context)