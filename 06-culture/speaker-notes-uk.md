# Виступ · 4–5 хвилин

## Головний ланцюжок
Бізнес-проблема → promise і метрики → приклади помилок → перевірка детектора → gate → результат проти bar → бюджет і дія.

## Текст
«Моя рекомендація — поки не відкривати Ascend IQ для всіх 50 акаунтів на підставі цього навчального batch. Причина конкретна: pricing-відповідь не проходить наш Hard gate.

Ascend Analytics продає перевірену ринкову інформацію. Платформа перевантажена; клієнтам довго шукати потрібні інсайти. Ascend IQ має відповідати на питання за секунди і підтримати retention. Але швидкість має цінність лише разом із правильністю відповіді. Тому я вибрав Latency, Hallucination Rate та UX Trust.

У M2 ми порівняли 20 відповідей із джерелами. Наприклад, агент назвав ціну $49, хоча source вже показує $59. У API-порівнянні він замінив факти 500 проти 1,000 запитів на хвилину непідтвердженим маркетинговим формулюванням. Початковий judge також помилився: юридична відмова була правильною за політикою. Отже, оцінювача теж треба перевіряти; 20 відібраних прикладів не дають production accuracy.

У M3 я сфокусувався на неправильній ціні. Усі три перевірки спіймали один відомий pricing-кейс. Для числової помилки достатньо дешевого rule check; judge потрібний для умов і змісту. Але тут важливе розрізнення: перевірка виявила погану відповідь, а не виправила її.

У M4 я задав Hard bar — нуль неправильних актуальних pricing-відповідей. У нас є одна. Тому поточний результат FAIL. Це прямий зв’язок між даними і HOLD. Крім того, відповідь із review-summary зайняла 4.2 секунди проти target 2.0. Це Soft failure, один вимір, не p95. Сленг дає warning; правильна відмова не повинна блокуватись.

У M5 я розподілив бюджет: $85k на fabrication і $70k на context specificity. Разом $155k online, а з аудитами й timing check — $168,250. Tone і регіональну якість перевіряємо вибірково, визнаючи затримку виявлення. Timing не потребує дорогого LLM judge.

Щоб змінити рішення, мені потрібний результат виправленої версії: актуальна source-supported ціна, відсутність непідтверджених умов, проходження Hard gate і вирішення або обмеження інших Soft failures. Мій запит — погодити відповідальних і дату повторного review. Я не стверджую, що агент назавжди неготовий: саме надані докази поки не дозволяють підписати широкий запуск».

## До кожного слайду
### 1. Hold broad rollout on the supplied evidence
Рішення тепер спирається на конкретний FAIL: $49 проти $59, а не на абстрактну відсутність доказів. Це висновок про наданий batch, не про невідому нову версію.
Джерела: 02-failure-discovery/audit-log.md, 04-eval-gates/launch-strategy.md, evidence/business-brief.md

### 2. Clients pay for verified market intelligence
Спочатку поясни продукт: платформа містить дослідження, ціни, відгуки. Агент скорочує ручний пошук. 50 акаунтів і понад $50k/рік — умови brief, не реальна аналітика.
Джерела: 01-evaluation-strategy/strategy-canvas.md, evidence/business-brief.md

### 3. Success means fast, grounded and trustworthy answers
Це твої три метрики з оновленого M1. Не кажи, що вони всі вже виміряні. Time-to-insight є бізнес-ціллю, response latency — лише її частиною.
Джерела: 01-evaluation-strategy/strategy-canvas.md

### 4. The audit provides examples, not a production accuracy rate
Сильний доказ — самі приклади. 55% не називай production failure rate. Funding і colors ще мають неоднозначні labels; головне рішення не залежить від них.
Джерела: 02-failure-discovery/audit-log.md, 02-failure-discovery/failure-taxonomy.md

### 5. The pricing check catches the known error
Це оцінка evaluator на одному known positive, не 100% загальна точність. Семантичне safety rule не стало кодом від назви. Numeric replay справді виконаний, але на тому самому fixture.
Джерела: 03-eval-suites/eval-suite.md, 03-eval-suites/eval-spec.md, evidence/pricing-replay.json

### 6. Detecting a bad answer does not fix it
Тут головний логічний міст. Evaluator PASS означає, що він спіймав помилку. Agent/gate FAIL означає, що відповідь лишилася неправильною. Не плутай ці дві оцінки.
Джерела: 03-eval-suites/eval-suite.md, 04-eval-gates/launch-strategy.md

### 7. Each gate has a different response
P0 pricing — прийнята PM policy з M2/M4, не універсальний закон про будь-яку ціну. API taxonomy P0 vs Soft узгоджуємо лише через відсутність незахищеної експозиції: функція вимкнена, не просто підписаний waiver.
Джерела: 04-eval-gates/gate-map.md, 04-eval-gates/launch-strategy.md

### 8. The supplied speed example misses its target
Не випускай latency з історії: саме швидкість мотивує агента. Але не кажи, що клієнти вже йдуть через ці конкретні 4.2 секунди: цього немає в даних.
Джерела: 04-eval-gates/gate-map.md, 04-eval-gates/launch-strategy.md, 05-scale/lab-2-budget-crisis.md

### 9. Fund the expensive checks where meaning matters
Це навчальна калькуляція, не оплачені контракти. Tone 50/тиждень, bias 50/тиждень 25US/25APAC. Є detection delay і rare misses; $45k не означає, що повний третій tier доступний.
Джерела: 05-scale/lab-2-budget-crisis.md

### 10. Portfolio coverage is a separate exercise
Це appendix-матеріал для вимоги шести модулів. Не аргумент про якість Ascend IQ. Не витрачай на це багато часу в основному виступі.
Джерела: 05-scale/lab-1-coverage-matrix.md

### 11. Launch changes when the evidence changes
Запит на зустрічі: погодити HOLD саме broad rollout на поточних даних, власників і дату повторного evidence review. Моя позиція зміниться, коли є результати виправленої версії.
Джерела: 06-culture/lab-1-ship-hold-memo.md, 04-eval-gates/launch-strategy.md

### 12. The evidence trail is available for every claim
CI приклад пояснює per-dimension blocking. Не використовуй його як додатковий реальний вимір готовності агента. Для кожного спірного рішення є register з причиною і межею доказу.
Джерела: 04-eval-gates/lab-ci-gate-policy.md, evidence/decision-register.md
