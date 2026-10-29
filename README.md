# Robot Learning: VLA / RL ｜项目 B

> 目标：通过 **一个可复现的机器人学习工程** 深入掌握 VLA / IL / RL 的数据、模型、训练、闭环评测、源码修改和实验方法，形成真实可展示的算法实习成果。

**当前状态（2026-10-29）：仅完成工程脚手架，尚未安装依赖、下载模型、执行训练或取得实验结果。**

## 固定目标与边界

- **求职目标**：2027 年 1 月中旬前争取杭州 VLA / 机器人 RL 算法实习。
- **优先主线（候选，待基线核验后固定）**：LeRobot + SmolVLA + LIBERO。
- **后续 RL 能力**：SAC / HIL-SERL 仿真实践，单独审批后开展。
- **世界模型**：VLA-JEPA、DINO-WM 等按需源码对照；不启动第二个大型训练项目。
- **时间**：项目学习约 2.5 h/天，投递和面试约 1 h/天。
- **与科研关系**：本仓库仅管理求职项目 B；船舶科研项目 A 的研究问题、方案、数据均不在此擅自更改。

## 从哪里开始

1. 打开 [`notebooks/week01_project_driven.ipynb`](notebooks/week01_project_driven.ipynb)：先看 LIBERO 真实任务与 SmolVLA 的源码，再按需补 Python/PyTorch/Transformer/Flow Matching。
2. 对照 [`docs/SOURCE_MAP.md`](docs/SOURCE_MAP.md) 定位固定参考版本的实际代码；不要假装本仓库已包含 LeRobot 上游源码。
3. 对照 [`docs/ROADMAP.md`](docs/ROADMAP.md) 逐关推进；需要下载模型、安装依赖、开始训练或付费时先征得批准。
4. 学习笔记填入 `notes/weekly/`，实验设计写入 `experiments/`，真实结果写入 `reports/`，自主实现代码放在 `src/robot_learning/`。
5. 第一次 push 参照 [`docs/GITHUB_SETUP.md`](docs/GITHUB_SETUP.md)。

## 工程目录

```text
robot-learning-vla-rl/
├── README.md                     # 项目入口与当前真实状态
├── AGENTS.md                     # Codex 的长期项目约束
├── notebooks/
│   └── week01_project_driven.ipynb  # 已有的完整第一周学习 Notebook
├── docs/
│   ├── ROADMAP.md                # 中长期学习与开发路线、关卡
│   ├── SOURCE_MAP.md             # LeRobot 官方源码定位
│   ├── GITHUB_SETUP.md           # VS Code / GitHub 发布与双电脑同步
│   ├── LEARNING_METHOD.md        # 项目驱动学习及验收办法
│   ├── DECISIONS.md              # 重要方案变更与授权记录
│   └── STATUS.md                 # 当前事实、未知、下一步
├── src/robot_learning/           # 自主编写、可审查的教学及算法模块
├── tests/                        # 对自己代码的基本测试
├── experiments/                  # 待执行实验的配置/设计/结果索引
├── reports/                      # 只收录已测得的指标、曲线、失败分析
├── notes/weekly/                # 每周源码与技术资产记录
└── .gitignore                    # 忽略数据、权重、环境和密钥
```

## 目前允许做什么

- 允许：阅读上游源码、整理调用链、编写**小型且不依赖大模型**的概念验证和测试、形成方案。
- 先审批：安装软件/依赖、下载大量数据和权重、执行 GPU 训练、租服务器/付费、切换主模型/仿真平台、上传私有资料。
- **不把开源项目直接改名上传为“原创成果”**；所有个人贡献以 Git diff、测试、实验配置、日志和结果为证据。

## 本仓库当前已有的演示模块

`src/robot_learning/action_queue.py` 是教学用的简化动作块队列，**不是 SmolVLA 的算法实现，也不是个人创新**。其单元测试使用 Python 标准库，不需安装 PyTorch：

```powershell
python -m unittest discover -s tests -v
```

这是第 6 天算法理解练习的一小部分；前几天仍然优先研究官方源码。**此项目没有真实成功率、训练曲线或训练后模型可展示。**
