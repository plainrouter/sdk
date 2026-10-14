from enum import IntEnum


class ActionRuleDetailReadRuleWindowDays(IntEnum):
    VALUE_3 = 3

    def __str__(self) -> str:
        return str(self.value)
