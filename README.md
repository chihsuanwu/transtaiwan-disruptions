# TransTaiwan 營運狀態訊息

### 資料格式

yaml檔，格式如下

``` yaml
- AlertID: String
  Title: String
  Description: String
  Status: Int (0 Level.Alert (TDX全線營運停止), 1 (TDX全線營運正常, 這邊不會使用), 2 Level.Alert (TDX有異常狀況), 3 Level.Info, 4 Level.Verbose)
  Scope: (optional)
    Stations: [ (String Array of station id) ] (optional)
    Lines: [ (String Array of line ID) ] (optional)
    Trains: [ (String Array of trainNo) ] (optional)
    AllStations: Boolean (optional)
  Direction: Int (0, 1, 2, 2 for both direction) optional
  Level: Int (1:'重度',2:'中度',3:'輕度') optional
  StartTime: String yyyy-MM-dd'T'HH:mm:sszzz (ex: 2022-01-03T16:30:00+08:00 optional)
  EndTime: String yyyy-MM-dd'T'HH:mm:sszzz (optional)
```