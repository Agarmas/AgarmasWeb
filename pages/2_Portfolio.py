import streamlit as st

st.set_page_config(
    page_title="Portfolio",
    page_icon=":bar_chart:",
)

st.title("Portfolio")

st.write("""
### Projects :briefcase:
1. **Odoo Coffee Management (with contributors)**\n
    Developed a custom Odoo module to manage coffee consumption and track stock levels for a coffee management system. Worked with a team of contributors to design and implement the solution.  
    [View Repository](https://github.com/Agarmas/upocafe)
2. **Data Visualization in remote work productivity analysis**\n
    Use matplotlib & seaborn for data visualization and generate knowedge and data correlation.\n
    [Web page](https://agarmas-remote-work-analysis.streamlit.app/)\n
    [View repository](https://github.com/Agarmas/remote-work-analysis)
""")
