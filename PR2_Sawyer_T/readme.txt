// ----------------------------------------------------
// UVM CS 195 / Math 195 ------------------------------
// FINAL PROJECT DOCUMENTATION - README.txt -----------
// Author(s): Tyler J. Sawyer - Last Updated: 5/4/14 --
// Contact : tsawyer1@uvm.edu -------------------------
// ----------------------------------------------------

1) Viewing the Report
	
	To view the report, you will need to open or render the file labeled
	'report_Sawyer_T.ipynb' in either:
		1) an iPython Renderer (Try: http://nbviewer.ipython.org/)
		2) A web browser capable of rendering XML pages.
		3) An XHTML or Python editor

	The report contains all the necessary information for learning about
	my final project, including:
		1) Project Questions / Goals
		2) Project Abstract
		3) Project Datasets & Analysis
		4) Conclusions / Answers to Questions

2) Viewing the Presentation Slides
	
	To view the presentation slides, you will need to open or render the file
	labeled 'slides_Sawyer_T.ipynb' in either:
		1) an iPython Renderer (Try: http://nbviewer.ipython.org/)
		2) A web browser capable of rendering XML pages.
		3) An XHTML or Python editor 

3) Project Contents

	./data/~				: This folder contains RAW data and dataset files.

	./data/shape_files/~			: This folder (And all files contained within) are shape data for
						  the continental US, and are used to render some of the animations 
						  and heat maps shown in my report file.

	./data/avg-annual-wage_State.csv	: This file contains the average annual wages for a select number
						  of historical years in a CSV format, used in my report file.
	./data/avg-annual-wage_State.xls	: This is the original XLS spreadsheet for the above CSV file,
						  unmodified from the US Census Bureau website.
	./data/gas_price_avg_state.csv		: This file contains average gas prices by state for a select
						  number of historical years in a CSV format, used in my report file.
	./data/gas_price_avg_state.xls		: This is the original XLS spreadsheet for the above CSV file,
						  unmodified from the US Census Bureau website.
	./data/health-insurance-by-State.xls	: An unused Health Insurance spreadsheet from the US Census Bureau website.
						  I did not have time to investigate this dataset, though I included
						  it for the sake of revisiting it in the future.
	./data/HMOs-by-State.xls		: An unused HMO-by-State spreadsheet from the US Census Bureau website.
						  I did not have time to investigate this dataset, though I included
						  it for the sake of revisiting it in the future.
	./data/purchasing_power_dollar.csv	: This data set demonstrates the purchasing power of a dollar, and was
						  not used in the scope of this project, but could be used later on
						  for fixing scales on my animations for inflation of the US currency.
	./data/purchasing_power_dollar.xls	: This is the original XLS spreadsheet for the above CSV file,
						  unmodified from the US Census Bureau website.
	./data/Single-Family_Housing_Price.csv	: This is the csv file containing housing prices and average cost
						  of living for each state, and used extensively in my report.
	./data/Single-Family_Housing_Price.xls	: This is the original XLS spreadsheet for the above CSV file,
						  unmodifed from the US Census Bureau website.
	./data/State-Population.csv		: This is a CSV file containing population data for each state for a select
						  number of historical years in the US. This was used in several
						  plots in my report.
	./data/State-Population.xls		: This is the original XLS spreadsheet for the above CSV file,
						  unmodifed from the US Census Bureau website.
	./data/unemployment_by_state.csv	: This is a CSV file containing the unemployment by state sheet 
						  from the origianl US Census Bureau spreadsheet for the 
						  unemployment and insured by state file (see below).
	./data/unemployed_insured_by-State.xls	: : This is the original XLS spreadsheet for the above CSV file,
						  unmodifed from the US Census Bureau website.

	./JSAnimation/~				: JSAnimation, and the contents within this folder, were used 
						  to render some of the animations seen in my project file(s).
						  JSAnimation is free to use under the BSD license.
						  see the below licenses section for more information.
						  (I hope this is the right place to put this library)

	./stats/~				: This folder contains either snippets of code (for testing), or 
				    		  extraneous log files that are generated as a result of code processes.
	./stats/buildHistogram_Simple.py	: This script was to test building a histogram for some of my 
						  data, carried over from my midterm project. It was unused in
						  this project.
	./stats/geo_USHeatMapTest.py		: This file was used to initially test the generation of heatmaps
						  seen throughout my final report.
	./stats/geo_USMapLabeled.py		: This file was a basic US Map with labels located on specific 
						  coordinates that corresponded to the locations of the capital
						  cities in each state. These locations were used for my animations,
						  but the labels were ultimately left out.
	./stats/geo_VTMap.py			: This file generated a map centered on the state of Vermont.
						  I used this script to figure out how to plot circles of varying 
						  radii on my animation plots.
	./stats/grabStateData.py		: This file was used to test python's ability to interpret CSV 
						  and XLS files and to import that data into a dictionary object.
	./stats/grabUnemploymentDatas.py	: Another file used to test python's ability to interpret a different
						  XLS format to see how well it would integrate into my project.
	./stats/histogram_State.py		: This was used in my midterm to generate a histogram of states,
						  but I ended up not using this for my final project.
	./stats/LatLong.py			: This script would grab the latitude and longitude of a location
						  based on its name. I may have used this, but luckily the geo_VTMap.py
						  script already had a list of Lat/Longs for me.
	./stats/README.md			: A readme file that is read by GITHUB. See the Github section of 
						  this readme for more information.
	./stats/sample_animateUSMap.py		: The original script to test and see if I could animate 
						  geographical maps with the JSAnimation library.
	./stats/sanitizeData.py			: An unused script that contained functions to clean and sanitize
						  incoming data from CSV, XLS, or online file sources.

	./readme.txt 				: This file : General information about all files. 

	./notes.txt 				: This file contains a running list of ideas, trials, and results 
						  of any code or code processing that occurs during my research. Each 							  entry is separated by a horizonal line, and each entry is timestamped 						  with each modification being timestamped as well. This will provide you
 						  (the reader) with a general idea of how long each task took me to 
						  process and what results I yielded from each of my experiments.

	./report_Sawyer_T.ipynb			: This is the main Report file. See Part (1) of this Readme 
						  for more details.

	./slides_Sawyer_T.ipynb			: This is my presentation file for the final project and the final
						  for the course at UVM. See Part (2) of this Readme for more details.

