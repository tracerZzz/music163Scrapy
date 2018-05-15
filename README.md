### 爬取网易云音乐的歌单

#### 框架

1. scrapy

2. scrapy-splash

3. mongodb

4. Python3

5. docker 


```Shell
docer pull  scrapinghub/splash

docker run -p  8050:8050 scrapinghub/splash
```



根据网易云音乐的歌单分类爬取，共爬取72类，歌单，总共十五万左右个歌单，爬取了歌单的封面连接，播放次数，歌单标题，歌单网页连接

```Js
db.getCollection('music163').find({"listenCount":{"$gt":400000}}).sort({"listenCount":-1})
```

#### 播放次数前五名的歌单

```json
/* 1 */
{
    "_id" : ObjectId("5ad623f3784d62ad5a1bdd08"),
    "title" : "华语速爆新歌",
    "link" : "/playlist?id=924680166",
    "realLink" : "https://music.163.com/playlist?id=924680166",
    "listenCount" : 140490000,
    "imgUrl" : "http://p1.music.126.net/aABkbD9nU0f6LWuJnxMoYw==/109951163250541864.jpg?param=140y140"
}

/* 2 */
{
    "_id" : ObjectId("5ad6235a784d62ad5a1b9923"),
    "title" : "【节奏控】那些超带感的音乐（典藏版）",
    "link" : "/playlist?id=306397077",
    "realLink" : "https://music.163.com/playlist?id=306397077",
    "listenCount" : 138260000,
    "imgUrl" : "http://p1.music.126.net/RnOZHM0BNxXuy-RwQQI5BA==/3313928048221849.jpg?param=140y140"
}

/* 3 */
{
    "_id" : ObjectId("5ad62438784d62ad5a1bf9e5"),
    "title" : "【旋律控】超级好听的外文歌",
    "link" : "/playlist?id=310970433",
    "realLink" : "https://music.163.com/playlist?id=310970433",
    "listenCount" : 98860000,
    "imgUrl" : "http://p1.music.126.net/2MsstS-M9w5-li0aRy3sUQ==/1380986606815861.jpg?param=140y140"
}

/* 4 */
{
    "_id" : ObjectId("5ad624b1784d62ad5a1c2ddd"),
    "title" : "那些只听前奏就中毒的英文歌",
    "link" : "/playlist?id=37432514",
    "realLink" : "https://music.163.com/playlist?id=37432514",
    "listenCount" : 93780000,
    "imgUrl" : "http://p1.music.126.net/mQy3lRj6YJ0TW3fM9v85YA==/6643249256145165.jpg?param=140y140"
}

/* 5 */
{
    "_id" : ObjectId("5ad62316784d62ad5a1b78ca"),
    "title" : "【欧美男团】秒杀耳朵系列",
    "link" : "/playlist?id=117377955",
    "realLink" : "https://music.163.com/playlist?id=117377955",
    "listenCount" : 70060000,
    "imgUrl" : "http://p1.music.126.net/FJAxNkFoq3dGiS9tz_bGgQ==/3405187512421439.jpg?param=140y140"
}
```

