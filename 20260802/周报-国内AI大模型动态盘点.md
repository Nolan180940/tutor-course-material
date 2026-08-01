# 本周国内 AI 大模型动态盘点

> **时间窗口**：2026 年 7 月第 4—5 周（7 月 16 日—8 月 2 日，重点覆盖 7 月末这一周）
> 本周国内大模型进入**罕见的密集发布期**：月之暗面、DeepSeek、阿里云先后放出新一代旗舰，竞争格局被迅速改写。

---

## 一、本周要闻概览

| 时间 | 厂商 | 事件 |
|------|------|------|
| 7 月 16 日 | 月之暗面 | 发布 Kimi K3，2.8 万亿参数，全球首个 3T 级开源模型 |
| 7 月 19 日 | 阿里云 | Qwen3.8-Max-Preview 预览版上线（2.4 万亿参数 MoE） |
| 7 月 20 日 | DeepSeek | V4 正式版发布（1.6 万亿参数，业内首创峰谷定价） |
| **7 月 31 日** | **DeepSeek** | **V4-Flash 正式版 API 上线公测**，官方称 V4-Pro 正式版「尽快」发布 |

> 数据来源：新华网、腾讯新闻、阿里云开发者社区等（详见文末参考链接）。

---

## 二、模型能力对比

### 2.1 Kimi K3（月之暗面）
- **规模**：总参数 2.8 万亿，混合专家（MoE）架构，运行时仅激活 896 个专家中的 16 个。
- **上下文**：**100 万 token** 原生长上下文。
- **多模态**：原生支持视觉理解，面向软件工程、知识工作与视觉场景。
- **编程/Agent**：官方称部分编程与 Agent 测试超过 Claude Opus 4.8、GPT-5.5；整体仍落后 Claude Fable 5 与 GPT-5.6 Sol。
- **开源**：完整权重与技术报告于 7 月 27 日发布（HuggingFace / GitHub）。

### 2.2 DeepSeek-V4-Flash（DeepSeek）
- **定位**：走「性价比 + 速度」路线，约 130 亿激活参数。
- **上下文**：**1M 上下文**、最高 384K 输出，支持思考 / 非思考双模式。
- **Agent**：官方称「Agent 能力大幅增强，远超 V4-Pro-Preview」，且同架构未加参数、仅靠重新后训练即实现。
- **生态**：原生支持 Responses API，可直接接入 Codex。

### 2.3 Qwen3.8-Max（阿里云，Preview）
- **规模**：2.4 万亿参数 MoE 旗舰。
- **能力**：较上代 Qwen3.7-Max 在**代码工程（Coding）、专业办公（Cowork）**上显著提升。
- **状态**：预览版，尚非正式版；业内普遍认为是在 Kimi K3 与 DeepSeek V4 双重压力下提前放出。

---

## 三、权威 Benchmark 横向对比

> 说明：三款模型发布密集，各评测为不同时间快照、不同 harness，**分数不可直接相加**。下表采用公开可查的公认评测集（LMSYS Chatbot Arena / SWE-bench 类 / HLE 等），数据口径均标注来源。

| 评测集 | Kimi K3 | DeepSeek V4-Flash | Qwen3.8-Max | 口径 |
|--------|---------|-------------------|-------------|------|
| LMSYS Chatbot Arena | 前端开发**第 1**、综合**第 3** | 未上榜（公测初期） | — | 第三方（LMArena） |
| SWE-bench 类 / SWE Marathon | **第 1** | 两个代码基准**反超 GLM-5.2** | 代码工程较上代显著提升 | 官方/第三方 |
| BrowseComp（浏览检索） | **第 1** | — | — | 第三方 |
| HLE（Humanity's Last Exam） | **大幅落后** Claude Fable（短板） | — | — | 第三方 |
| 综合榜（某聚合分） | 约 1679 分（腾讯网报道） | 独立综合榜「摸到行业头部低档位」 | — | 媒体报道 |

