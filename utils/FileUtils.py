import os
from pathlib import Path
import pytest
import pandas as pd

def get_csv_data(file_name, test_name):
    df = pd.DataFrame()
    try:
        file_path = Path(__file__).parent.parent / "data" / f"{file_name}.csv"
        # file_path = Path(__file__).parent.parent / "data" / "employee.csv"  ##is not working
        # file_path = "/Users/venug/PycharmProjects/pytestproj/data/employee.csv"
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            print(df)
    except FileNotFoundError as e:
        print(e)
    except Exception as exp:
        pytest.fail(str(exp), pytrace=False)
    if df is None:
        return None
    return df[df["Name"]==test_name].to_dict(orient="records")


def get_excel_data(file_name, test_name, sheet_name):
    df = pd.DataFrame()
    try:
        # file_path = "/Users/venug/PycharmProjects/pytestproj/data/data.xlsx"
        # file_path = Path(__file__).parent.parent / "data" / f"{file_name}.xlsx"
        file_path = "/Users/venug/Desktop/playwrightfrm/automation-framework/data/employee_data.xlsx"

        if os.path.exists(file_path):
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            print(df)
    except FileNotFoundError as e:
        print(e)
    except Exception as exp:
        pytest.fail(str(exp), pytrace=False)
    if df is None:
        return None
    return df[df["ID"]==test_name].to_dict(orient="records")

def get_excel_data_return_df(file_name, test_name, sheet_name):
    df = pd.DataFrame()
    try:
        # file_path = "/Users/venug/PycharmProjects/pytestproj/data/data.xlsx"
        file_path = Path(__file__).parent.parent / "data" / f"{file_name}.xlsx"

        if os.path.exists(file_path):
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            print(df)
    except FileNotFoundError as e:
        print(e)
    except Exception as exp:
        pytest.fail(str(exp), pytrace=False)
    if df is None:
        return None
    return df[df["ID"]==test_name]