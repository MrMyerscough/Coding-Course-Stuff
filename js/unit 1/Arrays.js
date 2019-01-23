/* Unit 1 - Arrays
This example will have you completing tasks using arrays using JS Syntax.
Make sure to run your code in between each task to make sure that program is working correctly before moving on.*/

// Task 1 - Create an array called greetings with at least 5 different ways to say hello. Then, output the string
// at the second index

let greetings = ['Hello', 'Hi', `What's up`, 'Yo', 'Hey']
console.log(greetings[2])

// Task 2 - 

let newGreetings = ['Bonjour', 'Hola', 'Salut', 'Guttentag', 'Hey']
let commonGreetings = []
for(let i = 0; i < greetings.length; i++){
    for(let x = 0; x < newGreetings.length; x++){
        if(greetings[i] === newGreetings[x]){
            commonGreetings.push(greetings[i])
        }
    }
}

// for(let greeting1 of greetings){
//     for( let greeting2 of newGreetings){
//         if(greeting1 === greeting2){
//             console.log(greeting1)
//         }
//     }
// }
console.log(commonGreetings)