/*

//number
let a = 9999999999999999999999999999999n; // BigInt literal
console.log(a);
console.log(typeof a);

//bigint
let b = 999999999;
let c = 999999n;
// let d = b + c //error bigint and number cannot be mixed
// console.log(d); 
console.log(typeof d);

//boolean
let e = false;
let f = true;
console.log(e);
console.log(f);
console.log(typeof e);
console.log(typeof f);

//null
let g = null;
console.log(g);
console.log(typeof g);

//undefined
let h;
console.log(h);
console.log(typeof h);

// String
let i = "vamsi";
console.log(i);
console.log(typeof i);

//type conversion
// converting string to number
let j = "10";
let k = "20pp";
let l = " 3 oo0 9";
let m = Number(j);
console.log(m);
console.log(Number(k));
console.log(Number(l)); // for converting string numbers to number
console.log(parseInt(k)) //for converting if string has number also
console.log(parseInt(l))
console.log(typeof m);

// converting string to boolean
let n = "true";
let o = "false";
let p = "0";
let q = "1";
let r = "";
let s = "null";
let t = "undefined";
console.log(Boolean(r)); //false
console.log(Boolean(s)); //true
console.log(Boolean(t)); //true
console.log(Boolean(p));
console.log(Boolean(q));
console.log(Boolean(n)); 
console.log(Boolean(o)); //true

// converting number to string
let u = 10;
let v = 0;
console.log(String(u)); // "10"
console.log(String(v)); // "0"

//converting number to boolean
let a1 = 1;
let b1 = 0;
let c1 = -1;
let d1 = 0n;
console.log(Boolean(c1)); // true
console.log(Boolean(d1)); // false
console.log(Boolean(a1)); // true
console.log(Boolean(b1)); // false

// converting boolean to number
let y = true;
let z = false;
console.log(Number(y)); // 1
console.log(Number(z)); // 0

//converting boolean to string
let w = true;
let x = false;
console.log(String(w)); // "true"
console.log(String(x)); // "false"


let n = 5;
let row;
for(let i=0;i<n;i++) {
    row = "";
    for(let j=0;j<n;j++) {
        row += "*";
    }
    console.log(row);
}



let n = 5;
let row;
for(let i=0;i<n;i++) {
    row = "";
    for(let j=0;j<i+1;j++) {
        row += "*";
    }
    console.log(row);
}


let n = 5;
let row;
for(let i=0;i<n;i++) {
    row = "";
    for(let j=0;j<n-i;j++) {
        row += "*";
    }
    console.log(row);
}


let n = 5;
let row;
for(let i=0;i<n;i++) {
    row = "";
    for(let j=0;j<n-i;j++) {
        row += "*";
    }
    console.log(row);
}

let n = 0
while (n < 10) {
    console.log(n);
    n++;
}


let n = 0;
do {
    console.log(n);
    n++;
} while (n < 10);


//functions

//no input no output
function first() {
    console.log("This is the first function");
}

// with input and no output
function second(a, b) {
    console.log("The sum of a and b is: " + (a + b));
}

//no input and with output
function third() {
    return "This function returns a string";
}

// with input and with output
function fourth(a, b) {
    return a * b;
}

first();
second(10, 20);
console.log(third());
console.log(fourth(5, 10));

//function types
//1.function declaration
function add(a,b) {
    console.log(a+b);
}
add(2,4);

//2.function expression
let sub = function(a,b) {
    return a - b;
}
console.log(sub(10, 5));

//3. arrow function
let mul = (a, b) => {
    return a * b;
}
console.log(mul(3, 5));

//4. IIFE (Immediately Invoked Function Expression)
(function(a,b) {
    console.log(a / b);
})(10,2);


// Hoisting - moving all variable and function declartions to the top of the code
// stack consists of two - global excution context and execution context
// global execution context  - collect all the function and varibale declartions
// execution context -  collect all the code to get executed
// var inital value is undefined
// let and const inital value is not defined
// let leads to temporal dead zone(tdz) - cannot access the variable before it is declared

console.log(a); // undefined
var a = 10;
console.log(a); //10

console.log(b); // Error: Cannot access 'b' before initialization also leads to tdz
let b = 10;
console.log(b); // 10


// we can call the function before it is declared beacuse of hoisting 
// Function declaration
add();
// function expression
function add() {
    console.log("This is an add function");
}


// scopes in javascript
//1. Global scope - it can be accessed from anywhere in the code
// there is no differnce between var, let and const in global scope

let x = 10;
if(x == 10) {
    console.log(x);
}
for(let i = 0; i < 2; i++) {
    console.log(x);
}
console.log(x);


//2. function scope - it can be accessed only within the function
// there is no difference between var, let in function scope

function fun() {
    var a  = 10;
    console.log(a);
}
console.log(a); // Error: a is not defined


//3. block scope - it can be accessed only within the block
// if you use var, it will breach the block scope and jump to the present outer scope
// now the var is jumped into the global scope so why we will able to access it outside the block

let temp = 10;
if (temp < 20) {
    var ans1 = temp + 10;
    console.log(ans1); 
}
else {
    var ans2  = temp - 10;
    console.log(ans2);
}
console.log(temp); 
console.log(ans1);  // 10 beause var is jumped into the global scope
console.log(ans2);  /

// in this case the var is jumped into the function scope
function fun() {
    if(true) {
        var a  = 10;
        console.log(a); 
    }
    console.log(a); 
}
fun(); // 10


// Object Orientation  - Thinkin in the perspective of objects is known as object orienatation
// it has mainly 3 rules
// 1. The world is the collection of objects
// 2. Every object has certain type and type is imaginary and object is real type not exists
// 3. Every object has certain properties and Behaviours

let student = {
    name :"vamsi",
    age: 20,
    salary: 100000,

    coding : function() {
        console.log("I can code in javascript");
    },

    dancing : function() {
        console.log("I can dance");
    },

    driving : function() {
        console.log("I can drive");
    }
}

console.log(student.name);
console.log(student.age);

student.coding();
student.dancing();


// pass by value - primitive data types are passed by value 
// if you change one value the other not change
let a = 10;
let b = a;
console.log(a); 
console.log(b);

// pass by reference - non primitive data types are passed by reference like objects, arrays, functions
// if you change one value the other also change
let obj1 = {
    name: "vamsi",
    age: 20
};

let obj2 = obj1;
obj2.name = "sai";
console.log(obj1.name); 
console.log(obj2.name);


// Functions as Objects
// function contains properties and methods like objects
// functions properties are name and length
// function methods are call, apply, bind

// first class functions - functions can be treated as values

// functions can be assigned to variables, passed as arguments, and returned from other functions
let a = function add(x,y) {
    console.log(x + y);
}

a(10, 20); 

let b;
b = a;
b(100,200); 

function sub(x, y) {
    return x - y;
}
console.log(sub(50, 30));

// Higher-order functions - functions that take other functions as arguments or return functions as output
function ex(fun) {
    return fun(10, 20);
}

// callback functions - functions passed as arguments to other functions
function mul(x,y) {
    return x * y;
}

console.log(ex(mul)); // 200

// Scope - we can travel in upward direction in the scope but not in the downward direction
//total program is global scoper
let name = "saivamsi"

// Function scope
function outerscoper() {

    let hascar = true;

    // Inner function scope
    function innerscoper() {
        // Inside inner scope if bloock scope
        if(hascar == true) {
            let money = 300000;
            console.log("Name: " + name);
            console.log("Has car: " + hascar);
            console.log("Money: " + money);
        }
    }

    innerscoper();
}

outerscoper();


// closures 

// returning a function from outer function
// functions are first class citizens in javascript so we can return a function from another function
function outerFunction() {
    
    console.log("Outer function ");

    function innerFunction() {
        console.log("Inner function");
    }
    
    // returning the inner function from the outer function
    return innerFunction;
}
let exmp = outerFunction();
exmp(); 


// closures example
// closure are function that have access to the outer function's scope even after the outer function has finished executing
// it is the proces are nees of remembering the variables thatded by the inner function - lexical scoping
function outerFunction() {
    // the total scope is called as closure
    // lexical scope - this variable is accessible even though the outer function has finished executing
    let val = 0; // this is a closure variable that is accessible in the inner function

    function innerFunction() {
        val += 1;
        console.log("Value: " + val);
    }

    return innerFunction;
}

let counta = outerFunction();
counta(); 


// callback functions

// callback functions are functions that are passed as parameter to other functions
function add(x, y) {
    return x + y;
}
// callback function 
function sub(x, y) {
    return x - y;
}
// callback function
function mul(x, y) {
    return x * y;
}

// Higher-order function that takes a callback function as an parameter and executer it later 
function calculator(x,y,callback) {
    console.log(callback(x, y));
}
calculator(10, 20, add); 
calculator(10, 20, sub);
calculator(10, 20, mul);


// Arrays 

let arr = [1, 2, 3, 4, 5];
// accessing elements
console.log(arr[0]); 
console.log(arr[1]);
console.log(arr);

let arr1 = new Array(5); 
arr1[0] = 10;
arr1[1] = 20;
arr1[2] = 30;
arr1[3] = 40;
arr1[4] = 50;
console.log(arr1);

for (let i = 0; i < arr1.length; i++) {
    console.log(arr1[i]);
}

// for of loop
for (let i of arr1) {
    console.log(i);
}


// Array methods

let arr = [1, 2, 3, 4, 5];
// push - adds an element to the end of the array
arr.push(6);
console.log(arr); 
// pop - removes the last element from the array
arr.pop();
console.log(arr);
// unshift - adds an element to the beginning of the array
arr.unshift(10);
console.log(arr);
// shift - removes the first element from the array
arr.shift();
console.log(arr);
// splice - adds or removes or replaces elements from the array
// syntax: array.splice(start, deleteCount, items)
let rem = arr.splice(2, 1); // removes 1 element from index 2
console.log(arr); 

arr.splice(1, 0, 20); // adds 20 at index 1
console.log(arr);

arr.splice(1, 1, 30); // replaces 1 element at index 1 with 30
console.log(arr);

arr = [1, 2, 3, 4, 5];
console.log(arr.indexOf(3)); // returns the index of the first occurrence of the element
console.log(arr.lastIndexOf(3)); // returns the index of the last occurrence of the element
console.log(arr.includes(3)); // returns true if the element is present in the array


let arr = [1,4,9,16];
// map - creates a new array with the results of calling a provided function on every element in the calling array

let up = arr.map((num) => Math.sqrt(num));

console.log(up); 

function filter(num) {
    if (num > 5) {
        return true;
    }
    else {
        return false;
    }
}
// filter - creates a new array with all elements that pass the test implemented by the provided function
let fill = arr.filter((num) => num > 5 ? true : false);
console.log(fill);

// reduce - executes a reducer function on each element of the array, resulting in a single output value

let sum = arr.reduce((total,x) => total + x,0);
console.log(sum);

// find - returns the value of the first element in the array that satisfies the provided testing function
let find = arr.find((num) => num > 10);
console.log(find); 

// findIndex - returns the index of the first element in the array that satisfies the provided testing function
let findIndex = arr.findIndex((x) => x > 10);
console.log(findIndex); 

// sort - sorts the elements of an array in place and returns the sorted array
let sort = arr.sort((a,b) => a - b);
console.log(sort);

let arr2 = ["vamsi","sai","kiran","sai"];
arr2.sort();
console.log(arr2);


// Type of arrays
// 1 - dimensional array

let arr1 = [1, 2, 3, 4, 5];
console.log(arr1);

// 2 - dimensional array
let arr2 = [
    [1,2,3],
    [4,5,6]
]
console.log(arr2);

// 3 - dimensional array
let arr3 = [
    [
        [2,3,4],
        [5,6,7]
    ],
    [
        [8,9,10],
        [11,12,13]
    ]
];
console.log(arr3);


// Shallow copy - creating a copy of another array and if changes made in one array affteced to another array

// in this one dimmesion it will not work
// It has 2 methods to perform - 1. Slice , 2. [...] Spread Operator
let arr = [1,2,3,4,5];
console.log(arr);

let arr1 = [...arr]; // arr.slice()
console.log(arr1);

arr.push(99);
console.log(arr);
console.log(arr1);

// This is a shallow copy 
// In 2d array if one array changes 2 array also affected
// Here in memory the array stores using address so both the arrays points to single array that why if one changes aother also changes
let arr = [[1,2,3],[4,5,6]];
console.log(arr);

let arr1 = [...arr]; // arr.slice()
console.log(arr1)

arr[0].push(100)
console.log(arr) // [[1,2,3,100],[4,5,6]]
console.log(arr1) // [[1,2,3,100],[4,5,6]] // same address in memory so changes made in one array affects the other array

// Deep copy - it is the process creating a sepearate copy of the original array with diff address and if changes made in one array it does not affect the other array
// it can performed by using StructuredClone

let arr = [[1,2,3],[4,5,6]]
console.log(arr)

let arr1 = structuredClone(arr)
console.log(arr1)

arr[0].push(8)
console.log(arr) // [[1,2,3,8],[4,5,6]]
console.log(arr1) // [[1,2,3],[4,5,6]] beacause it is a deep copy and it has a separate address in memory


// Strings  - are immutable in nature and it gets memory in string pool
// Strings can be created in 3 ways
// 1.using - ""
let s1 = "vamsi"
// 2. using - ''
let s2 = 'vamsisai'
// 3.using - `` - backtricks
let s3 = `Hello, ${s2}`

console.log(s1)
console.log(s2)
console.log(s3)

let s4 = "vamsi"
console.log(s1 === s4)

// type is object so we perform strict equals to operation it results in failure
let s5 = new String("vamsi") // object also get the memory in the same string pool same ref if it is already available
console.log(s1 === s5) // false


// String methods

let s = "   vamsi  |   VAMSI@gmail.com | I love javascript and i am full stack developer and my name is vamsi"

let arr = s.split("|")
let name = arr[0].trim()
let email = arr[1].trim()
let bio = arr[2].trim()
// console.log(name)
// console.log(email)
// console.log(bio)

name = name.toUpperCase()
email = email.toLowerCase()
// console.log(name)
// console.log(email)

console.log("-".repeat(10))
console.log(bio.includes("vamsi"))
console.log(bio.indexOf("vamsi"))
console.log(bio.charAt(10))
console.log(email.endsWith(".com") && email.includes("@"))
console.log(email.length)
console.log(bio.slice(0,50))
console.log(bio.replace("vamsi","saivamsi"))
console.log(bio.substring(0,5))
console.log("-".repeat(10))


// synchronous programming - line by line execution after one execution completes then only the other function starts execution
// it makes ui unresponsible and make lagy websites
// it wastes the time when there are independent functions

function loadingimages() {
    console.log("loadingimages started")

    let curr = Date.now();
    let delay = 5000;
    let end = curr + delay
    console.log("loadingimages executing..")
    while(Date.now() <= end) {

    }
    console.log("loadingimages Finished")
}

function loadingcontents() {
    console.log("loadingcontents started")

    let curr = Date.now();
    let delay = 3000;
    let end = curr + delay
    console.log("loadingcontents executing..")
    while(Date.now() <= end) {

    }
    console.log("loadingcontents Finished")
}

function performtask() {
    console.log("performtask started")

    let curr = Date.now();
    let delay = 4000;
    let end = curr + delay
    console.log("performtask executing..")
    while(Date.now() >= end) {

    }
    console.log("performtask Finished")
}

// single line execution
loadingimages() // after completion of this line then only it will enter to another line
loadingcontents()
performtask()


// asynchronous execution -it is the process of seperating normal functions and timer functions
// if you use synchronous it will block execution so we make timer functions as asynchornous so that synchronous function finishes the execution after asynchoronorus function starts
// to happen this we are going to use web API- application programming interface 
// in chrome we use v8 engine it provides the apis to execute asynchronous function in javascript
// javascript is a single threaded and synchrounous execution language
// this disadvanage has been overcomed by using the browsers every browser has seperate engines to run async function
// to execute this outside the browser we are going to use NODEJS it provides the web apis to run in vs code or other platforms

// asynchronours function
function fun1() {
    console.log("Fun1 started execution...")
    let curr = Date.now();
    let delay = 5000;
    let end = curr + delay;
    while(Date.now() <= end) {

    }
    console.log("fun1 finished execution..")
}
// synchronours function
function fun2() {
    console.log("Fun2 started execution...")
    console.log("fun2 finished execution..")
}
// synchronours function
function fun3() {
    console.log("Fun3 started execution...")
    console.log("fun3 finished execution..")
}
// asynchronours function
function fun4() {
    console.log("Fun4 started execution...")
    let curr = Date.now();
    let delay = 5000;
    let end = curr + delay;
    while(Date.now() <= end) {
        
    }
    console.log("fun4 finished execution..")
}

// it is provided by the browser to execute async function 
// timeout is used to add this function to the callbackqueue
// web api of chrome or internet explores or any browser contains [TIMER API,FETCH,OTHER APIS]
// and also provides callbackqueue and microtaskqueue
// after timeout completed it adds the function to the callbackqueue
// there is an event loop - it will check that call stack is empty or not if empty starts execution 
// 4
setTimeout(fun1,5000);
// 1
fun2();
// 2
fun3();
// 3 because it added first to callbackqueue
setTimeout(fun4,3000);


// setInterval() - takes 2 arguments as callback and time
// set interval after the time it add to the callbackqueue unlimited times if you not stop it will executes nonstop
// so for this we are going to use the method clearinterval method that clear the interval time 
// for this we use set timeout and clear interval same

function fun1() {
    console.log("feteching data......")
}

let id = setInterval(fun1,1000);
setTimeout(() => clearInterval(id),10000);

Code	Meaning	When it occurs
200  -OK	-Request succeeded (most common response for successful GET/POST)
201	-Created	-Resource successfully created (e.g., after POST)
301	-Moved Permanently	-Page has been permanently moved (used for SEO and redirects)
302	-Found	-Temporary redirect to another URL
304	-Not Modified	-Client cached version is still valid (used for performance)
400	-Bad Request	-Server couldn't understand the request (invalid syntax)
401	-Unauthorized	-Authentication required (e.g., no or invalid token)
403	-Forbidden	-Access denied (even if authenticated)
404	-Not Found	-Requested resource doesn't exist (most famous error!)
405	-Method Not Allowed	-HTTP method (GET, POST, etc.) not allowed on this route
500	-Internal Server Error	-Generic server error (something broke on the server)
502	-Bad Gateway	-Server received an invalid response from an upstream server
503	-Service Unavailable	-Server is down or overloaded (temporary)


// promises
// example for set timeout of instagram page

// This problem is known as callback hell or  Pyramid of Doom
// this is caused to multiple async functions that are nested so this causes the code readablity issues
// to solve we use promise
function loaddashboard() {
    setTimeout(()=>{
        console.log("user profile loading");
        setTimeout(()=>{
            console.log("user connection loading");
            setTimeout(()=>{
                console.log("user photos loading..");
                setTimeout(()=>{
                    console.log("comments loaded sucesss..")
                },2000);
            },2000);
        },2000);
    },2000);
}

// promise - it has 3 states fulfilled, pending, unfulfilled or rejected
// pending - > fulfilled(.then)  or rejected(.catch)
// and it contains executer function and it automatically executes without calling it
// and it contains 2 functions as resolve and reject
// resolve is success whereas reject is failure
// resolve uses .then method to get info
// reject uses .catch method to get info

let prm = new Promise((resolve,reject)=>{
    console.log("Feteching data...");
    // resolve("success");
    reject("failure");
});
prm
.then((result)=>{
    console.log(result); // success
})
.catch((result) => {
    console.log(result); // failure
});
console.log(prm); // Promise { <state>: "pending" }


// To solve callback hell or pyramid of DOM  we use promises
// example with promise and async

let prm = new Promise((resolve,reject) => {
    console.log("Water boiling started");
    setTimeout(() => {
        console.log("Water boiled successfully");
        resolve();
    },3000);
})

.then(() => {
    console.log("sucesss")
})
.catch(() => {
    console.log("failure")
})


// Example - ecomerece first select product , add cart, go to payment page, complete payment
// Promise contains macro queue and micro queue 
// if macro queue execution is going on and in the micro queue has some functions to execute the after macro fun all the micro functions executes then only it will execute macro
// first priority given to micro tasks
// macro queue conatins the function that are in the promise like the functions that are in the async
// micro queue contains the functions of .then .catch and .final 

function step1() {
    return new Promise((resolve,reject) => {
        console.log("Step - 1 started")
        setTimeout(() => {
            console.log("step - 1 completed");
            resolve();
        },3000);
    });
}
function step2() {
    return new Promise((resolve,reject) => {
        console.log("step - 2 started");
        setTimeout(()=>{
            console.log("step - 2 completed");
            resolve();
        },3000);
    })
}
function step3() {
    return new Promise((resolve,reject)=> {
        console.log("step - 3 started");
        setTimeout(()=>{
            console.log("step - 3 completed");
            resolve();
        },3000);
    });
}
function step4() {
    return new Promise((resolve,reject)=> {
        console.log("step - 4 started");
        setTimeout(()=>{
            console.log("step - 4 completed");
            resolve();
        },2000);
    });
}

// promise chaining 
// if step 1 completed successfully then only step 2 starts this process continous nestedly
step1()
.then(step2)
.then(step3)
.then(step4)
.then(()=>{
    console.log("All steps are completed");
})
.catch(()=> {
    console.log("There is a problem");
});


// async - it is used sepecify a function that the function contains asynchronous functions
// await - it is used to call the async fun it waits in the suspend state in web api after success it get remaining statements executes

function promise() {
    return new Promise((resolve,reject) => {
        console.log("process started");
        setTimeout(()=>{
            console.log("process ended");
            resolve()
        },3000);
    });
}

// without using .then and .catch web api introuduces async and await to increases the redablity and makes the logic easy to understand
async function run() {
    try {
    await promise();
    console.log("Promise successs");
    } catch(e) {
        console.log("failure");
    }
}
run();


// JSON - javascript object notation 
// it used to communtion language between 2 apps like 
// json format of string can be accepted by any programming language
// just we meed to convert the json string to our languge specific object
// we use json.parse to convert json string to javascript object
// we use json.stringify to convert javascript object to json string

let js = {
  "location": {
    "city": "London",
    "country": "United Kingdom",
    "latitude": 51.5074,
    "longitude": -0.1278
  },
  "current_weather": {
    "temperature_celsius": 18.5,
    "temperature_fahrenheit": 65.3,
    "condition": "Partly Cloudy",
    "humidity_percent": 70,
    "pressure_hpa": 1012,
    "wind_speed_kph": 15,
    "wind_direction": "SW"
  },
  "astronomy": {
    "sunrise": "05:30 AM",
    "sunset": "08:45 PM"
  }
}

let ans = JSON.stringify(js)
console.log(ans)


// Api - Api is nothing but a middle man between 2 systems
// consider the exmaple as waiter chief and customer api is like a waiter
// Api doesnt provide any code it just provide a url we use that to access the content related to that api
// so we cant access to their codes directly but when we send a get request to there server the server send back a request to us
// pre implementation of something and provided in the internet is known as api
// ex uber zomato and swiggy uses google map api
// there are so many api just we need to call them accourding to our need
// it reduces our time to built a website because we have differnt types of api for everything you need

// for accessing an api we use fetch(url) and it return a promise
// the promise is returned in the format of byte format because it is directly from the intenet so 
// we need use json method to convert bytes to normal javascript object object so we we can access
// if we use text method then it return in json format but we need to get javascript object so we again use
// promise call back to get the normal javasciprt object
// json object and javascript object are same but the json object has keys and values in double quotes for accessing it is hard
// in javascript object we have keys in normal format and values in double quotes 

// promise 
fetch("https://catfact.ninja/fact")
.then((result) => result.json()) // it will return in byte format
.then((res) => console.log(res))
// .then((ans) => console.log(ans)) // we use this extra line if we text method
.catch(() => {console.log("Api fetching failed..")})


// using async and await
// using await where every it takes time to execute and async when the function is asynchronous
async function fet() {
    const a = await fetch("https://catfact.ninja/fact");
    const ans  = await a.json();
    console.log(ans);
}

fet();


// Http method - to communicate with api there are mainly 5 types
// get - it is used to get the information from the server if you not specify it is automatically get
// post - it is used to create a new resource and send to the server
// patch - it is ued to update something partially
// delete - it is used to delete data from server
// put - it is used to update or replace something from the server 

// get
async function texthttpmethods() {
    let a = await fetch("https://api.restful-api.dev/objects",{method:"GET"})
    let b = await a.json();
    console.log(b);
}

texthttpmethods()

// ff8081819782e69e019880eb364d6029

// post
let s = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
};

async function texthttpmethods() {
    let a = await fetch("https://api.restful-api.dev/objects",
        {
        method:"POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        body: JSON.stringify(s)
    });
    let b = await a.json();
    console.log(b);
    }

texthttpmethods()

// put
let s = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
};

async function texthttpmethods() {
    let a = await fetch("https://api.restful-api.dev/objects/ff8081819782e69e019880eb364d6029",
        {
        method:"PUT",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        body: JSON.stringify(s)
    });
    let b = await a.json();
    console.log(b);
    }

texthttpmethods()


// patch
let s = {
   "name": "Apple MacBook Pro 16 (Updated Name)"
};
async function texthttpmethods() {
    let a = await fetch("https://api.restful-api.dev/objects/ff8081819782e69e019880eb364d6029",
        {
        method:"PATCH",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        body: JSON.stringify(s)
    });
    let b = await a.json();
    console.log(b);
    }

texthttpmethods()

// Delete
let s = {
   "name": "Apple MacBook Pro 16 (Updated Name)"
};
async function texthttpmethods() {
    let a = await fetch("https://api.restful-api.dev/objects/ff8081819782e69e019880eb364d6029",
        {
        method:"GET",
    });
    let b = await a.json();
    console.log(b);
    }

texthttpmethods()

// objects in javascript

const student = {
    name : "vamsi",
    age : 20,
    salary: 100000,

    teach : function() {
        console.log("I can teach javascript")
    }
}

const std = {
    "name" : "vamsi",
    "age" : 20,
    "salary" : 200000,

    "teach" : function() {
        this.console.log("I can teach javascript")
    }
}

for (let key in student) {
    console.log(`key: ${key}, value: ${student[key]}`)
}

for (let key in std) {
    console.log(`key: ${key}, value: ${std[key]}`)
}

let key = Object.keys(student);
let values = Object.values(student);
let entries = Object.entries(student);

let key1 = Object.keys(std);
let values1 = Object.values(std);
let entries1 = Object.entries(std);

console.log(key)
console.log(values)
console.log(entries) // returns key value pair in array format

console.log(JSON.stringify(student)) // converts object to string
console.log(JSON.stringify(std)) // converts string to object


const fetchData = ((callback) => {
    let std = ["vamsi","sai","kiran","mithun"];
    return callback(std);
});

fetchData((data) => {
    console.log(data);
});


class exception extends Error {
    constructor(msg) {
        super(msg);
        this.msg = msg;
    }
}
let c = 10;
try {
let a = 10;
console.log(b);
} catch(error) {
    throw new exception("This is a custom exception");
}
console.log(c);


// call - it is used to call a function with a specific this value and arguments and it calls the function immediately
function greet(name1) {
    console.log(name1 + this.name);
}

let person = {name: "vamsi"};
greet.call(person , "Hello "); // using call method


// apply - it is used to call a function with a specific this values as array and arguments and it calls the function immediately

function greet(name1, name2) {
    console.log(name1 + this.name + " and " + name2);
}
let person1= {name: "vamsi"};
greet.apply(person1, ["Hello ", "Sai"]); // using apply method


// bind - it is used to create a new function with a specific this value and arguments and it does not call the function immediately

function greet(name1) {
    console.log(name1 + this.name);
}

let person2 = {name: "vamsi"};
let boundGreet = greet.bind(person2,"Hello "); // using bind method
boundGreet(); // calling the bound function

*/

// Dom - Document object Model 
// it is the representation of the html document in the form of tree structure
// it is used to manipulate the html document using javascript
// it contains mainly
// document.querySelector - it is used to select the first element that matches the specified selector
// document.getElementById - it is used to select the element by id
// document.getElementsByClassName - it is used to select the elements by class name
// document.getElementsByTagName - it is used to select the elements by tag name
// document.querySelectorAll - it is used to select all the elements that matches the specified selector
// document.createElement - it is used to create a new element
// document.removeChild - it is used to remove a child element from the parent element
// document.appendChild - it is used to append a child element to the parent element
// document.innerHTML - it is used to get or set the html content of an element
// document.textContent - it is used to get or set the text content of an element
// document.style - it is used to get or set the style of an element
