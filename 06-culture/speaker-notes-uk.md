# Виступ · 6 слайдів · приблизно 3–4 хвилини

Один сюжет: чи відкривати Ascend IQ для 50 enterprise-акаунтів. Кожен слайд дає аргумент для цього рішення. Модулі — лише джерела, не структура розповіді.

## Слайд 1. Should Ascend IQ launch to 50 enterprise accounts?

Це саме завдання, а не ще один лабораторний exercise. Спочатку пояснюємо продукт і business problem. Далі перевіряємо готовність за labs. Понад $2.5m account value — контекст, не прогноз втрат. Твої метрики: latency, hallucination, UX trust.

Вплив на рішення: DECISION REQUIRED: approve or hold this rollout. Success means fast, source-supported answers—not speed alone.

Джерела: evidence/business-brief.md, 01-evaluation-strategy/strategy-canvas.md

## Слайд 2. The supplied answers contain decision-relevant failures

Це результати агента, не evaluator. Для speed reference — заданий M4 task, а не M2 timing dataset. API не містить чисел у відповіді, тому просте numeric rule не перевіряє всю проблему. Початковий judge помилково покарав правильну відмову.

Вплив на рішення: HOLD EVIDENCE: pricing is wrong and the speed target is missed. The correct legal refusal supports compliance; it does not cancel the failures.

Джерела: 02-failure-discovery/audit-log.md, 04-eval-gates/gate-map.md

## Слайд 3. The pricing evaluator detects the known failure

Позитивний результат тут є, але щодо перевірки. Не стверджуй 100% загальну accuracy: тільки один known positive і мало релевантних negatives. Safety rule тут семантична перевірка, не незалежна code implementation. Три chat checks — не три production controls.

Вплив на рішення: SUPPORTS SHIP READINESS OF THE CHECK: the known example is detectable. It does NOT justify shipping the agent: the flagged answer is still wrong.

Джерела: 03-eval-suites/eval-suite.md, 03-eval-suites/eval-spec.md, evidence/pricing-replay.json

## Слайд 4. One failed Hard gate blocks the proposed release

Ось правило прийняття рішення, яке пов’язує observations з rollout. Для API підписаний waiver не може відкрити P0 без захисту: вимкнути automated comparisons і human routing або fix. Pricing code перевіряє число, judge — умови; reference owner підтверджує freshness. Speed — один sample, не p95.

Вплив на рішення: HOLD: pricing fails a non-overridable Hard gate. Soft exceptions and Advisory warnings cannot compensate for it.

Джерела: 04-eval-gates/launch-strategy.md, 04-eval-gates/gate-map.md

## Слайд 5. The proposed monitoring allocation is affordable

Бюджет не треба перетворювати на ще один HOLD: він PASS за affordability. Але це necessary support, не sufficient readiness. Додатковий online tone65k не влазить у online headroom45k. Portfolio іншого продукту зберігається у evidence bundle, а не використовується для readiness Ascend IQ.

Вплив на рішення: SUPPORTS SHIP ON COST: the planned online allocation fits the cap. It does not establish quality or override the failed pricing gate.

Джерела: 05-scale/lab-2-budget-crisis.md

## Слайд 6. Final recommendation: HOLD this broad rollout

Не п’ять HOLD проти одного SHIP. Це система gates: один Hard failure вирішальний. Позитивні дані про detection та budget не ігноруємо, але вони про інші об’єкти. Пропозиція обмежена supplied batch, не unknown newer build. Конкретний ask: не approve broad rollout сьогодні; призначити fix/rerun і наступний review.

Вплив на рішення: HOLD TODAY ON THE SUPPLIED EVIDENCE—not by majority vote. A corrected build passing the agreed gates can change the decision; that result is not yet recorded.

Джерела: 06-culture/lab-1-ship-hold-memo.md, evidence/decision-register.md, 04-eval-gates/launch-strategy.md

## Текст короткого виступу

«Моя рекомендація — HOLD для широкого відкриття Ascend IQ на 50 enterprise-акаунтів на основі наданих даних. Вони платять понад $50k на рік за перевірену інформацію; агент має прискорити доступ до неї і підтримати retention. Він повинен бути і швидким, і правильним.

Конкретний blocker — pricing. Агент назвав $49, хоча reference містить $59, і додав непідтверджені умови. Наш обраний Hard gate допускає нуль таких помилок. Одна помилка є — отже FAIL. У M3 перевірки спіймали цей кейс, але це успіх детектора, не доказ виправлення агента.

Інші результати теж впливають на запуск. Коректна відповідь про відгуки зайняла 4.2 секунди проти target 2.0. API-порівняння не передає перевірені ліміти. Це Soft failures, які потрібно виправити або контрольовано обмежити. Сленг у чернетці дає warning, а правильну юридичну відмову взагалі не блокуємо.

Для pricing потрібні актуальний source, числова перевірка та оцінка умов. API override може дозволити інші можливості лише з вимкненими automated comparisons та human routing. Він не дозволяє обійти pricing Hard failure. Controls ще треба продемонструвати, вони не виникають від написаного документа.

План вкладається в бюджет: $155k online, $168,250 загалом. Для тону і regional quality використовуємо weekly audits, для часу — код. Це свідомий компроміс із затримкою виявлення, а не гарантія безпеки.

Я прошу погодити HOLD broad rollout, власників pricing fix і rerun, дату наступного review. Коли виправлена версія пройде Hard bar, а Soft risks будуть усунені або контрольовані, ми переглянемо рішення про запуск».
