import { Component } from '@angular/core';
import { UserService } from '../../../../services/user.service'
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  error: string = '';

  constructor(private userService: UserService) {}

  login() {
    this.userService.login(this.username, this.password).subscribe({
      next: (response) => {
        console.log('Login exitoso', response);
        // Aquí puedes manejar el almacenamiento del token o redirigir al usuario
      },
      error: (error) => {
        this.error = 'Error de login: ' + error.error.detail;
      }
    });
  }
}
