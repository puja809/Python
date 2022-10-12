import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Datacluster } from './_commons/datacluster';

@Injectable({
  providedIn: 'root'
})
export class DataCallServiceService {
  
  URL = "https://api.data.gov.in/resource/26a686fb-eff5-4b33-b5e9-7dd6f41fb870?api-key=579b464db66ec23bdd000001dc53dec48c7e45c4558b0a1d29b7b155&format=json&limit=1000";
  constructor(private http: HttpClient) { }

  getAllDataFromServer() {
    return this.http.get<Datacluster>(this.URL, { responseType: 'json' });
  }
}
