# Streamlit Demo

Presented as a ligtning talk on 4th June, 2021 at the Wadhwani Institute of Artificial Intelligence.  
[Presentation link](https://docs.google.com/presentation/d/1evaObTTzYkH_zva2SCWoapq6LuLb2WP6pgcJ68wMDqI/edit?usp=sharing)

### Steps to follow 
1. Install the requirements  
`pip install -r requirements.txt`
1. Run any of the following files with the command  
`streamlit run <filename.py>`
   - `app1.py` 
   - `app2.py` 
   - `cropper.py` 
   - `page.py` 
   - `page_state.py` 

### Streamlit custom components
Custom components are for additional widget functionality that is not covered by Streamlit widgets out-of-the-box
- Using custom components
    1. Go to [streamlit components gallery](https://streamlit.io/gallery?type=components&category=featured)
    2. Check if someone has built the component you want
    3. An example can be seen by running  
	`streamlit run cropper.py`
- Building custom components  
	_Explanation coming soon_
    - [Official Link](https://docs.streamlit.io/en/stable/streamlit_components.html)


### Maintaining state across reruns
1. (Without state) `streamlit run page.py`
2. (WITH state) `streamlit run page_state.py`
3. Copy the state.py file to your directory.
4. Use `from state import get` in the file that you maintain state in.
5. Use `ret_state = get(a=0, b=0)` where the get function will take in all variables (`a`, `b`) that you want to maintain state for, with their initial values (`a=0`, `b=0`).
6. Values can be read from the state using `state.a`
7. New values can be updated to the state by using `state.a = 5`
8. In summary, replace `a` in the code without state by `state.a` and move the initialisation to the `get` function.
9. Please compare `page.py` (without state) and `page_state.py` (with state) for an example use of state.

### Distributing/Deplying a Streamlit app  
- (RECOMMENDED) Streamlit Sharing
    1. Log on to [streamlit sharing](https://streamlit.io/sharing) page through your Github account
    2. Pick the repo, branch and file that you want to deploy
    3. Submit and it will give a shareable URL of your app! 
    4. Any commits made to the branch chosen in step 2 will trigger a re-deploy of the new version of the app!
   
- Using AWS EC2 like services  
    1. ssh into the instance
    2. clone and run your app through `streamlit run <filename.py>`
    3. The `Network URL` that is displayed is the shareable URL of your app!
    4. The network settings of your security-group have to be changed to allow traffic to the streamlit port and all IP addresses.
    5. The public IP of an AWS instances changes everytime we restart it. To have the same IP, it can be assigned a static IP through Elastic IPs (free).

- Using Github Gists
    1. This method is only for distributing your app. It will not deploy it anywhere. Users can run the app easily on their own instances!
    2. Distribute the URL of your Github Gist's raw version. You can find the raw version by going to the normal gist url and clicking raw on the file that you want to share. 
       - (Incorrect) [Github gist url](https://gist.github.com/apugoneappu/42707b59c5a50f0f7a3fff0176f80431)
       - (Correct) [Github gist raw url](https://gist.githubusercontent.com/apugoneappu/42707b59c5a50f0f7a3fff0176f80431/raw/b0395e7f85f8631d126e79a7ace88f477ae68b6c/streamlit_demo.py)
    3. Users can run the app on their machine through  
	`streamlit run <replace_gist_raw_url>` 

### References   
1. [Custom components gallery](https://streamlit.io/gallery?type=components&category=featured)  
Before building a component, check this link if someone has already built it
2. [Building custom components](https://docs.streamlit.io/en/stable/streamlit_components.html)
3. [Gist that contains the code for maintaining state](https://gist.github.com/tvst/036da038ab3e999a64497f42de966a92)
4. [Shareable gist for app2.py](https://gist.githubusercontent.com/apugoneappu/42707b59c5a50f0f7a3fff0176f80431/raw/b0395e7f85f8631d126e79a7ace88f477ae68b6c/streamlit_demo.py)
5. [Talk slides](https://docs.google.com/presentation/d/1evaObTTzYkH_zva2SCWoapq6LuLb2WP6pgcJ68wMDqI/edit)
