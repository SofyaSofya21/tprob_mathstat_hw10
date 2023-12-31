# 1) Провести дисперсионный анализ для определения того, есть ли различия среднего роста 
# среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

f = np.array([173, 175, 180, 178, 177, 185, 183, 182])
h = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
s = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])


# fig = sm.qqplot(f, line='45')
# fig = sm.qqplot(h, line='45')
# fig = sm.qqplot(s, line='45')
stats.probplot(f,dist="norm",plot=plt)
stats.probplot(h,dist="norm",plot=plt)
stats.probplot(s,dist="norm",plot=plt)
plt.show()
# по графику, который рассматривался на семинаре, все выборки сильно отклонены от линии в 45 градусов 
# и я бы сказала, что распределение не нормальное, но видимо, я не очень поняла эти графики.
# график по методу из лекции показывает, что хочется видеть)) 

print(stats.shapiro(f)) # ShapiroResult(statistic=0.9775082468986511, pvalue=0.9495404362678528)
print(stats.shapiro(h)) # ShapiroResult(statistic=0.9579196572303772, pvalue=0.7763139009475708)
print(stats.shapiro(s)) # ShapiroResult(statistic=0.9386808276176453, pvalue=0.5051165223121643)
# p-value больше 0.05, значит, распределение нормальное

print(stats.bartlett(f,h,s)) # BartlettResult(statistic=0.4640521043406442, pvalue=0.7929254656083131)
# p-value больше 0.05, значит, дисперсии однородны (это важно, т.к. выборки разного размера)

print(stats.f_oneway(f,h,s)) # F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698694)
# Если принять уровень значимости за 5%, то p-value будет меньше, то есть существуют 
# статистически значимые различия. Если в целях исследования уровень стат значимости будет 1%, то
# результат окажется другим - мы примем гипотезу Н0, говорящую об отсутствии статистически значимых различий

print(stats.tukey_hsd(f,h,s))
# Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
# Comparison  Statistic  p-value  Lower CI  Upper CI
#  (0 - 1)      0.458     0.979    -5.357     6.273
#  (0 - 2)      6.398     0.022     0.837    11.958
#  (1 - 0)     -0.458     0.979    -6.273     5.357
#  (1 - 2)      5.939     0.028     0.561    11.318
#  (2 - 0)     -6.398     0.022   -11.958    -0.837
#  (2 - 1)     -5.939     0.028   -11.318    -0.561

# Статистически значимые различия есть между футболистами и штангистами, между хоккеистами и штангистами.
# Нет значимых различий между ростом футболистов и хоккеистов.
 