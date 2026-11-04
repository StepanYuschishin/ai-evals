# Виступ · 6 слайдів · приблизно 3–4 хвилини

Один сюжет: чи відкривати Ascend IQ для 50 enterprise-акаунтів. Кожен слайд дає аргумент для цього рішення. Модулі — лише джерела, не структура розповіді.

## Слайд 1. HOLD broad rollout to the 50 accounts

Рішення стосується саме запропонованого broad rollout для 50 акаунтів. Понад $2.5m річної вартості акаунтів — контекст, не прогноз втрат. Далі показуємо конкретну причину HOLD, а не переказ шести модулів.

Вплив на рішення: SHIP/HOLD impact: hold this broad rollout until the pricing Hard gate passes; this is not a verdict on an unseen newer build.

Джерела: evidence/business-brief.md, 01-evaluation-strategy/strategy-canvas.md, 06-culture/lab-1-ship-hold-memo.md

## Слайд 2. The pricing answer fails the non-negotiable bar

Ключова різниця: evaluator PASS — спіймав неправильну ціну; agent FAIL — неправильно відповів. Hard — обрана PM policy для матеріальної помилки ціни. Один positive не доводить загальну detection accuracy. Відомі помилки агрегованих labels не змінюють цей конкретний приклад.

Вплив на рішення: SHIP/HOLD impact: this single known Hard failure is sufficient to block the evaluated release, regardless of the overall audit score.

Джерела: 02-failure-discovery/audit-log.md, 03-eval-suites/eval-suite.md, 04-eval-gates/launch-strategy.md, evidence/pricing-replay.json

## Слайд 3. Speed and relevance still need a launch decision

Latency не загублена: це частина базової обіцянки агента. 4.2s — окремий заданий приклад, не production distribution. API Soft не дозволяє віддати клієнтам незахищений P0: за override API функція має бути вимкнена, питання — до людини. Slang і правильна відмова не дорівнюють матеріальній pricing-помилці.

Вплив на рішення: SHIP/HOLD impact: after fixing pricing, resolve or explicitly mitigate the Soft failures; warnings and correct refusals alone should not stop rollout.

Джерела: 04-eval-gates/gate-map.md, 04-eval-gates/launch-strategy.md, 01-evaluation-strategy/strategy-canvas.md

## Слайд 4. Protect the client before approving an exception

Це запропонований план, не вже реалізовані feature flags. Для запуску необхідні докази реалізації потрібних controls. Freshness підтверджує pricing-data owner; fixture59 не гарантує, що live page ніколи не змінилася. QA rerun має перевірити виправлену відповідь, не тільки старий failure.

Вплив на рішення: SHIP/HOLD impact: a documented override can narrow a Soft risk; it cannot bypass the pricing Hard failure or substitute for working controls.

Джерела: 03-eval-suites/eval-spec.md, 04-eval-gates/launch-strategy.md, evidence/decision-register.md

## Слайд 5. The protection plan fits the online budget

Ціни задані в навчальному сценарії. Online headroom45k, total168250. Тон — 50 кейсів/тиждень; fairness50 порівну US/APAC. Немає підстав стверджувати, що перевірки вже працюють чи клієнти задоволені. Portfolio coverage іншого продукту не тягнемо на основні слайди.

Вплив на рішення: SHIP/HOLD impact: the planned protection is within budget, but funding does not turn a failed gate into a pass; audit delay remains an explicit trade-off.

Джерела: 05-scale/lab-2-budget-crisis.md

## Слайд 6. Approve HOLD now; revisit with corrected-build evidence

Фінальний ask: погодити HOLD саме broad rollout, призначити власників і дату review. Не просимо абстрактно більше даних: потрібен конкретний pricing pass та рішення щодо Soft. Це не автоматичний SHIP після одного виправленого рядка; потрібні всі погоджені release criteria.

Вплив на рішення: SHIP/HOLD impact: a corrected build passing the Hard bar, with Soft risks resolved or controlled, can support reconsidering rollout; today’s supplied evidence supports HOLD.

Джерела: 06-culture/lab-1-ship-hold-memo.md, 04-eval-gates/launch-strategy.md, evidence/decision-register.md

## Текст короткого виступу

«Моя рекомендація — HOLD для широкого відкриття Ascend IQ на 50 enterprise-акаунтів на основі наданих даних. Вони платять понад $50k на рік за перевірену інформацію; агент має прискорити доступ до неї і підтримати retention. Він повинен бути і швидким, і правильним.

Конкретний blocker — pricing. Агент назвав $49, хоча reference містить $59, і додав непідтверджені умови. Наш обраний Hard gate допускає нуль таких помилок. Одна помилка є — отже FAIL. У M3 перевірки спіймали цей кейс, але це успіх детектора, не доказ виправлення агента.

Інші результати теж впливають на запуск. Коректна відповідь про відгуки зайняла 4.2 секунди проти target 2.0. API-порівняння не передає перевірені ліміти. Це Soft failures, які потрібно виправити або контрольовано обмежити. Сленг у чернетці дає warning, а правильну юридичну відмову взагалі не блокуємо.

Для pricing потрібні актуальний source, числова перевірка та оцінка умов. API override може дозволити інші можливості лише з вимкненими automated comparisons та human routing. Він не дозволяє обійти pricing Hard failure. Controls ще треба продемонструвати, вони не виникають від написаного документа.

План вкладається в бюджет: $155k online, $168,250 загалом. Для тону і regional quality використовуємо weekly audits, для часу — код. Це свідомий компроміс із затримкою виявлення, а не гарантія безпеки.

Я прошу погодити HOLD broad rollout, власників pricing fix і rerun, дату наступного review. Коли виправлена версія пройде Hard bar, а Soft risks будуть усунені або контрольовані, ми переглянемо рішення про запуск».
