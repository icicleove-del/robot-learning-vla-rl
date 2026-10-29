# 官方参考源码导航（**候选标签 v0.6.1**）

> 学习时统一看同一标签，避免把 `main` 和旧教程混在一起；真正运行前需重新核对依赖与 checkpoint 兼容性。本仓库没有克隆或复制上游大仓库。

| 模块 | 参考链接 | 当前问题 |
|---|---|---|
| 模型 | [SmolVLA 模型](https://github.com/huggingface/lerobot/blob/v0.6.1/src/lerobot/policies/smolvla/modeling_smolvla.py) | `forward`, `predict_action_chunk`, `select_action` |
| 数据 | [LeRobotDataset](https://github.com/huggingface/lerobot/blob/v0.6.1/src/lerobot/datasets/lerobot_dataset.py) | 图像、状态、动作、时间窗口 |
| 训练 | [lerobot_train.py](https://github.com/huggingface/lerobot/blob/v0.6.1/src/lerobot/scripts/lerobot_train.py) | loss/optimizer/checkpoint |
| 评测 | [lerobot_eval.py](https://github.com/huggingface/lerobot/blob/v0.6.1/src/lerobot/scripts/lerobot_eval.py) | 环境 rollout/成功率 |
| 环境 | [envs/libero.py](https://github.com/huggingface/lerobot/blob/v0.6.1/src/lerobot/envs/libero.py) | 观测/动作/环境生命周期 |
| 扩展阅读 | [VLA-JEPA](https://github.com/huggingface/lerobot/blob/v0.6.1/src/lerobot/policies/vla_jepa/modeling_vla_jepa.py) | 世界模型的潜在预测损失；此时只读 |
| RL | [RL 代码目录](https://github.com/huggingface/lerobot/tree/v0.6.1/src/lerobot/rl) | 后期 SAC/HIL-SERL，暂不执行 |

## 后续填写的源码审查记录

| 日期 | 版本 / commit | 路径 + 函数 | 输入输出证据 | 已验证/待验证 |
|---|---|---|---|---|
| — | v0.6.1（候选） | 待审查 | 未执行 | 待验证 |
