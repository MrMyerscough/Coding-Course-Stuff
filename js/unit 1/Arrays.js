/* Unit 1 - Arrays
This example will have you completing tasks using arrays using JS Syntax.
Make sure to run your code in between each task to make sure that program is working correctly before moving on.*/

// Task 1 - Create an array called greetings with at least 5 different ways to say hello. Then, output the string
// at the second index

greetings = ['Hello', 'Hi', 'What\'s up', 'Yo', 'Hey']
console.log(greetings[2])

// Task 2 - 

newGreetings = ['Bonjour', 'Hola', 'Salut', 'Guttentag', 'Hey']
commonGreetings = []
for(i = greetings; i < greetings[greetings.length]; i++){
    for(x = newGreetings; x < newGreetings[newGreetings.length]; x++){
        if(i == x){
            commonGreetings.append(i)
        }
    }
}
console.log(commonGreetings)