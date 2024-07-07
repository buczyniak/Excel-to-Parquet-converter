# import pyarrow
import pandas as pd
import glob


def merge_excel_to_parquet(excel_files_path_pattern, output_parquet_file):
    # Find all Excel files matching the pattern
    excel_files = glob.glob(excel_files_path_pattern)

    # Read and concatenate all Excel files into a single DataFrame
    df_list = [pd.read_excel(file) for file in excel_files]
    merged_df = pd.concat(df_list, ignore_index=True)

    # Write the merged DataFrame to a Parquet file
    merged_df.to_parquet(output_parquet_file, index=False, engine='pyarrow')


merge_excel_to_parquet('*.xlsx', 'merged_file.parquet')
