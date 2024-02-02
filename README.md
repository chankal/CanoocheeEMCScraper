# Web Scraper for Canoochee EMC

	With the goal of making a web scraper, I decided to use canoochee emc’s outage map available at https://outage.canoocheeemc.com:8889. In order to make my scraper, I utilized the outages.json file available in develop tools. This contains all the necessary raw data without having the need to interact with the website. My first step was to make a method that allows me to add a timestamp to each data added. Then, if the request to the url was successful,we first parse the data and then use pandas to data frame our different variables. We then save this formatted data into a csv file which can later be processed for our more specific needs. For example, we can later use the collected latitude and longitude to calculate the location or zip code to add to a bigger data set.
	
    Some issues that may arise include there being no outages at the moment within canoochee emc. This would cause no data to be outputted from the csv file.




## Execution
To run this code, cd to where you have saved this project and type in terminal:
`python3 main.py`

If it seems the program is not running, close any open csv file/excel file and run the program again.
