import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';


@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss']
})
export class RegistrationComponent implements OnInit {
  registrationForm!: FormGroup;
  email!: FormControl;
  password!: FormControl;
  user!: FormControl;
  surname!: FormControl;
  user_name!: FormControl;
  father_name!: FormControl;
  b_day!: FormControl;
  submitted!: boolean;

  status = true;
  
  constructor() { 

  }


  createFormControls(){
    this.email = new FormControl("", [
      Validators.required, 
      Validators.pattern("^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")
    ]);
    this.password = new FormControl("", [
      Validators.required,
      Validators.minLength(8)
    ])
    this.user = new FormControl("", [
      Validators.required
    ])
    this.surname = new FormControl("", [
      Validators.required,
      Validators.minLength(2),
      Validators.pattern("[^:$#@^&*/><.,][^0-9]{1,20}")
    ])
    this.user_name = new FormControl("", [
      Validators.required,
      Validators.minLength(2),
      Validators.pattern("[^:$#@^&*/><.,][^0-9]{1,20}")
    ])
    this.father_name = new FormControl("", [
      Validators.required,
      Validators.minLength(2),
      Validators.pattern("[^:$#@^&*/><.,][^0-9]{1,20}")
    ])
    this.b_day = new FormControl("", [
      Validators.required
    ])
  }

  createForm(){
    this.registrationForm = new FormGroup({
      email: this.email,
      password: this.password,
      user: this.user,
      surname: this.surname,
      user_name: this.user_name,
      father_name: this.father_name,
      b_day: this.b_day
    })
  }

  ngOnInit(): void {
    this.createFormControls();
    this.createForm();
  }

  onSubmit(): void {
    this.submitted = true;
    if (this.registrationForm.valid) {
      console.log("Form Submitted!");
      console.log(this.registrationForm.value);
      this.registrationForm.reset();
    }
  }

  changeStatus(): void{
    this.status = !this.status;
  }
}
