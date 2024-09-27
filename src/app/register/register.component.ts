/*import { Component } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
})
export class RegisterComponent {
  // Propiedades necesarias
  username: string = '';
  password: string = '';
  error: string = '';

  // Método para manejar el registro
  register() {
    // Lógica de registro aquí, por ejemplo, validar datos o llamar a un servicio
    if (!this.username || !this.password) {
      this.error = 'Por favor, completa todos los campos.';
      return;
    }

    // Aquí se podría llamar a un servicio de registro
    console.log('Registrando usuario:', this.username);
    // ... lógica adicional para manejar el registro
  }
}
*/

import { Component } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
})
export class RegisterComponent {
  // Propiedad que contiene los datos del usuario
  userData = {
    username: '',
    email: '',
    password: '',
    password2: ''
  };

  // Mensaje de error
  error: string = '';

  // Método para manejar el registro
  register() {
    // Validaciones simples
    if (!this.userData.username || !this.userData.email || !this.userData.password || !this.userData.password2) {
      this.error = 'Por favor, completa todos los campos.';
      return;
    }

    if (this.userData.password !== this.userData.password2) {
      this.error = 'Las contraseñas no coinciden.';
      return;
    }

    // Aquí se podría llamar a un servicio de registro
    console.log('Registrando usuario:', this.userData.username);
    
    // ... lógica adicional para manejar el registro, como enviar datos a un servicio

    // Reiniciar el formulario después del registro exitoso
    this.userData = { username: '', email: '', password: '', password2: '' };
    this.error = ''; // Limpiar el mensaje de error
  }
}
