import streamlit as st
from state import get

st.title('Pages with state')

with st.echo():
	page = st.radio('Page select', options=['A', 'B'])

	state = get(a=0, b=0)

	a = state.a
	b = state.b
	sum = 0

	if page == 'A':
		a = st.number_input('Enter a: ', value=state.a)
		state.a = a
	elif page == 'B':
		b = st.number_input('Enter b: ',  value=state.b)
		state.b = b

	sum = a+b
	st.write('a: ', a)
	st.write('b: ', b)
	st.write('sum: ', sum)