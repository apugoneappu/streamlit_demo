import streamlit as st

with st.echo():
	st.write(r'''
		# This is my first Streamlit app
		## Build with just a single line of code, it can use **_Markdown_** and $\LaTeX$ and emojis :sunglasses:!
	''')

@st.cache
def foo(a):
	return a +1