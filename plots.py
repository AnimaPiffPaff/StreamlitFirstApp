import pandas as pd

data = pd.read_csv('student-mat.csv', sep=';')
pd.set_option('display.max_columns',None)
data.head()

import plotly.express as px

def draw_hist(data):
    fig = px.histogram(data, x='G3')
    return fig
    
def draw_heatmap(data):    
    fig = px.density_heatmap(data, x="age", y="G3", labels={'G3':'Final Grade'}, text_auto=True)
    fig.show()

def draw_scatter(data):
    fig = px.scatter(data, x="G1", y="G3", color="Medu", size='G3', trendline='ols')
    return fig

def draw_animscatter(data):
    fig = px.scatter(data, x="G1", y="G3", animation_frame="age",
               size="G3", color="Medu",
               log_x=True)
    return fig

def draw_funnel(data):
    fig = px.funnel(data, x='G3', y='Medu')
    return fig

import plotly.graph_objects as go

def draw_3dfig(data):
    fig = go.Figure(data=go.Surface(z=data, showscale=True))
    fig.update_layout(
        title='Grades',
        width=400, height=400,
        margin=dict(t=40, r=0, l=20, b=20)
    )
    return fig