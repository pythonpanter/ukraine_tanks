import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# create the dataframe
# copied in here because of emojis, status 15.03.23
data = {'Delivery Country': ['🇩🇰 🇩🇪 🇳🇱', '', '🇺🇸', ' ', '🇬🇧', '  ', '🇵🇱', '🇩🇪', '🇪🇸', '🇸🇪', '🇨🇦', '🇳🇴', '🇵🇹', '🇫🇮'],
        'Announced': [100, 0, 31, 0, 24, 0, 14, 18, 6, 10, 8, 8, 3, 3],
        'Potential': [ 78, 0,  0, 0,  4, 0,  0,  0, 4,  0, 0, 0, 0, 0],
        'Delivered': [  0, 0,  0, 0,  0, 0, 14,  0, 0,  0, 0, 0, 0, 0],
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

for status in ["Announced", "Potential", "Delivered"]:
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
    Last Update: 15.03.2023

    Comments:
   
    * 🇩🇰 🇩🇪 🇳🇱: Coalition announced 100 Leopard 1 until early 2024, up to 178 until end of 2024
    * 🇸🇪: announced a maximum of 10 Leopard 2, could be less
    
    No responsiblity is taken for the correctness and completeness of this information.\n
    Created by Kai Braeunig: [LinkedIn profile - login required](https://www.linkedin.com/in/ai-kai/)
    
""")


# Display optional table
#if st.checkbox("Show Data Table"):
#    st.write(data)
    
# Display optional sources
if st.checkbox("Show Sources"):
    st.markdown("""
* https://english.nv.ua/nation/ukraine-to-receive-no-more-than-50-leopards-tanks-promised-by-west-by-april-newspaper-claims-50305298.html
* https://www.technology.org/2023/03/11/ukraine-will-receive-twice-as-many-challenger-2-tanks-as-previously-planned/
* https://www.forbes.com/sites/davidaxe/2023/03/04/more-ex-british-challenger-2-tanks-are-bound-for-ukraine-as-london-doubles-its-pledge/?sh=3445596b232b
* https://news.yahoo.com/first-batch-leopard-1-tanks-182300105.html
* https://english.nv.ua/nation/germany-to-transfer-178-leopard-1a5-tanks-to-ukraine-news-50302756.html
* https://news.yahoo.com/poland-sends-10-more-leopard-161300461.html
* https://euromaidanpress.com/2023/03/09/poland-already-sent-14-leopard-2-tanks-to-ukraine-as-ukrainian-crews-finished-training-on-them-polish-defense-minister/
* https://english.nv.ua/nation/tank-coalition-has-full-battalion-of-leopard-2a4-tanks-ready-for-ukraine-news-50304558.html
* https://www.reuters.com/world/canada-imposes-new-russia-sanctions-pledges-battle-tanks-ukraine-2023-02-24/
* https://www.swissinfo.ch/eng/reuters/ukrainian-soldiers-wrap-up-leopard-2a4-tank-training-in-spain/48356738
* https://www.reuters.com/world/europe/ukrainian-soldiers-wrap-up-leopard-2a4-tank-training-spain-2023-03-13/
* https://www.berliner-zeitung.de/news/offiziell-deutschland-liefert-14-leopard-2-kampfpanzer-in-die-ukraine-li.310692
* https://www.armyrecognition.com/defense_news_march_2023_global_security_army_industry/germany_and_portugal_to_donate_together_to_ukraine_21_leopard_2a6_tanks.html
* https://www.reuters.com/world/europe/sweden-send-up-10-leopard-tanks-ukraine-2023-02-24/
* https://www.reuters.com/world/europe/finland-send-three-leopard-tanks-ukraine-2023-02-23/
* https://www.welt.de/politik/ausland/article243651059/Ueber-100-Leopard-1-Pistorius-verkuendet-in-Kiew-weitere-Militaerhilfe.html
""")