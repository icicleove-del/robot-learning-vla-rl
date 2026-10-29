# Windows + VS Code：将本仓库发布到 GitHub

## 路径 1（推荐）：VS Code 内置 Git

1. 将 ZIP 解压，得到真正的 `robot-learning-vla-rl` 文件夹；例如放在 `D:\codex\robot-learning-vla-rl`。不要只在压缩包预览窗口打开文件。
2. VS Code → 文件 → 打开文件夹，选择 `robot-learning-vla-rl`。
3. 确认 Git 已安装：VS Code 终端输入 `git --version`。
4. 按 `Ctrl+Shift+G` 打开源代码管理，点 **Initialize Repository（初始化仓库）**。
5. 先审查 `.gitignore` 和待提交文件；在源代码管理中 Stage 文件，填写 `chore: initialize robot learning project`，点击 Commit。
6. 在命令面板 `Ctrl+Shift+P` 中选择 **Git: Publish to GitHub**（显示名称可能为 Publish to GitHub），根据提示登录，仓库名称用 `robot-learning-vla-rl`，**优先选择 Private**。
7. GitHub 网页核验是否有 `README.md`、`AGENTS.md`、`notebooks/week01_project_driven.ipynb`，并检查没有数据、模型权重或密钥。

官方说明：https://code.visualstudio.com/docs/sourcecontrol/repos-remotes

## 路径 2（命令行，仓库尚无 .git 时）

从根目录打开 PowerShell：

```powershell
git init -b main
git status
git add .
git status
git commit -m "chore: initialize robot learning project"
```

之后在 https://github.com/new 新建**空白**的 `robot-learning-vla-rl` 私有仓库（**不要**勾选初始 README / .gitignore / License），将 `<GITHUB_USERNAME>` 替换成你的账号：

```powershell
git remote add origin https://github.com/<GITHUB_USERNAME>/robot-learning-vla-rl.git
git push -u origin main
```

**不要把 GitHub 密码或 token 粘贴进代码或聊天；按 Git Credential Manager / 浏览器授权提示登录。**

## 两台电脑保持同一个项目

**第二台电脑第一次：** `git clone https://github.com/<GITHUB_USERNAME>/robot-learning-vla-rl.git`，用 VS Code 打开克隆目录。

**每次换电脑：** 开始工作前 `git pull --ff-only`；保存完成后 `git status` → `git add ...` → `git commit -m "..."` → `git push`。确认当前电脑推送成功后再换另一台电脑继续。

Git 不会实时同步未提交文件；若两台电脑同时修改相同文件，会产生合并冲突。不要使用 `git push --force` 处理冲突。

## 不上传什么

- Hugging Face 权重、LIBERO 数据集、大量视频、checkpoint、cache、`.env` 和任何密钥。
- 初始仓库不需要 Git LFS；若未来必须发布大型成果，先评估 Hugging Face Hub / GitHub Release / Git LFS 的容量与费用。
- 每次 Push 前执行 `git status` 并检查变更列表。
