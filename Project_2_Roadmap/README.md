# roadmap-generator

```bash
Roadmap-generator:.
│  frontend-road.json			// 前端路线图
│  README.md
│  roadmap-generator.html		// 可视化编辑页面
│
├─assets
│  └─README
│          1752338432438.png
│          1752398923474.png
│
├─data
│  │  data.json				// 原始json数据（b站up主专栏页的封面接口）
│  │
│  └─pics				// pics数据
│          114248982202583.jpg
│          15241731.jpg
│          ...
│          index.json			// 和data.json中图片对应的索引数据
│
└─utils
        pic_downloader.py		// 下载data.json中图片到pics/
```

### 数据准备

保存 `data/data.json`中的外链图片到 `data/pics `，生成索引 `index.json`

### Roadmap-generator

- 上传 `data/pics/`
- 上传 `data/data.json`   (👉和 `data/pics/index.json` 建立图片对应关系)
- （可选）导入`roadmap.json`数据
- 编辑数据，双击节点编辑list
- 导出node和edge数据

![1752398923474](assets/README/1752398923474.png)
