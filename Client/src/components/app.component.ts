import { Component, OnInit } from '@angular/core';
import { NetworkService } from '../services/network-service/network.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Awesome website';
  private category: string;
  private corporation: string;
  private userInput: string;

  constructor(private networkService: NetworkService)
  {

  }

  Search()
  {
    let corporations = [];

    if (0 != this.corporation.length)
    {
      corporations = [this.corporation];
    }

    this.networkService.getCouponsFromSelectedCorporations(corporations, this.userInput).subscribe(response=>
    {
        console.log(response);
    });
  }

  ngOnInit()
  {
    this.category = '';
    this.corporation = '';
    this.userInput = '';
  }
}
