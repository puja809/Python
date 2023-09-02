import { TestBed } from '@angular/core/testing';

import { DataCallServiceService } from './data-call-service.service';

describe('DataCallServiceService', () => {
  let service: DataCallServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DataCallServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
