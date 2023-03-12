<h2>Electricity Demand</h2>
<h4>Objectives:</h4>
<ul>
<li>Get the data of the real electricity demand from the Spanish electricity grid during the period from 02/09/2018 to 06/10/2018, 
using their <a href="https://api.esios.ree.es/" target="_blank">API.</a></li>
<li>Decompose the electricity demand using Fast Fourier Transform.</li>
<li>Deploy an API to allow remote access to this data.</li>
</ul>
<h4>The Data:</h4>
<img src="https://user-images.githubusercontent.com/112963325/224485993-f26c4844-798a-4f19-ba08-782447d98e4e.png" alt=demand>
As we can see in the graph above, the function is approximately periodical. This make it a good candidate to be modeled using a Fourier Transform. <br><br>
<img src="https://user-images.githubusercontent.com/112963325/224536279-728971ff-f697-4dfc-8e6b-a0911c614b39.png" alt=welch">

As expected, the spectral density estimated has peaks near the frequencies that represent one week (1/(24*7) ≈ 0.006), one day (1/24 ≈ 0.04), and twelve hours (0.08). 
<br>
<h4>The APIs:</h4>
I decided to make two APIs, one returning the fast fourier transform, the other the Welch estimated power spectral density. Both return the values from 02/09/2018 to 06/10/2018 in their home page, but also have option of changing dates.
The reason for including the second API is that, if the objective of computing the FFT for the signal is to detect seasonal patterns, they can be found by looking at the spectral density for peaks. The Welch estimated is just a smoothed periodogram, making it easier to detect patterns.


