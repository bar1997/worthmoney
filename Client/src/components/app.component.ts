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
    this.networkService.example().subscribe(response=>
    {
        console.log(response);
    });

    this.networkService.getHeverInfo().subscribe(response=>
      {
          console.log(response);
      });
  }
}
