# Narro Design System (MASTER)

> 基于 [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) 推理 + 产品调性定制。  
> 当前测试实现：**方向 B** — Soft UI Evolution + 选择性毛玻璃。

## 方向 B（主推荐）

| 项 | 选择 |
|----|------|
| **风格** | Soft UI Evolution + Selective Glass (Liquid Glass) |
| **模式** | Task-First Dashboard + Story Hero |
| **主色** | `#0d9488` (an-teal-600)，与 `narro-tokens.css` 一致 |
| **字体** | Inter + Noto Sans SC |
| **玻璃面积** | ≈30%（氛围、侧栏、图卡框、Modal）；数据区实心 |

### 玻璃 token

```css
--narro-glass-bg: rgba(255, 255, 255, 0.62);
--narro-glass-bg-strong: rgba(255, 255, 255, 0.88);
--narro-glass-border: rgba(255, 255, 255, 0.72);
--narro-glass-blur: 20px;
```

### 分区规则

| 区域 | 处理 |
|------|------|
| 登录 / 官网氛围 | 流动渐变 + 玻璃卡片 |
| 侧栏 | 轻玻璃 + blur |
| 讲述图卡 | 玻璃外框 |
| 输入 dock / 分数 / 表格 / 报告 | **实心** |
| Modal / Chat 抽屉 | 玻璃面板 |

### 反模式（避免）

- 全屏玻璃 + 小字号分数
- AI 紫粉渐变、霓虹
- 讲述页重度 parallax
- emoji 作功能图标

## 预览测试主题

```
http://127.0.0.1:8000/app?theme=glass-soft
```

退出：页面底部「退出预览」或去掉 `?theme=` 并清除 `localStorage.narro_theme`。

## 文件

| 文件 | 说明 |
|------|------|
| `frontend/styles/narro-theme-glass-soft.css` | 测试主题样式源 |
| `frontend/static/js/theme-preview.js` | URL / localStorage 切换 |
| `.cursor/skills/ui-ux-pro-max/` | UI UX Pro Max Skill（已安装） |
