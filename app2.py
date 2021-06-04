import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

st.title('This is my second Streamlit app')

st.header('Write can handle (almost) anything you throw at it')

def addOne(x: int) -> int:
	"""This function adds 1 to the input
	"""
	return x+1

st.write('### Passing a function to write displays its signature and docstring')
with st.echo():
	st.write(addOne)

st.write('### Passing html to write')
with st.echo():
	st.write("""
	<font color='red'>Some red text</font>
	""", unsafe_allow_html=True)

st.write('### Passing multiple things to write')
with st.echo():
	st.write('Some **_markdown_**,', 'Some $\LaTeX$', 'and some :sunglasses: emojis')

st.header('image() for images')
with st.echo():
	img = Image.open('/Users/apoorve/Downloads/test_to_align.jpeg')
	img = img.resize(size=(200, 200))
	st.image(img)

st.header('Passing a dataframe to write (with styling!)')
with st.echo():
	df = chart_data = pd.DataFrame(
		np.random.randn(20, 3),
		columns=['a', 'b', 'c']
	)
	st.write(df.style.highlight_max(axis=1))

st.header('Drawing a line chart from our dataframe')
with st.echo():
	st.line_chart(df)

st.header('Drawing an area chart from our dataframe')
with st.echo():
	st.area_chart(df)

st.header('Adding things to the sidebar')
with st.echo():
	st.sidebar.write('This thing goes to the sidebar')

st.header('Displaying points on a map')
with st.echo():
	df = pd.DataFrame(
		np.random.randn(1000, 2) / [50, 50] + [26.912434, 75.787270],
		columns=['lat', 'lon'])
	st.map(df)

st.header('Other input widgets')

st.subheader('Text input')
with st.echo():
	some_input = st.text_input('Enter text here')
	st.write('Writing the text back:', some_input)

st.subheader('Date input')
with st.echo():
	some_input = st.date_input('Enter date here')
	st.write('Writing the date back:', some_input)

st.subheader('Audio playback')
with st.echo():
	st.audio('/Users/apoorve/Downloads/hello.wav')

st.subheader('Video playback')
with st.echo():
	st.video('https://www.youtube.com/watch?v=SjHUb7NSrNk')

st.sidebar.header('Button')
with st.echo():
	btn = st.sidebar.button("Don't press me")
	if btn:
		st.balloons()

st.subheader('Checkbox')
with st.echo():
	cb = st.checkbox('Preticked checkbox', value=True)
	st.write('Checkbox is: ', cb)

st.subheader('Radio buttons')
with st.echo():
	option = st.radio('Some radios', options=['Option1', 'Option2', 'Option3'])
	st.write('Selected radio: ', option)

st.subheader('Selectbox')
with st.echo():
	option = st.selectbox('A selectbox', options=['Option1', 'Option2', 'Option3'])
	st.write('Selected option: ', option)

st.subheader('Multi-selectbox')
with st.echo():
	option = st.multiselect('A multi-selectbox', options=['Option1', 'Option2', 'Option3'])
	st.write('Selected options: ', option)

st.subheader('Slider')
with st.echo():
	option = st.slider('A slider', min_value=0, max_value=100, step=1, value=77)
	st.write('Selected value: ', option)

st.subheader('File uploader')
with st.echo():
	option = st.file_uploader('File', type=['jpeg', 'jpg', 'png'], accept_multiple_files=True)

st.header('Forms')
with st.echo():
	with st.form("my_form"):
		st.write("Inside the form")
		slider_val = st.slider("Form slider")
		checkbox_val = st.checkbox("Form checkbox")

		# Every form must have a submit button.
		submitted = st.form_submit_button("Submit")
		if submitted:
			st.write("slider", slider_val, "checkbox", checkbox_val)

st.header('Expander')
with st.echo():
	with st.beta_expander("This is an expander"):
		st.write('Expanded content!')

st.header('Columns')
with st.echo():
	col1, col2, col3 = st.beta_columns(3)
	with col1:
		st.header("A cat")
		st.image("https://static.streamlit.io/examples/cat.jpg")
	with col2:
		st.header("A dog")
		st.image("https://static.streamlit.io/examples/dog.jpg")
	with col3:
		st.header("An owl")
		st.image("https://static.streamlit.io/examples/owl.jpg")

import time
st.header('Spinners and different types of messages')
with st.echo():
	with st.spinner('Wait for 3 seconds...'):
		time.sleep(3)
		st.success('This is a success message!')
		st.info('This is a purely informational message')
		st.warning('This is a warning message')

st.header('Progress bar')
with st.echo():
	my_bar = st.progress(0)
	for percent_complete in range(100):
		time.sleep(0.1)
		my_bar.progress(percent_complete + 1)
