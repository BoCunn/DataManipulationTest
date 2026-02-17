
<div align="center">

<h1>How To Set Up Locally</h1>

</div>


<h2>Dependancies: </h2>
<p>Python 3.11.14</p>
<p>Librosa >v.11</p>
<p>Matplotlib</p>
<b><p>Numpy < v2.3</p></b>
<p>Pandas >v2.3.3</p>
<p>Scipy >v1.13 </p>
<p>Install all necessary modules and clone the repo, hit run and be amazed by the produced graphs of extracted features!</p>
<br>
<h1 align="center"> Scripts and Descriptions</h1>

<h2>display.py</h2>
<p>Iterates through the provided dictionary of features and uses NumPy and MatPlot to either compile and display a graph or display the value in the case of the euclidean distance.</p>
<br>
<h2>export.py</h2>
<p>Iterates through the provided dictionary of features and uses Pandas to convert the features to dataFrames, then to csv files.</p>
<br>
<h2>feature_extraction.py</h2>
<p>Displays the wave form of the audio, then calls the appropriate librosa functions to extract the features and store the value in the features dictionary.</p>
<br>
<h2>load_audio.py</h2>
<p>Uses librosa to load the audio at the provided audio path and at the provided offset for the provided duration.</p>
<br>
<h2>main.py</h2>
<p>Calls the other scripts in the pipeline to create the overall intended functionallity of the program</p>
