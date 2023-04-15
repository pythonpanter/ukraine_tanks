import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# create the dataframe
# copied in here because of emojis, status 15.03.23
data = {'Delivery Country': ['🇩🇰 🇩🇪 🇳🇱', '', '🇺🇸', ' ', '🇬🇧', '  ', '🇩🇪', '🇵🇱', '🇪🇸', '🇸🇪', '🇨🇦', '🇳🇴', '🇵🇹'],
        'Delivered': [  0, 0,  0, 0, 14, 0, 18, 14, 0,  0, 8, 8, 3],
        'Announced': [100, 0, 31, 0, 10, 0,  0,  0, 6, 10, 0, 0, 0],
        'Potential': [ 78, 0,  0, 0,  2, 0,  0,  0, 4,  0, 0, 0, 0],
}

df = pd.DataFrame(data)

# sort the dataframe by the 'Total' column
#df = df.sort_values(by='Total', ascending=False)

# Load data from CSV, separator is ";"
# data = pd.read_csv("data.csv", sep=";")
data = df

# Set layout colors
colors = {
    "Announced": "#1f77b4",  # dark blue
    "Potential": "#ff7f0e",  # orange
    "Delivered": "#2ca02c",  # dark green
}

# Create bar chart
fig = go.Figure()

for status in ["Delivered", "Announced", "Potential"]:
    fig.add_trace(
        go.Bar(
            x=data["Delivery Country"],
            y=data[status],
            name=status.title(),
            marker_color=colors[status],
        )
    )

fig.update_layout(
    title="Delivery of M1 Abrams, Challenger 2, Leopard 1, Leopard 2 battle tanks to Ukraine",
    #title_x=0.5,
    xaxis_title="Delivery Country",
    yaxis_title="Number of Tanks",
    legend_title="Status",
    barmode="stack",
    #width=1200,  # set width to 1000 pixels
)

fig.update_xaxes(range=[-1,14])

fig.update_yaxes(range=[0,220])

plus = 15

fig.add_annotation(
    x=0,  # x-coordinate of the center of the '🇩🇰 🇩🇪 🇳🇱' bar group
    y=178 + plus - 3,  # y-coordinate at the top of the bar group
    text="Leopard 1",
    showarrow=False,
    font=dict(size=12),
    xanchor='center',  # center the annotation horizontally
    #bgcolor='black',
    #textangle=-15,
    #bordercolor='white',
    xref="x",
    yref="y",
)

fig.add_annotation(
    x=2,  # x-coordinate of the center of the '🇺🇸' bar group
    y=28 + plus,  # y-coordinate at the top of the bar group
    text="M1 Abrams",
    showarrow=False,
    font=dict(size=12),
    xanchor='center',  # center the annotation horizontally
    #bgcolor='black',
    #textangle=-15,
    #bordercolor='white',
)

fig.add_annotation(
    x=4,  # x-coordinate of the center of the '🇬🇧' bar group
    y=28 + plus,  # y-coordinate at the top of the bar group
    text="Challenger 2",
    showarrow=False,
    font=dict(size=12),
    xanchor='center',  # center the annotation horizontally
    #bgcolor='black',
    #textangle=-15,
    #bordercolor='white',
)

fig.add_annotation(
    x=19/2,  # x-coordinates of the '🇩🇪', '🇵🇱', '🇨🇦', '🇳🇴', '🇪🇸', '🇵🇹', '🇸🇪', '🇫🇮' bar groups
    y=28 + plus,  # y-coordinates at the top of the bar groups
    text="Leopard 2",
    showarrow=False,
    font=dict(size=12),
    xanchor='center',  # center the annotation horizontally
    #bgcolor='black',
)

fig.add_shape(
    type="rect", # shape type
    x0=5.6, # lower bound of box along x-axis
    x1=13.4, # upper bound of box along x-axis
    y0=32, # lower bound of box along y-axis
    y1=34, # upper bound of box along y-axis
    fillcolor="white", # box color
    line_width=0, # border width (set to 0 to remove border)
)

st.title("Status of Game Changer Tanks for Ukraine")

# Display chart and comments
st.plotly_chart(fig)

st.markdown("""
    Last Update: 28.03.2023

    Comments:
   
    * 🇩🇰 🇩🇪 🇳🇱: Coalition announced 100 Leopard 1 until early 2024, up to 178 until end of 2024
    * 🇸🇪: announced a maximum of 10 Leopard 2, could be less
    
    No responsiblity is taken for the correctness and completeness of this information.\n
    [Sources and data table](https://docs.google.com/spreadsheets/d/1I6_B_REuG6m8kQFKfVm5LWnrcdOxiB7Imi8FfGGzuZw/edit?usp=sharing)\n
    Created by Kai Braeunig: [LinkedIn profile - login required](https://www.linkedin.com/in/ai-kai/)
    
""")