# 心理-生理维护系统框架 Psychological-Physiological Maintenance System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 项目背景
该项目受程序员调试代码的启发，构建了一个实时监测心理状态的"调试系统"。通过将心理学概念与软件工程术语相结合（如情绪堆积=内存泄漏，强迫性思维=死循环），帮助用户更好地理解和管理心理状态。

## 核心功能
- 🧠 **心理调试器**：包含四大核心模块
  - `EmotionAnalyzer` 情感分析引擎（词库匹配+平衡指数计算）
  - `CognitiveBiasDetector` 认知偏差扫描（正则模式匹配）
  - `StressEvaluator` 压力评估系统（生物反馈模拟）
  - `ResilienceGauge` 心理弹性标尺（逆境事件日志分析）

- 🌊 **心流状态监测**
  - 技能-挑战平衡算法
  - 即时反馈优化建议生成
  - 目标拆解策略推荐

- 📊 **集成评估系统**
  ```python
  def full_psych_scan(self):
      return {
          'emotional_balance': [...],
          'cognitive_biases': [...],
          'stress_level': {...},
          'resilience_index': 0.85
      }
  ```

## 设计理念
1. **程序员友好型心理模型**
   - 将休息重构为"系统维护"
   - 用敏捷开发中的"sprint"概念管理任务周期
   - 采用技术债的隐喻理解情绪堆积

2. **渐进式改善策略**
   - 20-20-20护眼法则集成
   - 碎片化冥想模块
   - 最小可行目标(MVO)设定

## 使用场景

初始化增强型系统
enhanced_system = EnhancedPsychophysiologicalSystem()
记录应对事件
enhanced_system.assessment_tools.ResilienceGauge().record_challenge(
"项目截止日提前", outcome=0.7)
执行完整心理扫描
print(enhanced_system.full_psych_scan())

## 系统架构

├── PsychophysiologicalSystem # 基类系统
└── EnhancedPsychophysiologicalSystem # 增强实现
├── MentalAssessmentSDK # 心理评估工具集
│ ├── EmotionAnalyzer # 情感分析
│ ├── CognitiveBiasDetector # 认知检测
│ ├── StressEvaluator # 压力评估
│ └── ResilienceGauge # 弹性标尺
└── FlowStateMonitor # 心流状态监测

## 后续计划
- [ ] 生物传感器数据接入（HRV/GSR）
- [ ] 心理状态版本控制（Git式快照）
- [ ] 自动生成调试建议的LLM模块

## 贡献指南
欢迎通过Issue提交：
- 新的"心理模式识别算法"
- 生物特征数据采集方案
- 本地化情感词库扩展

## License
MIT License
