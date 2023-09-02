import { DataCallServiceService } from './data-call-service.service';
import { Component, OnInit,ViewChild } from '@angular/core';
import { Datacluster } from './_commons/datacluster';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'ListOfLifeSavingDrugs';
  constructor(private service: DataCallServiceService) { } 
  _dataCluster: Datacluster; 
  displayedColumns: string[] = ['Medicine Name','Type Name'];
    
  ngOnInit() {
    this.service.getAllDataFromServer().subscribe(
        data => {
          console.log(data);
          this._dataCluster = data;
        },
        error=>console.log("unable to fetch data cluster")
      );
  }

}