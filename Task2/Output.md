Summary Statistics for Numerical Features:
       PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200

Summary Statistics for Categorical Features:
                           Name   Sex  Ticket    Cabin Embarked
count                       891   891     891      204      889
unique                      891     2     681      147        3
top     Braund, Mr. Owen Harris  male  347082  B96 B98        S
freq                          1   577       7        4      644

=== Key Patterns and Trends Suggestion ===
- Survival rates are notably higher among women and first-class passengers.
- Most passengers are aged 20–40; outliers exist for age and fare.
- High positive correlation: SibSp (siblings/spouse) and Parch (parents/children), indicating families travel together.
- Strong negative correlation: Pclass and Fare—higher class means higher fare.
- Outliers: There are extreme values for Fare (e.g., 512), likely wealthy passengers.

=== Basic Feature-level Inferences ===
- Age: Median passenger age is about 28. Many children (Age <12) traveled in 3rd class.
- Fare: Fares skew right; most paid under 50, but with some very large outliers in 1st class.
- Pclass vs Survival: 1st class passengers had far greater survival odds than 3rd.
- Family features SibSp and Parch: Large families less common among survivors; singles/duos fared best.
- Visuals highlight clear class and gender disparities in survival (which is well-established in Titanic EDA).


Output Screenshots:

<img width="745" height="576" alt="Screenshot 2025-08-06 213030" src="https://github.com/user-attachments/assets/88787931-bc11-45ad-a655-8df6e7c755d1" />

