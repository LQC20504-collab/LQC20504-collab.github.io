# 我的个人网站使用指南

欢迎！这个网站是用 **Hugo + PaperMod 主题**搭建的，部署在 **GitHub Pages** 上。你只需要学会写简单的 Markdown 文章，然后把代码推送到 GitHub，网站就会自动更新（大约 2 分钟）。

---

## 一、网站架构简介

- **Hugo**: 静态网站生成器，把 Markdown 文章变成网页
- **PaperMod**: 简洁美观的主题（就是你现在看到的样式）
- **GitHub Actions**: 自动部署流水线——你推送代码后，它自动构建并发布到 `https://LQC20504-collab.github.io/`
- **giscus**: 评论区服务，评论保存在 GitHub Discussions 里，读者用 GitHub 账号登录后即可评论
- **不蒜子**: 免费的网站访问量/文章阅读量统计服务

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
| 评论区不显示 | 检查 `hugo.yaml` 里 `params.giscus.repoId`/`categoryId` 是否已填；仓库是否开启了 Discussions；是否安装了 giscus 应用 |
| 想让某篇文章不显示评论 | 在文章 front matter 里加一行 `comments: false` |

---

## 六、评论区（giscus）—— 如何开启

这是一次性设置（约 5 分钟）。评论区支持：**GitHub 账号登录**、显示头像和用户名、给评论**点赞（👍）**、按**时间排序**（最新/最旧按钮）。

1. **开启仓库 Discussions**：打开 GitHub 仓库 `https://github.com/LQC20504-collab/LQC20504-collab.github.io` → **Settings → General** → 往下滚动到 **Features** → 勾选 **Discussions** 并保存。
2. **安装 giscus 应用**：浏览器打开 `https://github.com/apps/giscus` → 点击 **Install** → 选择安装到 `LQC20504-collab/LQC20504-collab.github.io` 这一个仓库。
3. **新建评论分类（可选）**：如果仓库 Discussions 里没有分类，先到仓库 **Discussions** 页面新建一个，比如叫 `Comments`。
4. **获取仓库 ID**：打开 `https://giscus.app`，Repository 一栏填 `LQC20504-collab/LQC20504-collab.github.io`，选择分类，页面会自动生成一段嵌入代码。
5. **填入配置文件**：把生成的 `data-repo-id` 和 `data-category-id` 的值，复制到项目根目录 `hugo.yaml` 里 `params.giscus.repoId` 和 `params.giscus.categoryId`（引号内）。如果分类名和默认的 `Comments` 不同，也一并修改 `params.giscus.category`。
6. **发布**：执行 add → commit → push（见第三节），等 2 分钟，文章下方就会出现评论区。

> 小贴士：新文章默认带 `comments: true`（自动开启评论）；若某篇文章不想要评论，在它的 front matter 加一行 `comments: false` 即可。

---

## 七、如何删除评论

评论数据保存在 GitHub 仓库的 **Discussions** 里，删除后刷新网页即生效，**不需要重新推送网站**。

- **删除单条评论**：GitHub 仓库 → **Discussions** 标签 → 找到对应文章的讨论（标题形如 `Comments for: posts/文章名`）→ 鼠标移到该评论上 → 点击右下角的 **⋯** → **Delete**。
- **删除某篇文章的全部评论**：进入该讨论 → 右上角 **⋯** → **Delete discussion**。
- **禁止再评论（锁定）**：进入该讨论 → 右上角 **⋯** → **Lock conversation**。
- 注意：删除的评论无法恢复。

---

## 八、阅读次数与网站访问量

- 每篇博客文章底部显示 **本文阅读 N 次**；所有页面底部显示 **网站访问 N 次 · 访客 N 人**。
- 统计由第三方免费服务 **不蒜子** 提供，无需注册。
- 想关闭统计：把 `hugo.yaml` 里 `params.busuanzi.enable` 改为 `false`，然后 add → commit → push。

---

## 九、内容板块说明

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

## 十、学习资源（可选）

- Markdown 语法速查: <https://www.markdownguide.org/cheat-sheet/>
- Hugo 官方文档: <https://gohugo.io/documentation/>
- PaperMod 主题文档: <https://github.com/adityatelange/hugo-PaperMod/wiki>

祝你写作愉快！🎉
