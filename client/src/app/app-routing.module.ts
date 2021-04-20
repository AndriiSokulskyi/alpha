import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { LoginComponent } from './login/login.component';
import { ContactsComponent } from './contacts/contacts.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { PoliticsComponent } from './politics/politics.component';

const routes: Routes = [
  {path: '', component: LoginComponent},
  {path: 'contacts', component: ContactsComponent},
  {path: 'forgot-password', component: ForgotPasswordComponent},
  {path: 'politics', component: PoliticsComponent},
  {path: 'about-us', component: AboutUsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }