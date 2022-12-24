# TransTaiwan 營運狀態訊息

[TransTaiwan App](https://tools.transtaiwan.com/download.html) 新版自訂營運狀態訊息，預計於App v2.1.6版開始支援。
<br>

TransTaiwan 介接了由[TDX](https://tdx.transportdata.tw/)平台提供的營運狀態訊息，
此資料源目的為加入額外的自訂訊息，以及覆蓋TDX訊息的功能。
<br>

commit至main branch後會進行自動測試，並於測試通過後自動部署至TransTaiwan的伺服器中。
<br>

# 資料格式

訊息資料於`disruptions`資料夾中，命名規則為`{operator}.yml`，如`tra.yml`為台鐵訊息。<br>

目前支援以下營運公司
```
tra:    台鐵
thsr:   高鐵
trtc:   台北捷運
krtc:   高雄捷運
tymc:   桃園捷運
tmrt:   台中捷運
klrt:   高雄輕軌
ntdlrt: 淡海輕軌
```

資料格式為訊息陣列，訊息的格式如下

``` yaml
- AlertID: String
  Title: String
  Description: String
  Status: Int
  Scope: (optional)
    Stations: [ String Array ] (optional)
    Lines: [ String Array ] (optional)
    Trains: [ String Array ] (optional)
    AllStations: Boolean (optional)
  Direction: Int (optional)
  Level: Int (optional)
  StartTime: String yyyy-MM-dd'T'HH:mm:sszzz (optional)
  EndTime: String yyyy-MM-dd'T'HH:mm:sszzz (optional)
```

<!-- 資料詳細說明 -->

- AlertID: 訊息ID，若與TDX訊息ID相同，則會覆蓋該TDX訊息
- Title: 標題，長度限制`4~15`字
- Description: 訊息內容，長度限制`4~255`字
- Status: 訊息狀態，只能是以下其中一個`Int`值
  - `0`: Level.Alert
  - `1`: Level.Normal
  - `2`: Level.Alert
  - `3`: Level.Info
  - `4`: Level.Verbose

  `1` 為營運正常，不會使用到<br>
  `0`、`2`為營運異常，其中`0`為全線營運停止，`2`為有異常狀況<br>
  以上`0`、`1`、`2`繼承了TDX的營運狀態Status，但目前App並不會區分`0`與`2`，皆視為`Alert`<br>
  `3`、`4`為營運正常，但有其他訊息<br>
  `3`與`4`的區別為`4`不會顯示在App主頁的應用狀態列表中<br>
  例如於疫情期間，高鐵全車對號座為`Level.Info`，此訊息會顯示於App主頁<br>
  <br>
  目前於北捷與中捷有常駐的`Verbose`訊息為`中運量時刻表非官方`

- Scope: 訊息範圍 (非必填)
  - Stations: 訊息影響的車站，為車站ID陣列 (非必填)<br>
  如台鐵 `["1000", "1001", "1002"]`，北捷 `["BL10", "BL11", "BL12"]`<br>
  - Lines: 訊息影響的路線ID陣列 (非必填)<br>
  目前只支援捷運路線，如北捷 `["R", "G", "R22A"]`，高雄輕軌 `["C3", "C4"]`<br>
  - Trains: 訊息影響的車次陣列 (非必填)<br>
  只支援台鐵與高鐵。**注意** yaml格式中純數字車次須加`''`將資料格式轉為`String`，如`'371'`
  - AllStations: 是否影響全線車站 (非必填)
- Direction: 訊息影響的方向 (非必填)
  - `0`: 台鐵順行/高鐵南下/捷運正向
  - `1`: 台鐵逆行/高鐵北上/捷運反向
  - `2`: 雙向
- Level: 訊息等級 (非必填)，此訊息繼承TDX的等級，為預留欄位，目前App不使用
  - `1`: 重度
  - `2`: 中度
  - `3`: 輕度
- StartTime: 訊息開始時間 (非必填，但請盡量提供)<br>
  時間格式為`yyyy-MM-dd'T'HH:mm:sszzz`，如`'2022-01-03T16:30:00+08:00'`<br>
  **注意** 須加`''`將資料格式轉為`String`
- EndTime: 訊息結束時間 (非必填，但請盡量提供)<br>
  時間格式同上

以下為一個合法的資料範例

```yaml
- AlertID: tra-alert-202201031630
  Title: 花東地震天然災害
  Description: 受0918地震影響，玉里=富里間路線中斷，改公路接駁，敬請見諒。
  Status: 2
  Scope:
    Stations:
      - '6110'
      - '6100'
      - '6090'
      - '6080'
  Direction: 2
  Level: 2
  StartTime: '2022-09-19T00:09:25+08:00'
  EndTime: '2023-03-19T00:05:00+08:00'
```