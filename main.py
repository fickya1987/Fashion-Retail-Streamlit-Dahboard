import streamlit as st 
from streamlit_option_menu import option_menu

import fashion , customers , items , Sales


st.set_page_config(
    page_title= "Fashion Retail Sales"

)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })


    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Fashion Retail ',
                options=['Data','Sales ','Customers ','Items '],
                icons=['database-fill','cash-coin','people-fill','bag-fill'],
                menu_icon='bi-cart3',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )     


        if app == "Data":
            fashion.app()
        if app == "Sales ":
            Sales.app()    
        if app == "Customers ":
            customers.app()        
        if app == 'Items ':
            items.app()



    run()            
        