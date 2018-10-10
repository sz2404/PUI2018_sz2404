# Homework 5 Statement
## Assignment 1 - Citibike Peer Review
In this assignment, I reviewed Nathan Benjamin Caplan (nbc270)'s citibike project. 

## Assignment 2 - Statistical Tests and Literature Review
Three articles were identified from PLOS one to learn more about selected Statistical Tests. 

Results are documented [here](../HW5_sz2404/HW5_sz2404_Part2_README.md)

## Assignment 3 - Reproducing NYC employment project

I followed Professor's notebook and refered to some statistical reference online for value interpretation. 

## Assginment 4 - Citibike 2 questions

In this part, I follower Professor's notebook to process data and produce graphs for the two questions. 

I used January and August data in 2017 for both questions. I think picking the a relatively cold and a relative hot month of the year can make my dataset a bit more comprehensive with being affected a lot by the weather factors. 

For day and night trip seperation, I used 6am and 6pm as a the seperation point. Therefore, between 6am to 6pm is considered as day rides and between 6pm to 6am of the next day is considered as night rides. However, I believe day lights can further affect the number of riders so possibly if studying further, I would use different standards for each month. 

For Manhattan and Brooklyn ride seperation, I used an open source package for Python called Reverse_Geocoder. Infomation for this package can be found [here](https://github.com/thampiman/reverse-geocoder). It is a simple package to based on your coordinates and return address in a JSON format. Referencing some methods from a previous assignment for getting bus info, I used similar method to extract information of the boroughs. However, when I was extracting rides from the dataset. I noticed some entries had the name just as New York City. Therefore, the data I am using in the stats practice might not include all the data. I also created a How-to Guide for Reverse_Geocoder, the ipynb can be found [here](https://github.com/sz2404/PUI2018_sz2404/blob/master/How_to%20Series/How%20to%20Play%20with%20Reverse%20Geocoder%20(1).ipynb). 

However, I think the most accurate way would be using the station ID for location seperation. I looked into the station map online, there seems to be discrepanies between station ID listed on the dataset versus the Station ID number on the map (located [here](https://member.citibikenyc.com/map/)). It can possibly be a csv formatting issue. 

## Collaboration:
I worked along in Assignment 1 and Assignment 3. 
I worked with Chang (Angel) Liu on Assignment 2 for finding literatures on Plos One. 

I consulted Chun-Chieh Tsai, a former CUSP student, for Assignment 4 regarding coverting coordinates to borough names in NYC. 

Special thanks to Sally Zhang, a software engineer, who answered several of my technical question, regarding using append, json file reading etc. 

## Reference:
I referred to many technical links on stackflow and github. Links are documented throughout my notebooks as # statements. 
