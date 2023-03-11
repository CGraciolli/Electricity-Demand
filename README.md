<h2>Electricity Demand</h2>
<h4>Objectives:</h4>
<ul>
<li>Get the data of the real electricity demand from the Spanish electricity grid during the period 02/09/2018-06/10/2018, 
using their <a href="https://api.esios.ree.es/" target="_blank">API.</a></li>
<li>Decompose the electricity demand using Fast Fourier Transform.</li>
<li>Deploy an API to allow remote access to this data.</li>
</ul>
<h4>The Data:</h4>
<img src="https://user-images.githubusercontent.com/112963325/224485993-f26c4844-798a-4f19-ba08-782447d98e4e.png" alt=demand>
As we can see in the graph above, the function is approximately periodical. This make it a good candidate to be modeled using a Fourier Transform. <br><br>
<img src="https://user-images.githubusercontent.com/112963325/224485997-22352f5c-836b-416d-89e3-637ed0e8bd0e.png" alt=welch">
As expected, we have peaks where the frequenies represent one day (0.04) as well as one week (0.006). We also have a peak for the 12 hours period (0.083), probably representing meal times.
<br>
<h4>The APIs:</h4>
I decided to make two APIs, one returning the fast fourier transform, the other the power spectral density. Both return the values from 02/09/2018 to 06/10/2018 in their home page, but also have option of changing dates. 


