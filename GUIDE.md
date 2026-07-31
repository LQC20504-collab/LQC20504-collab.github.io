# 我的个人网站使用指南

欢迎！这个网站是用 **Hugo + PaperMod 主题**搭建的，部署在 **GitHub Pages** 上。你只需要学会写简单的 Markdown 文章，然后把代码推送到 GitHub，网站就会自动更新（大约 2 分钟）。

---

## 一、网站架构简介

- **Hugo**: 静态网站生成器，把 Markdown 文章变成网页
- **PaperMod**: 简洁美观的主题（就是你现在看到的样式）
- **GitHub Actions**: 自动部署流水线——你推送代码后，它自动构建并发布到 `https://LQC20504-collab.github.io/`

你不需要理解这些工具怎么工作，只要学会下面的操作就行。

---

## 二、如何写一篇博客文章（4 步）

### 第 1 步：创建文章文件

在 `content/posts/` 文件夹下新建一个文件，名字随便起，比如 `我的第一篇文章.md`（建议用英文或拼音命名，避免链接乱码，例如 `my-first-post.md`）。

### 第 2 步：写 front matter 和正文

用记事本或 VS Code 打开这个文件，顶部先写"头部信息"（front matter），然后写正文：

```markdown
---
title: "我的第一篇文章"
description: "一句话描述这篇文章"
date: 2026-07-31
tags: ["随笔"]
---

这是文章正文的第一段。

## 小标题

这里是内容。写 Markdown 很简单：
- 用 `-` 开头可以写列表
- 用 `**文字**` 可以加粗
- 用 `[文字](网址)` 可以加链接
```

### 第 3 步：本地预览（可选）

在项目文件夹 `D:\Develop\github.io` 打开终端，运行：

```
hugo server -D
```

然后浏览器打开 `http://localhost:1313` 就能预览效果。按 `Ctrl + C` 停止预览。

### 第 4 步：发布

把改动推送到 GitHub（见下面"git 推送命令速查"），等大约 2 分钟，网站就更新了。

---

## 三、git 推送命令速查（就 3 个命令）

每次改完内容，在项目文件夹打开终端，依次运行：

```bash
# 1. 把修改的文件加入暂存区（也可以用 git add . 添加全部）
git add .

# 2. 提交修改，-m 后面写本次改动的说明
git commit -m "发布新文章：我的第一篇文章"

# 3. 推送到 GitHub，网站自动更新
git push
```

记住这三步：**add → commit → push**，就像"打包 → 贴上标签 → 寄出去"。

---

## 四、如何更新主题

PaperMod 主题是用 git submodule 安装的，更新命令：

```bash
git submodule update --remote
git add themes/hugo-PaperMod
git commit -m "更新主题"
git push
```

---

## 五、常见问题

| 问题 | 解决方法 |
|---|---|
| 提示 `hugo` 不是内部或外部命令 | 重新打开一个终端窗口（PATH 没刷新） |
| 端口被占用，`hugo server` 报错 | 换个端口: `hugo server -p 1323` |
| 推送后网站没更新 | 等 2 分钟再刷新；到 GitHub 仓库的 Actions 标签页查看是否失败 |
| 文章显示不出来 | 检查 front matter 的 `date` 是否为过去日期，`draft: true` 要删掉 |

---

## 六、内容板块说明

```
content/
├── posts/     博客文章（你以后主要在这里写）
├── about/     关于我（个人简介）
├── projects/  项目作品（展示你的项目）
├── resume/    技能与履历
content-en/        英文版内容（与上面结构对应）
```

想改"关于我"页面，就编辑 `content/about/index.md`，然后执行 add → commit → push 即可。

---

## 七、学习资源（可选）

- Markdown 语法速查: <https://www.markdownguide.org/cheat-sheet/>
- Hugo 官方文档: <https://gohugo.io/documentation/>
- PaperMod 主题文档: <https://github.com/adityatelange/hugo-PaperMod/wiki>

祝你写作愉快！🎉
