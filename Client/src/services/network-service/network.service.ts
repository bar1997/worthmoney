import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Response } from '../../models/response';

@Injectable({
  providedIn: 'root'
})
export class NetworkService {
  HOST_NAME = 'localhost';
  PORT = '8080';
  SERVER_URL = 'HTTP://' + this.HOST_NAME + ':' + this.PORT + '/';

  HEADERS = new HttpHeaders({'Content-Type': 'application/json',
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE, PUT'});

  constructor(private http: HttpClient) 
  {
  }

  example(): Observable<Response>
  {
    let body = {a: 'a', b: 'c'};
    return this.http.post<Response>(this.SERVER_URL + 'Example', JSON.stringify(body), {headers: this.HEADERS});
  };
}
