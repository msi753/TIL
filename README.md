# TIL

구조
```
.
└── docs
    ├── README.md
    ├── guide.md
    └── zh-cn
        ├── README.md
        └── guide.md
```

```
docs/README.md        => http://domain.com
docs/guide.md         => http://domain.com/#/guide
docs/zh-cn/README.md  => http://domain.com/#/zh-cn/
docs/zh-cn/guide.md   => http://domain.com/#/zh-cn/guide
```

# 스크립트 사용여부
```
window.$docsify = {
  executeScript: true,
};
```

```
<script>
  console.log(2333)
</script>
```

# npm 실행시키는 방법
해당 폴더로 이동 후
```
docsify serve ./docs
```