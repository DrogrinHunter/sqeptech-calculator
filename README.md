Part 1 – Arithmetic operations on two numbers

Questions
    1. What happens when we call /calc/web/divide/10/by/4 ?

        a. Is the answer accurate (enough)? 
        The app calculates it to be 2.5 - checking this against a calculator, it provides the correct number.
        
        b. Can we make it more accurate? 
        No

    2. What happens when we call /calc/web/divide/7/by/0 ?
        a. How can we handle this in a more user-friendly manner? 
        This would bring back undefined or error on a normal calculator however on this app, it brings back a 500 response (as it's in debug mode). In the terminal, it brings up the error "ZeroDivisionError: division by zero". To make this a more user-friendly view, I would create specific error pages to display a prettier look for the users so they don't think that it's broken or untrustable.

Optional bonuses
    1. Fix any problems identified by the questions above
    2. Make the response prettier.
        a. Include details of the calculation in the response. For example, if we call /calc/web/subtract/4/from/7 show the response as: “7 – 4 = 3”



Part 2 – Arithmetic operations on more than two numbers
Questions:
    1. Does the calc/web/mean endpoint return an accurate (enough) answer?
        a. Can we make it more accurate?
    2. What happens when we supply decimal numbers as parameters to these endpoints?
        a. If the app does not return the correct answer, how can we fix this?

Optional Bonus:
1.	Fix any problems identified by the questions above.



Part 3 – Using JSON payload data
Questions:
    1. What happens if the JSON does not contain a “Numbers” property?
        a. How can we handle this?
    2. What happens if the array in the “Numbers” property is empty, e.g. []
        a. How can we handle this?

Optional Bonus:
1.	Fix any problems identified by the questions above



Part 4 – Return a JSON response
Questions:
    1. It would be nice to have the option to use the calculator in either “Web” mode where the result is returned as a string or “API” mode where the result is returned as JSON in the response body. In practice this functionality is often achieved by varying the URL, for example /calc/web/add/1/to/7 or calc/api/add/1/to/7.
        a. How could this be implemented without needing to create any additional endpoints or functions within the Flask app?


Optional Bonus:
1.	Implement your solution to the question above
