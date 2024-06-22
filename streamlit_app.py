# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Example Streamlit App :cloud:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)

name_on_order = st.text_input('Mame on Smoothie:')
st.write('The name on your smoothie will be:', name_on_order)


session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select((col("FRUIT_NAME")))
st.dataframe(data=my_dataframe, use_container_width=True)


ingredients_list = st.multiselect(
    'Chose up to 5 ingredients:', my_dataframe, max_selections = 5)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += ' ' + fruit_chosen
        
    st.write(ingredients_string)

    
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
       values ('""" + ingredients_string + """', '"""+ name_on_order + """"')"""
    #st.write(my_insert_stmt)

    time_to_insert = st.button('Submit order')
