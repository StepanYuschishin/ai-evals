# Відповіді на запитання

**Чому HOLD, якщо лише одна неправильна ціна?** HOLD стосується необмеженого rollout на поточних evidence. Помилка підтверджена, але recurrence/root cause невідомі. Не робимо висновку, що всі функції unsafe; оцінюємо restricted alternative після тестів і controls.

**Чи можна просто вимкнути pricing?** Це варіант, не доведена можливість. Треба показати, що boundary працює, affected requests коректно routed, інші задачі пройшли criteria і PM/CPO погодили новий scope.

**Чому не запускаємо pilot зараз?** Немає результатів proposed in-scope tasks і доказу потрібних exclusions/rollback. Ми просимо підготувати pilot proposal, а не підписуємо його автоматично.

**Що доводять три M3 checks?** Кожна flag known pricingrow1. Це detection цього прикладу; не corrected-agent pass, не general recall і не три незалежні production implementations.

**Що таке production accuracy estimate?** Частка правильних відповідей на репрезентативному реальному потоці. Наші 20 навчальних кейсів не дають такої оцінки.

**Чому legal PASS?** Reference каже Refuse legal queries; агент відмовив. Початковий judge помилився. Це урок про evaluator, не launch blocker.

**Що з Hard gate?** Погоджений у лабі pricing Hard діє для candidate з automated pricing. Нова restricted scope потребує окремих criteria й demonstrable isolation; це не waiver failedHard.

**Що з latency?** Один M4 task 4.2s проти2.0s. Це miss tasktarget, не p95/p99. M5 longqueries10s — інший taskclass. Speed є ключовою businesspromise.

**Що з budget?** 85k fabrication +70kcontext=155konline; із6500tone+5500bias+1250timer=168250total. Onlinecap200k. Це planningcosts, не operatingcoverage.

**Що доводить $2.5m?** Лише accountvalue context:50×понад50k/рік. Не forecastloss, agentrevenue чи retentionuplift.

**Що змінить рішення?** Evidence виправлених відповідей і representative in-scope tasks, працюючі controls, погоджені scope/stoprules та CPO/PMapproval.
