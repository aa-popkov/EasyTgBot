from typing import NamedTuple


class BudgetMenu(NamedTuple):
    balance: str = "⚖️ Баланс"
    accounting: str = "💵 Учёт"
    reports: str = "📊 Отчеты"
    settings: str = "🙋‍ Настройки"