> 小结：**Kimi K3 在编码与 Agent 类评测全面领先、但长程深度推理（HLE）是明显短板**；**DeepSeek V4-Flash 以极小激活参数在代码基准上反超国产旗舰 GLM-5.2**，性价比突出；**Qwen3.8-Max 主打代码工程与办公协同**的定向强化。

---

## 四、价格与可用性

| 模型 | API 定价（每百万 tokens） | 开放渠道 | 备注 |
|------|---------------------------|----------|------|
| Kimi K3 | 输入 **$3** / 输出 **$15** | Kimi、Kimi Work、Kimi Code、API；7/27 开源 | 较前代价格约翻 4 倍 |
| DeepSeek-V4-Flash | 报道称约 **1 元/百万 tokens** 量级（以官方价格页为准） | API 公测（模型名 `deepseek-v4-flash`） | 原生接入 Codex / Responses API |
| Qwen3.8-Max | 预览期按 **百炼 Token Plan 订阅制**（个人/团队） | 仅阿里官方三大渠道（百炼、Qoder CN 等） | 预览版**限时优惠** |

> 价格数据来源：BlockBeats / 月之暗面官方、CSDN、阿里云帮助中心；DeepSeek 具体输入/输出分档价请以官方发布为准。

---

## 五、行业影响分析

1. **价格战加剧，性价比成为分水岭**：DeepSeek V4-Flash 以「约 1 元/百万 tokens + 反超旗舰的代码能力」重新定义性价比下限；Kimi K3 选择高价高规格路线（$3/$15），呈现「**越级性能 vs 极致性价比**」的分化，而非单纯互砍价格。
2. **开源路线全面反扑**：Kimi K3 作为「全球首个 3T 级开源模型」直接冲击开源榜首，并引发海外「蒸馏」质疑——开源阵营的头部之争从「有没有」升级到「是不是真自研」。
3. **峰谷定价等商业模式创新**：DeepSeek V4 首创业内峰谷定价（闲时便宜），配合 Flash 档位，推动「**分档定价 + 按场景选模型**」成为行业标配，进一步利好开发者。
4. **开发者生态争夺白热化**：三家不约而同强化代码/Agent 能力并拥抱 Codex、Responses API 等工具链，意图绑定开发者工作流——谁的工具链好用，谁就赢得下一轮生态。

---

## 六、小结

三款模型的密集发布表明：**国产大模型已从「卷参数」进入「卷性价比 + 卷 Agent 工程化 + 卷开源生态」的新阶段**。对开发者而言，可按场景组合使用——重推理用 Pro 档、高频执行用 Flash 档（呼应「分档选型」的工程化思路），是当下最优解。

---

## 参考链接

- 新华网《中国企业发布全球最大规模的开源模型 Kimi K3》：https://www.xinhuanet.com/tech/20260717/dA893d3a5e1b429eA79D928E02847744/c.html
- 腾讯新闻《DeepSeek-V4-Flash正式版API上线公测》：https://news.qq.com/rain/a/20260731A06YRI00
- 阿里云开发者社区《Qwen3.8-Max 预览版全解析》：https://developer.aliyun.com/article/1749296
- DataLearnerAI《Qwen3.8-Max-Preview 模型卡》：https://www.datalearner.com/ai-models/pretrained-models/qwen3-8-max-preview
- 威易网《DeepSeek V4-Flash 正式版 API 上线》：https://www.weste.net/2026/08-01/DeepSeek-V4-Flash.html
- wan27.org《Kimi K3 跑分全解析》：https://www.wan27.org/zh/blog/kimi-k3-benchmarks
- 知乎专栏《刚刚，月之暗面发布 Kimi K3》：https://zhuanlan.zhihu.com/p/2061358565617563257
- ABMedia《Kimi K3 完整指南 2026》：https://abmedia.io/kimi-k3-complete-guide-2026
- 掘金《DeepSeek V4-Flash 正式版深度解读》：https://juejin.cn/post/7668608790367682595

---

*本文基于公开报道整理，评测数据为各来源快照；涉及第三方评测请以原始报告为准。*
