interface user{
    name:string
    surname:string
    father_name:string
    b_date:string
    email:string
    password:string
    photo:string
    city:string
    schedule:string
    signal:boolean
    id:number
}

interface student extends user{
    clase:string
}

interface teacher extends user{
    subject:string
}

interface subject{
    mark:number
    comment:string
    home_work:string
}

let test_student1 ={
    name: 'nastya',
    surname:'gurak',
    father_name:'ruslanivna',
    b_date:'23.04.2002',
    email:'nastkka@icloud.com',
    password:'12345',
    photo:'url',
    city:'lviv',
    schedule:'ukr,math',
    signal:true,
    id:1,
    clase:'11-b'
}

console.log(student1);