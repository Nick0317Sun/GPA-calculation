"""
    Converting Jialin's undergraduate academic records to 4-point scale GPA
"""

import pandas as pd
import numpy as np

if __name__ == "__main__":
    print('================================================')
    # all courses included
    df_allCourse = pd.read_excel(r'GPA raw data/GPA_convert_worksheet_allCourses.xlsx')
    credits = df_allCourse['Credit'].values
    grades = df_allCourse['4.0 Scale'].values
    total_quality_points = np.sum(credits * grades)
    gpa = total_quality_points / np.sum(credits)

    df_copy = df_allCourse.copy(deep=True)
    df_copy['Score'] = df_copy.apply(lambda row: row['Letter grade to mark'] if isinstance(row['Score'], str) else row['Score'], axis=1)
    df_copy['Score'] = pd.to_numeric(df_copy['Score'], errors='coerce')
    mean_score = df_copy['Score'].mean()
    
    print(f'Undergraduate Cumulative GPA (all courses included):\n4-point scale: {gpa:.2f}/4.0\n100-percent scale: {mean_score:.2f}/100')

    print('================================================')

    # only compulsory courses
    df_compulsory = pd.read_excel(r'GPA raw data/GPA_convert_worksheet_compulsory.xlsx')
    credits = df_compulsory['Credit'].values
    grades = df_compulsory['4.0 Scale'].values
    total_quality_points = np.sum(credits * grades)
    gpa = total_quality_points / np.sum(credits)

    df_copy = df_compulsory.copy(deep=True)
    df_copy['Score'] = df_copy.apply(lambda row: row['Letter grade to mark'] if isinstance(row['Score'], str) else row['Score'], axis=1)
    df_copy['Score'] = pd.to_numeric(df_copy['Score'], errors='coerce')
    mean_score = df_copy['Score'].mean()
    
    print(f'Undergraduate Cumulative GPA (compulsory courses only):\n4-point scale: {gpa:.2f}/4.0\n100-percent scale: {mean_score:.2f}/100')
    print('================================================')
