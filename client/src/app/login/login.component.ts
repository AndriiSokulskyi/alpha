import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})



export class LoginComponent implements OnInit {
  loginForm!: FormGroup;
  login!: FormControl;
  password!: FormControl;
  
  status = true;
  constructor() { 

  }

  createFormControls(){
    this.login = new FormControl("", [
      Validators.required, 
      Validators.pattern("^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")
    ]);
    this.password = new FormControl("", [
      Validators.required,
      Validators.minLength(8)
    ]);
  }

  createForm(){
    this.loginForm = new FormGroup({
      login: this.login,
      password: this.password
    })
  }

  ngOnInit(): void {
    this.createFormControls();
    this.createForm();
  }

  onSubmit(): void {
    if (this.loginForm.valid) {
      console.log("Form Submitted!");
      console.log(this.loginForm.value);
      this.loginForm.reset();
    }
  }

  changeStatus(): void{
    this.status = !this.status;
  }
}