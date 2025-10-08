# 1. Минус 5 дней
import datetime

today = datetime.date.today()
five_days_ago = today - datetime.timedelta(days=5)
print("Сегодня:", today)
print("Пять дней назад:", five_days_ago)

# 2. Вчера, сегодня, завтра
from datetime import date, timedelta

today = date.today()
print("Вчера:", today - timedelta(days=1))
print("Сегодня:", today)
print("Завтра:", today + timedelta(days=1))

# 3. Без микросекунд
from datetime import datetime

now = datetime.now()
print("Обычно:", now)
print("Без микросекунд:", now.replace(microsecond=0))

# 4. Разница между двумя датами в секундах
from datetime import datetime

first = datetime(2025, 10, 8, 12, 0, 0)
second = datetime(2025, 10, 8, 12, 5, 30)
diff = (second - first).total_seconds()
print("Разница в секундах:", diff)
