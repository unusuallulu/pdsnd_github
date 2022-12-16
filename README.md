>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
16 December 2022

### Project Title
Explore US Bikeshare Data

### Description
Describe what your project is about and what it does
In this project, we used data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.

We compared the system usage between three large cities: Chicago, New York City, and Washington, DC.

We computed a variety of descriptive statistics, to help us understand the following:
* Popular times of travel
* Popular stations and trips
* Trip duration
* User information

At first, the program prompts the user to choose which city they want to perform analysis on.
Then the user is asked to specify a month, from January to June. Next the user specify a day of week to filter by.
Alternatively, the can opt for no month and day filtering by entering "All".

Now with these three information(city,month,day) the program will begin loading the data through load_data() function.

Next is where the calculations are made, the program will display all the following:
* Statistics on the most popular time of travel:
- The most popular month
- The most popular day
- The most popular hour

* Statistics on the most popular stations and trips:
- The most popular start station
- The most popular end station
- The most popular combination of start and end stations

* Statistics on trip duration:
- The total travel time
- The average travel time

* User statistics:
- General breakdown of users : in terms of their type(subscriber or customer) and gender(male or female)
- General breakdown of users birth year: oldest, youngest and most popular.

At the end, the program asks the user whether they want to see the first few rows of trip dats.
if the user choose yes: first few rows are displayed. Then the user is again prompted to decide whether to continue or not. This prompt is kept on repeat until the user decides 'No'. 

### Files used
File data for three cities:
* chicago.csv
* new_york.csv
* washington.csv

### Credits
