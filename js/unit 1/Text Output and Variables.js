/* Unit 1 - Text Output and Variables
This example will have you completing tasks using text output and variables using JS Syntax.
Make sure to run your code in between each task to make sure that program is working correctly before moving on.*/

// Task 1 - Create a variable for the number of people that live in your house. Output this variable into the console.

numPeopleInHouse = 2
console.log(numPeopleInHouse)

// Task 2 - Use the readline command to take text input from the user. Ask the user for their favorite color, and then
// repeat it back to them in a sentence.

const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('What is your favorite color? ', (answer) => {
    console.log(`Your favorite color is ${answer}`)
    r1.close()
})

// Task 3 - 