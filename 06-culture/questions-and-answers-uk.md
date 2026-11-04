# Підготовка до запитань

**Чому HOLD?** У перевіреній відповіді ціна $49, а source $59. Ми задали Hard bar 0 неправильних pricing-відповідей. Є 1 failure; виправлений прогін відсутній. Це висновок про надану версію/вибірку.

**А якщо нова версія вже все виправила?** Покажіть її відповіді та результати тих самих критеріїв. Тоді переглянемо рішення; не переносимо старі failures на невідому нову версію.

**Чому detector PASS, а запуск HOLD?** Detector виконав свою задачу — спіймав неправильну відповідь. Product answer усе ще FAIL. Це різні об’єкти оцінювання.

**Це 100% detection?** Тільки 1 із 1 на цьому in-sample case. Одного positive і переважно unrelated прикладів недостатньо для загальної якості або recall.

**Звідки counts?** M3 показує 0 на row1 і 1 на решті 19. M2 row1 failed, отже caught 1/1. Всі 9 original audit-passed rows пройшли pricing check, отже false alarms 0/9. Це не означає, що решта 19 правильні загалом.

**Чому ціна — P0?** Це обрана PM release policy для materially wrong pricing у decision-support продукті. Курсова матриця дає високий пріоритет через high-impact і high tag frequency. Та tag frequency не є production prevalence й не доводить, що кожна похибка ціни — катастрофа.

**Чому API P0 в taxonomy, але Soft?** Запускати незахищений P0 через підписаний waiver не можна. За планом override лише дозволяє інші features після вимкнення API comparison та human routing. Якщо таке обмеження недоступне — виправляємо або тримаємо запуск.

**Чому latency не головний blocker?** Вона центральна для promise. Але accurate answer за 4.2s — Soft проти 2.0s; wrong price — Hard. Швидкість не компенсує матеріальну помилку.

**2 чи 10 секунд?** 2.0s — конкретний review-summary task M4. >10s — long multi-step query failure M5. Це різні task classes; вони не задають єдиний production SLA.

**Чи fairness перевірена?** Ні. Відсутність fairness flags у 20 загальних кейсах не є fairness audit. M5 бюджет передбачає 25US/25APAC із matched cases і спільною rubric щотижня.

**Що означає $2.5m?** 50 акаунтів × мінімальний орієнтир $50k/рік. Це account-value context, не очікуваний збиток, не дохід агента і не retention uplift.

**Чому $155k, а не весь cap?** Повні tiers fabrication85 + context70 + tone65 дали б $220k online, вище $200k. Не витрачаю headroom без обґрунтованого варіанта. Total із fallback = $168,250.

**Чи checks вже в production?** Ні. Є chat evaluation, executable narrow fixture replay та дизайн controls. Не заявляю реалізований pipeline, feature flags, staffed audit чи rollout.

**Навіщо AI Report Summaries?** Це окрема portfolio-лаба M5, appendix для демонстрації coverage prioritization. Вона не є даними про Ascend IQ.

**Який один наступний крок?** Engineering виправляє source/current pricing; QA проганяє corrected output через agreed criteria. Після цього повертаємось до rollout-рішення.
