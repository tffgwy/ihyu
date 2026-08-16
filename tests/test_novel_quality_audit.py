import unittest

from tools.novel_quality_audit import audit_text
from tools.validate_emotion_plan import validate_plan
from tools.validate_story_state import validate_state


class NovelQualityAuditTests(unittest.TestCase):
    def test_clean_candidate_has_no_findings(self):
        text = (
            "门外的脚步停在第三层。林遥把最后一枚钥匙压进锁孔，"
            "身后的火已经烧到窗帘。她必须在门开之前决定救谁。"
            "\n\n"
            "她选了那个欠她一条命的人。锁芯转动，楼下传来一声枪响，"
            "钥匙却在掌心留下了新的血痕。"
        )
        self.assertEqual(audit_text(text), [])

    def test_meta_and_placeholder_are_reported(self):
        findings = audit_text(
            "本章将说明接下来的规则。\n"
            "主角[姓名待填]终于明白，TODO。"
        )
        codes = {finding.code for finding in findings}
        self.assertIn("meta.chapter", codes)
        self.assertIn("structure.placeholder", codes)


class StateValidationTests(unittest.TestCase):
    def test_minimal_valid_state(self):
        state = {
            "schema_version": "1.0",
            "project": {},
            "rank_scout_status": "data_required",
            "canon": {},
            "chapter_range": {},
            "protagonist": {},
            "open_loops": [],
            "hooks": {},
            "payoffs": {},
            "policy": {
                "local_models_allowed": False,
                "ai_output_is_candidate": True,
                "human_acceptance_required": True,
            },
            "last_accepted_change": {},
        }
        self.assertEqual(validate_state(state), [])


class EmotionPlanValidationTests(unittest.TestCase):
    def test_plan_requires_structured_beats(self):
        plan = {
            "unit_id": "u1",
            "reader_promise": "危险会逼近",
            "emotion_sequence": [
                {
                    "beat": "opening",
                    "emotion": "不安",
                    "cause": "门外有人",
                    "reader_question": "谁在外面",
                    "risk": "主角暴露",
                },
                {
                    "beat": "turn",
                    "emotion": "惊讶",
                    "cause": "钥匙发热",
                    "reader_question": "钥匙是什么",
                    "risk": "失控",
                },
                {
                    "beat": "payoff",
                    "emotion": "期待",
                    "cause": "门锁变化",
                    "reader_question": "门后是什么",
                    "risk": "代价扩大",
                },
            ],
            "turning_point": "主角开门",
            "payoff": "逃生机会出现",
            "cost_paid": "暴露位置",
            "new_state": "门外敌人进入",
            "next_hook": "钥匙留下印记",
        }
        self.assertEqual(validate_plan(plan), [])


if __name__ == "__main__":
    unittest.main()
