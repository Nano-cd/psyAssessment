from V2 import PsychophysiologicalSystem


class MentalAssessmentSDK:
    class EmotionAnalyzer:
        def __init__(self):
            self.emotion_lexicon = self._load_emotion_dictionary()
            self.temporal_window = 7  # 分析时间窗口(天)

        def _load_emotion_dictionary(self):
            """加载情感词库"""
            return {
                'positive': ['希望', '平静', '成就感'],
                'negative': ['焦虑', '疲惫', '自我怀疑'],
                'neutral': ['例行', '观察', '等待']
            }

        def analyze_journal(self, text):
            """日记文本情感分析"""
            from collections import defaultdict
            emotion_counts = defaultdict(int)
            for word, categories in self.emotion_lexicon.items():
                for term in categories:
                    if term in text:
                        emotion_counts[word] += 1
            return self._calculate_emotional_balance(emotion_counts)

        def _calculate_emotional_balance(self, counts):
            """情感平衡指数计算"""
            total = sum(counts.values())
            if total == 0:
                return 0.5  # 中性值
            return (counts['positive'] + 0.5 * counts['neutral']) / total

    class CognitiveBiasDetector:
        def __init__(self):
            self.bias_patterns = {
                '灾难化思维': r'永远|绝对无法|彻底完蛋',
                '过度概括': r'总是|从不|每个人',
                '心理过滤': r'只[记得|关注]'
            }

        def scan_thoughts(self, thought_record):
            """认知扭曲模式扫描"""
            import re
            findings = []
            for bias, pattern in self.bias_patterns.items():
                if re.search(pattern, thought_record):
                    findings.append({
                        'bias_type': bias,
                        'severity': self._calc_severity(thought_record),
                        'trigger_phrase': re.findall(pattern, thought_record)
                    })
            return findings

        def _calc_severity(self, text):
            """扭曲思维严重程度"""
            return min(len(text) // 10, 10)  # 简单长度模拟

    class StressEvaluator:
        def __init__(self):
            self.biomarkers = {
                'sleep_quality': 0,
                'muscle_tension': 0,
                'mind_wandering': 0
            }

        def continuous_assessment(self):
            """持续压力评估"""
            return {
                'physiological': self._bio_feedback(),
                'cognitive': self._attention_test(),
                'emotional': self._mood_sampling()
            }

        def _bio_feedback(self):
            """模拟生物反馈数据"""
            # 实际应用可接入穿戴设备数据
            return {
                'hrv': 55 + 15 * self.biomarkers['sleep_quality'],
                'skin_conductance': 2 + self.biomarkers['muscle_tension']
            }

        def _attention_test(self):
            """注意力稳定性测试"""
            from random import randint
            return {
                'focus_duration': randint(5, 45),
                'task_switching_cost': randint(100, 500)
            }

        def _mood_sampling(self):
            """随机情绪采样"""
            moods = ['平静', '烦躁', '期待', '倦怠']
            return [moods[i % 4] for i in range(5)]

    class ResilienceGauge:
        def __init__(self):
            self.adversity_log = []

        def record_challenge(self, event, outcome):
            """记录应对事件"""
            self.adversity_log.append({
                'event': event,
                'coping_strategy': [],
                'outcome': outcome
            })

        def calculate_resilience_score(self):
            """心理弹性指数"""
            successes = sum(1 for e in self.adversity_log if e['outcome'] >= 0.5)
            return successes / len(self.adversity_log) if self.adversity_log else 1


class FlowStateMonitor:
    def __init__(self):
        self.flow_conditions = {
            '技能挑战比': 0.6,  # 理想平衡点
            '即时反馈': False,
            '清晰目标': False
        }

    def assess_flow(self, task):
        """心流状态评估"""
        skill_challenge_ratio = task.skill_level / task.challenge_level
        return {
            'flow_probability': self._calc_flow_prob(skill_challenge_ratio),
            'optimization_suggestions': self._generate_suggestions(task)
        }

    def _calc_flow_prob(self, ratio):
        """计算心流概率"""
        return 1 - abs(ratio - self.flow_conditions['技能挑战比'])

    def _generate_suggestions(self, task):
        """生成优化建议"""
        suggestions = []
        if task.feedback_interval > 60:  # 分钟
            suggestions.append("缩短反馈周期至30分钟内")
        if not self.flow_conditions['清晰目标']:
            suggestions.append("拆解任务为更明确的子目标")
        return suggestions


# 集成到主系统
class EnhancedPsychophysiologicalSystem(PsychophysiologicalSystem):
    def __init__(self):
        super().__init__()
        self.assessment_tools = MentalAssessmentSDK()

    def full_psych_scan(self):
        """执行完整心理评估"""
        return {
            'emotional_balance': self._run_emotion_analysis(),
            'cognitive_biases': self._detect_thinking_errors(),
            'stress_level': self._measure_stress_response(),
            'resilience_index': self._gauge_resilience()
        }

    def _run_emotion_analysis(self):
        """情感状态分析"""
        journal_samples = self._collect_journal_data()
        return [self.assessment_tools.EmotionAnalyzer().analyze_journal(j)
                for j in journal_samples]

    def _detect_thinking_errors(self):
        """认知扭曲检测"""
        thought_records = self._load_thought_logs()
        return self.assessment_tools.CognitiveBiasDetector().scan_thoughts(thought_records)

    def _measure_stress_response(self):
        """压力反应测量"""
        return self.assessment_tools.StressEvaluator().continuous_assessment()

    def _gauge_resilience(self):
        """心理弹性评估"""
        return self.assessment_tools.ResilienceGauge().calculate_resilience_score()


# 使用示例
if __name__ == "__main__":
    enhanced_system = EnhancedPsychophysiologicalSystem()

    # 模拟输入数据
    enhanced_system.assessment_tools.ResilienceGauge().record_challenge(
        "项目截止日提前", outcome=0.7)

    # 执行完整评估
    print(enhanced_system.full_psych_scan())
    # 示例输出可能包含：
    # {'emotional_balance': [0.6, 0.55],
    #  'cognitive_biases': [{'bias_type': '灾难化思维', ...}],
    #  'stress_level': {'physiological': {'hrv': 62, ...}},
    #  'resilience_index': 1.0}
