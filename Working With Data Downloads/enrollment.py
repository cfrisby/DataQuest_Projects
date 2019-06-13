import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")

    data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']
    race_gender_cols = ['SCH_ENR_HI_M', 'SCH_ENR_HI_F', 'SCH_ENR_AM_M',
                        'SCH_ENR_AM_F', 'SCH_ENR_AS_M', 'SCH_ENR_AS_F',
                        'SCH_ENR_HP_M', 'SCH_ENR_HP_F', 'SCH_ENR_BL_M',
                        'SCH_ENR_BL_F', 'SCH_ENR_WH_M', 'SCH_ENR_WH_F',
                        'SCH_ENR_TR_M', 'SCH_ENR_TR_F']
    race_gender_sums = data[race_gender_cols].sum(axis=0)
    all_enrollment = data['total_enrollment'].sum()
    race_gender_percentages = race_gender_sums / all_enrollment

    print(race_gender_percentages)
