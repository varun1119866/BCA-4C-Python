//array is store in array,array is storing data types
const arr=[
    'anshu',
    124,
    ['ram','sham','yash']
]
//object {curly brakets  are used for object}
let data={
    firstName: "anshu",
    lastName: "kumari",
    id: 123,
    email: "anshukumari95601@gmail.com"
}

console.log (data.firstName)//output anshu //value ko access krne ke liye ,agar object me value nhi hai toh error aayega
console.log(data["full Name"])//changing value in object
data.last name="pandey"
console.log(data.lastName)//change kiya hai last name and change ho jayega
console.log(data.hasOwnProperty('lastName'))// output true
//OBJECT INSIDE A OBJECT:
let data={

    fullname:{
        firstName:"anshu",
        lastName:"kumari",
    }
    id=123,
    email:"anshukumari95601@gmail.com"
}
//accessing object:
console.log(data.fullname.lastName)
console.log(data.hasOwnProperty("lastname"))//boolean output false

//MERGING AN OBJECT:
const info={
    car: "creta",
    bike: "bullet"
}
const details{
    colour: "red",
    model: 25
}
const fulldetails = Object.assign(info.details)
console.log(fulldeatails);
//output{car:'creta',bike:'bullet',clour:'red',model:25}

//OBJECT INSIDE ARRAY:
const val=[
    {
        id: 1,
        name="anshu"
    }
    {
        id: 2,
        name="kumari"
    }
]
console.log(val[1].name)
const val=[
    {
        id: 1,
        name="anshu"
    }
    {
        id: 2,
        name="kumari"
    }
]
//particular index ke liye
console.log(val[1].name)
output{id:2,name:'kumari'}

console.log(val[1].name)
//output->

//FUNCTION IN OBJECT
const val=[
    {
        id: 1,
        name="anshu",
    },
    {
        id: 2,
        name="kumari",
    }
]
console.log(Object.entries(val))//sari entery cheak krne ke liye 