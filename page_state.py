import streamlit as st
from state import get

st.title('Pages with state')

with st.echo():
	page = st.radio('Page select', options=['A', 'B'])

	ret_state = get(a=0, b=0)
	sum = 0

	if page == 'A':
		ret_state.a = st.number_input('Enter a: ', value=ret_state.a)
	elif page == 'B':
		ret_state.b = st.number_input('Enter b: ',  value=ret_state.b)

	sum = ret_state.a + ret_state.b
	st.write('a: ', ret_state.a)
	st.write('b: ', ret_state.b)
	st.write('sum: ', sum)