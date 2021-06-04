import streamlit as st

st.title('Pages')

with st.echo():
	page = st.radio('Page select', options=['A', 'B'])

	a = 0
	b = 0
	sum = 0

	if page == 'A':
		a = st.number_input('Enter a: ', value=a)
	elif page == 'B':
		b = st.number_input('Enter b: ', value=b)

	sum = a+b
	st.write('a: ', a)
	st.write('b: ', b)
	st.write('sum: ', sum)