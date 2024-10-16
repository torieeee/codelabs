


"""df=pd.read_excel("E:/Downloads/Test Files.xlsx")

print(df.info())

df[["Surname","Other Names"]]=df["Student Name"].str.split(",",expand=True)

df["Surname"]=(
    df["Surname"]
    .astype(str)
    .str.replace("'","",regex=False)
    .str.strip()
    )
df["Other names"]=(
    df["Other names"]
    .astype(str)
    .str.replace("'","",regex=False)
    .str.split()
    )
df["Student_emails"]=df["Other Names"].str[0].str.lower() + df["Surname"].str.lower() + "@gmail.com"
print(df)"""

import pandas as pd
import numpy

file_path = r"C:\Users\mwend\OneDrive\Desktop\test_files.xlsx"
df = pd.read_excel(file_path)


print(df.info())
df[["Surname", "Other Names"]] = df["Student Name"].str.split(",", expand=True)


df["Surname"] = (df["Surname"]
                 .astype(str)
                 .str.replace("'", "", regex=False)
                 .str.strip())
df["Other Names"] = (df["Other Names"]
                     .astype(str)
                     .str.replace("'", "", regex=False)
                     .str.strip())


df["Email Address"] = df["Other Names"].str[0].str.lower() + df["Surname"].str.lower() + "@gmail.com"
female_students=df[df["Gender"]=="F"]
male_students=df[df["Gender"]=="M"]
special_names=df["Student Name"]
print(female_students)
print(male_students)
print(df)
df.to_excel("C:Users/mwend/Downloads/Generated_Emails.xlsx", index=False)
df.to_csv("C:Users/mwend/Downloads/Generated_Emails.csv", index=False)
df.to_csv("C:Users/mwend/Downloads/Generated_Emails.tsv",sep='\t', index=False)

