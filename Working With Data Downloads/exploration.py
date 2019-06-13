import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    JJ_vc = data['JJ'].value_counts()
    SCH_STATUS_MAGNET_vc = data['SCH_STATUS_MAGNET'].value_counts()

    print(JJ_vc)
    print(SCH_STATUS_MAGNET_vc)

    pv_JJ = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"],
                         index="JJ", aggfunc="sum")
    pv_MAGNET = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], 
                               index="SCH_STATUS_MAGNET", aggfunc="sum")

    print(pv_JJ)
    print(pv_MAGNET)
