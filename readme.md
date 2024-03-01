# Gettring Ready for Production: Devops, Cloud Computing, Environment Variables, Logging, and Continuous Integration

## Introduction

In this unit, we are adding three new features to our program that will start to prepare your program for use in a production environment.  

You will add the following features:

1.  GitHub Actions to run your tests on GitHub automaticly, which is your first steps toward having an understanding of Deveops.  Make sure that when you push to master, it runs the tests and try to find where it outputs the test results on GitHub.  

2.  Environmnent variables = Environment variables are also important because they are how you provide input to your program.  You use them to store passwords, api keys, etc... It's important to understand how to use them because they are your goto solution for providing input to your program, when you don't want to, or can't ask a user to provide the information.  You need to use Environment variables for API keys or other secure information because if you let an API key appear on GitHub, it will be banned within minutes.  You must create a .env file and put your key there and add the .env file to the .gitignore, so that when you put secret information in your local development environment that it isn't accidently posted to GitHub. Right now we don't have anything secret, so you can just add a key / value pair to identify your local development environment.  Check out my sample .env file [here](.sample.env) 

3.  Logging - Logging is how your program outputs information to external systems and is important for tracking application usage, security, and development, since you can use logging to output data like a print statement; however, as we start working with data in the following units, you will need a more effective way of viewing data in variables.

## Project Enhancements from Assignment 5

Incorporate the functionalities discussed in the lecture videos to your previous assignment. In your program a

## Required Viewing

1. Instructor Video Unit Overview - [here](https://youtu.be/hucp1naTcEY) - Note all the code is on the main branch I ended up making a new repo after I recorded the video.

2. Focus on Logging - [here](https://www.youtube.com/watch?v=pxuXaaT1u3k)

3. Focus on Environment Variables - [here](https://www.youtube.com/watch?v=8dlQ_nDE7dQ)

4. Introduction to DevOps - [here](https://www.youtube.com/watch?v=Xrgk023l4lI)

### Submission Requirements

1. Add a GitHub action to your project by copying my .github folder and the python-app.yml file that is in there and then click on the actions tab on your repository to see that when you push to the main branch that all your tests are run.

2.  Add the .env file and refer to the 

## Grading Rubric (Total: 100 Points)

- **Testing (50 Points):**
  - Comprehensive test coverage near 100% average coverage: 50 Points

- **Functionality (50 Points):**
  - Implementation of command pattern and REPL: 10 Points
  - Interactive calculator commands (add, subtract, multiply, divide): 20 Points
  - Successful plugin architecture integration for dynamic command loading: 20 
Ensure that the functionality aligns with the requirements and demonstrates the effective use of the command pattern and plugin architecture as outlined in the instructor videos.

## Recommended Viewing

