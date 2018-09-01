import { Component, OnInit } from '@angular/core';
import { NetworkService } from '../services/network-service/network.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Awesome website';

  constructor(private networkService: NetworkService)
  {

  }

  ngOnInit()
  {
    this.networkService.getCouponsFromSelectedCorporations().subscribe(response=>
    {
        console.log(response);
    });
  }
}
