# True_Reads
A simple machine learning model that helps us display top rated books as well as recommend similar books on a web application.

# Used Technologies:
Flask framework for connecting the backend of the website with the machine learning model
HTML & CSS to build the web application
Bootstrap css framwork to allow us make the web page more user-friendly
Juypter Notebook to run and test our machine learning model
Pandas, Pickle and Numpy library for python

# Working:
This project was mainly divided into to two components whilst recommending the books:
1) Popularity based recommendations
2) Collaborative filter based recommendations

Both these methods can be displayed in my webpage as 'TOP RATED' and 'SEARCH SIMILAR' respectively.

A] Popularity based recommendations:

For this part of the project my main focus was to first find the criteria on which this rating will be based.
The criteria in this project is a simple condition: books with more than 500 reads (or votes incase of my project) and averaging the highest rating amongst itself
This simple  criteria helps us to display 20 top rated books of all time based on the considered data set.

B] Collaborative filter based recommendations:

Similar to popularity based, it also follows a criteria with it being: consider the rating only by users who have reads more than 220 books.
Based on this we can be sure that only those users have are knowledegable in this field will be voting the similar books


