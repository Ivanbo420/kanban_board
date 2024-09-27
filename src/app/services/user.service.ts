import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'http://localhost:8000/usuarios/api/';

  constructor(private http: HttpClient) {}

  register(userData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}register/`, userData);
  }

  login(username: string, password: string): Observable<any> {
    return this.http.post(`${this.apiUrl}login/`, { username, password });
  }
}
