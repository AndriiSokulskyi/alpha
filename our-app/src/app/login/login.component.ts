import {Component} from '@angular/core';

@Component({
  selector:'app-login',
  templateUrl:'./login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  title = 'Вітаємо в Alpha!';
  textLogin = 'Логін';
  textPassword = 'Пароль';
  textForgot ='Забув пароль';
  textRegistration ='Реєстрація';
}
