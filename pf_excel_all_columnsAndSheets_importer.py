# a program that reads two columsn of two xlsx in alternation, copy and \
# copy and pasting each cell of each row in two seperate /txt files


def xlsx_importerAndScout(file_path):
    """

    Parameters
    ----------
    file_path : STR
        Imports a excel file with multiple sheets stores in DICT
            Removes the first row of a sheet
            resets the index

    Returns
    -------
    DIC
        A dictionary of dataframes.

    """
    import pandas as pd
    sheet_to_df_map = pd.read_excel(file_path, sheet_name=None) # store in DIC
    print()
    
    
    for key in sheet_to_df_map.keys():
        sheet_to_df_map[key].columns = range(sheet_to_df_map[key].shape[1]) # # remove the comment on the first line (you cant remove column names, only reset them by range with shape:)
        sheet_to_df_map[key].columns = sheet_to_df_map[key].iloc[0] # change column names to the first row
        sheet_to_df_map[key] =  sheet_to_df_map[key].iloc[1:] # drop the first row
        sheet_to_df_map[key] =  sheet_to_df_map[key].reset_index(drop=True) # reset index (0th is back):
        
    print('\n Hereunder are the outputted text file(s) corresponding to each sheet in the xls* file:')
    for key in sheet_to_df_map.keys():
        try:
            df = sheet_to_df_map[key]
            file_name = key.replace(" ", "_")
            with open(f'/home/siebe.albers/dev/TN_w_IRISA/ATN_input/{file_name}.txt', 'w') as f:
                # writing the columns names on the first line of the text file:
                columns = "" 
                # & delimit the column names, for conversion to xlsx later:
                for column in list(df.columns):
                    columns+=str(column) + " DELIMITER "
                if columns[-10:] == 'DELIMITER ':
                    columns = columns[:-10]
                f.writelines(columns+"\n")
                
            # determining how many columns (strings) are in a row:
            
                for i in range(0,len(df)):
                    df.iloc[i].shape[0]
                    # concat the columns(stings):
                    string_concatted = ""
                    for string in df.iloc[i]:
                        string_concatted += str(string) + " DELIMITER "
                        # TODO dirty remove the last 'DELEIMITER'
                    if string_concatted[-10:] == 'DELIMITER ':
                        string_concatted = string_concatted[:-10]
                            
                
                    if type(string_concatted) == str:
                        # print(i, string_concatted)
                        # some indices, such as #87 are not capped (also not for the manually normalized)
                        # string_concatted = string_concatted.capitalize()
                        # some strings have '\n', causes them to be printed on a seperate line in the txt file
                        string_concatted = string_concatted.replace("\n", "")
                        f.writelines(string_concatted)
                        f.write('\n')
                    else:
                        string_concatted = 'EMPTYROW'
                        f.writelines(string_concatted)
                        f.write('\n')
        except TypeError:
            print(f"exceptions: sheet: {sheet}")
        
        print(f' \n /home/siebe.albers/dev/TN_w_IRISA/ATN_input/{file_name}.txt')
    
    return sheet_to_df_map  # return the df for importer()


                
# %%
if __name__ == '__main__':
    import pandas as pd

    # printing the xlsx files in the dir, for user input convenience
    import glob
    import os
    os.chdir(os.getcwd())
    try:
        os.chdir("EXCEL_files")
    except FileNotFoundError:
        pass
    
    print(f'\n pwd == {os.getcwd()}')
    for file in glob.glob("*.xls*"):
        print(file)
        
    if len(glob.glob("*.xls*")) ==1:
        answer = input(f'is this the file you want to process? : \n {file} [y/n] \n')
        if answer.lower() in ['y', 'yes']:
            file_path = file
    else:
        file_path = input("input the file path to the xlsx file ")

    # if file_path.endswith((".xls")):
    #     import xlrd
    #     xls_file = xlrd.open_workbook_xls(file_path)
    #     print()
    #     sheets = xls_file.sheet_names()
    #     for sheet in sheets: print(sheet)
 
    
    dicc = xlsx_importerAndScout(file_path)  # !!! FUNCTION












    # # printing out the columns if there are more than 1 (i.e. there is not a comment on first line)
    # if len(df.columns) >1:
    #     for i, column in enumerate(df.columns):
    #         print(i, column)
    # index = int(input("\nInput the index-number of the column you want to process (starting at 0) "))
    # # index = 4

    # # df = indexSelector( # !!! FUNCTION
    # #     df,
    # #     sheet_name,
    # #     index)

    # output_file_name = "none"
    # while output_file_name.lower() not in ['atn', 'gs', 'other']:
    #     output_file_name = input(
    #         '\nspecify whether you want to process the sentences for automatic transcript normalization (ATN) or the already normalized sentences that will serve as the goldstandard sentences (GS) or OTHER  ')  # dep
    #     if output_file_name.lower() == 'atn':
    #         exporter('ATN.txt') # !!! FUNCTION
    #         print('saved under "ATN.txt" ')
    #     elif output_file_name.lower() == 'gs':
    #         sheet_name = sheet_name.replace(" ", "_")
    #         exporter(f'goldStandard_{sheet_name}_tts.txt')
    #         print(f'saved under "goldStandard_{sheet_name}_tts.txt" ')
    #     elif output_file_name.lower() == 'other':
    #         file_name_other = str(
    #             input('specify the name of your output_file, without extension \n'))
    #         exporter(f'{file_name_other}.txt')
    #         print(f'saved under "{file_name_other}.txt" ')
    #     else:
    #         print(' specify either "ATN" or GS" ')