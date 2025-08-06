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
<img width="732" height="580" alt="Screenshot 2025-08-06 213056" src="https://github.com/user-attachments/assets/0525a928-7557-4239-8ade-621fe231d0ed" />
<img width="736" height="579" alt="Screenshot 2025-08-06 213104" src="https://github.com/user-attachments/assets/86c2dd4e-3172-4387-9e4a-e7a199261c2c" />
<img width="734" height="575" alt="Screenshot 2025-08-06 213112" src="https://github.com/user-attachments/assets/0650fb22-caf8-4efd-8a50-5d446879a413" />
<img width="745" height="577" alt="Screenshot 2025-08-06 213119" src="https://github.com/user-attachments/assets/a12807e6-199f-40f8-a521-4b21b1f6f463" />
<img width="739" height="572" alt="Screenshot 2025-08-06 213127" src="https://github.com/user-attachments/assets/c39bb131-78e1-46b8-b54f-244a071f25e1" />
<img width="723" height="563" alt="Screenshot 2025-08-06 213135" src="https://github.com/user-attachments/assets/206698ec-4614-455a-a903-096cd6d1c761" />
<img width="493" height="576" alt="Screenshot 2025-08-06 213142" src="https://github.com/user-attachments/assets/98b412c5-afb5-4045-a9d4-fcb3c03907ab" />
<img width="492" height="578" alt="Screenshot 2025-08-06 213149" src="https://github.com/user-attachments/assets/08ead8c8-7052-4026-901d-7afa3ec06cb1" />
<img width="490" height="580" alt="Screenshot 2025-08-06 213157" src="https://github.com/user-attachments/assets/58fb20e8-059e-4d0f-b696-db86b3d8fbe4" />
<img width="491" height="575" alt="Screenshot 2025-08-06 213203" src="https://github.com/user-attachments/assets/7a2fb89a-9f9c-4cb7-8d37-98fc3b6596bd" />
<img width="491" height="520" alt="Screenshot 2025-08-06 213208" src="https://github.com/user-attachments/assets/1383582a-c1d9-44e6-8684-993479021d21" />
<img width="492" height="579" alt="Screenshot 2025-08-06 213215" src="https://github.com/user-attachments/assets/a6d9af3f-3cb5-4110-aac0-00099865a71b" />
<img width="486" height="568" alt="Screenshot 2025-08-06 213221" src="https://github.com/user-attachments/assets/5e46955c-c503-445e-8c30-765482f571bc" />
<img width="1919" height="1020" alt="Screenshot 2025-08-06 213327" src="https://github.com/user-attachments/assets/e5af96cb-2a43-4830-a8a3-59a850e4e928" />
<img width="1713" height="892" alt="Screenshot 2025-08-06 213343" src="https://github.com/user-attachments/assets/e012360c-173a-4b77-aee9-6e03ad4e1371" />












