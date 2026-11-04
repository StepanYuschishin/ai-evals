# Виступ · 5 слайдів · приблизно 3 хвилини

«Наше завдання — вирішити, чи відкривати Ascend IQ для 50 enterprise-акаунтів, які платять понад $50k на рік за перевірену інформацію. Агент має скоротити час пошуку й підтримати retention. Я рекомендую поки не схвалювати необмежений запуск і підготувати обґрунтований варіант обмеженого пілота.

Що ми знаємо? У навчальних логах агент назвав $49 замість актуальних $59, некоректно сформулював API-порівняння, а одна відповідь зайняла 4.2 секунди проти target 2.0. Це конкретні дефекти. Ми не знаємо їхню production частоту і не довели, що всі можливості продукту небезпечні. Три перевірки M3 спіймали pricing-кейс, але це показує detection, а не виправлення відповіді.

Тому я порівняв варіанти. Відкрити все всім зараз — доказів недостатньо. Зупинити кожну можливість до усунення будь-якого ризику — надмірно, такого наші дані не доводять. Кращий наступний крок — hold broad rollout і перевірити, чи можна підготувати narrower pilot без неперевірених функцій. Це ще не дозвіл почати його.

Захист має бути пропорційним. Для ціни — актуальне джерело, числова перевірка та review умов; треба з’ясувати source, retrieval чи generation cause. Для API — контекстна перевірка й обмеження до fix. Для speed — representative timing. Тон чернетки дає warning, а правильна legal refusal проходить. Бюджет такого плану: $155k online, $168,250 разом, online cap $200k. Але план і гроші не означають, що controls уже працюють.

Мій запит: не approve broad rollout сьогодні. Engineering і pricing owner пояснюють та виправляють або ізолюють дефект; QA перевіряє виправлені відповіді та решту proposed scope. Ми визначаємо pilot scope, stop rules, демонструємо routing/rollback й узгоджуємо review date. Після результатів CPO може погодити пілот. Це рішення можна змінити новими доказами».

## Нотатки до слайдів
### 1. Decide whether to launch to 50 enterprise accounts
Завдання — вирішити readiness broad rollout, не переказати курс. HOLD означає не схвалити необмежений запуск на наявних даних. Це не заборона всіх експериментів. Понад $2.5m account value не дорівнює forecast loss.
Джерела: evidence/business-brief.md, 01-evaluation-strategy/strategy-canvas.md

### 2. The labs expose risks—and a way to detect one
Це фактичні відповіді та результати з лаб. Ніякого 50% production accuracy. Три chat checks дали fail pricingrow1; це один known positive, не три незалежні implementation. Відома pricing-помилка потребує rootcause й нового output. Legal refusal не окремий launch аргумент: він в appendix показує evaluator falsealarm.
Джерела: 02-failure-discovery/audit-log.md, 03-eval-suites/eval-suite.md, 04-eval-gates/gate-map.md

### 3. A pricing failure does not automatically require a total shutdown
Тут прибираємо circularreasoning: «Hard тому HOLD». Material pricing concern — potential wrongpurchasing, але одна помилка не доводить системність. Не видаємо disabledpricing за готове featureflag. Rootcause може бути sourcefreshness retrieval generation. M4 initial Hardpolicy переглядаємо для scope: failed pricing блокує candidate що включає pricing, не будь-який isolated scope.
Джерела: 04-eval-gates/launch-strategy.md, evidence/managerial-decision.md

### 4. Keep checks proportional to the risk and cost
M5 dollars — listed costs planning. $85k fabrication+$70kcontext155k. Toneaudit6500 bias5500 timer1250total168250. Це не гарантія і не proof controls працюють. M4 speed2s vs M5 longtask10s distinct. Correctlegalrefusal PASS за policy, slangeditable warning. Не приховуємо M2 API P0/M4Soft: не допускаємоunmitigated exposure.
Джерела: 03-eval-suites/eval-spec.md, 04-eval-gates/launch-strategy.md, 05-scale/lab-2-budget-crisis.md

### 5. HOLD broad rollout; return with a testable pilot proposal
Чіткий ask сьогодні: не approve broad50; призначити workowners і evidence reviewdate. Пілот може бути обмежений по accounts та capabilities, але його size/dateне вигадуємо. Hardbar0pricing застосовний коли scope включаєpricing; виключення лише при доведеному boundary й новомуapprovedcandidate. Далі масштабування based evidence, не автоматично.
Джерела: evidence/managerial-decision.md, 06-culture/lab-1-ship-hold-memo.md