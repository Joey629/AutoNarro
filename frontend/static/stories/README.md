# 故事图卡（看图讲故事）

`configs/story_stimuli.json` 定义四则故事的分镜顺序与说明文字。

图卡由 `MAIN_pictures_Standard.pdf` 导入（猫/狗/鸟/羊各 6 张 `panel-01.jpg` … `panel-06.jpg`）：

```bash
python scripts/import_main_pictures.py /path/to/MAIN_pictures_Standard.pdf
```

配置见 `configs/story_stimuli.json`。
