
# 배경에 이미지 넣는 방법
```
background-image: url('https://www.ancient-origins.net/sites/default/files/field/image/Agesilaus-II-cover.jpg');
background-position: center;
background-size: cover;
```

# 폰트 넣는 방법
```
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">
<style>
    * {
        font-family: 'Jua', sans-serif;
    }
</style>
```

# 양 옆에 여백을 동일하게 주고 싶을 때
```
.wrap {
    width: 300px;
    margin: auto;
}
```
width를 300으로 줄이니 공간이 생겨서 margin을 auto로 주니 가운데 정렬이 가능해졌다.