4) Dataset Sources & Licenses

	(1) - US Census Bureau
	      This report uses spreadsheets of data obtained from the US Census Bureau, but the contents of this
	      package and report are not endorsed or certified by the Census Bureau. For more information regarding
	      the usage of US Census Bureau data, please visit: http://www.census.gov/developers/tos/terms.html

	(2) - US Energy Information Administration
	      This report uses Gas Price information provided by the US Energy Information Administration, and are
	      available publicly on the web, free to use, though not endorsed by the US Energy Information
	      Administration. See http://www.eia.gov/dnav/pet/pet_pri_allmg_a_EPM0_PTC_dpgal_a.htm for details.

	(3) - JSAnimation Library - Copyright (C) 2013 Jake Vanderplas
	      The JSAnimation Library is provided as an open source library, available on the web and free to use
	      under the BSD Developers license. Information regarding this project may be found at the following 
	      sources:
		GITHUB SRC: https://github.com/jakevdp/JSAnimation
		BSD License Information: http://opensource.org/licenses/BSD-2-Clause

5) GITHUB - Information about this Project on Github
	
	I provide the entirety of my project online, for free, for others to use as either a reference for 
	code or as a method of inspiration. I also host this project on my GitHub for my own personal back up storage,
	as well as my own source of revision control and future project continuation in the future.
	
	You may view my online version of the project at the following location:

	http://www.github.com/Aayrl/python_DataScience




