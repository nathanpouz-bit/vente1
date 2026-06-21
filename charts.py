import plotly.express as px

def bar(df, x, y, title):
    return px.bar(df, x=x, y=y, title=title)


def line(df, x, y, title):
    return px.line(df, x=x, y=y, title=title)


def pie(df, names, values, title):
    return px.pie(df, names=names, values=values, title=title)
