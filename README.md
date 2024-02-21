# Personalized-execution-of-codeformer
You can choose your own folder to run CodeFormer and specify the folder to store the repair results.


First, download the CodeFormer program, and make sure to install the required packages listed in requirements.txt.
 - URL: https://github.com/sczhou/CodeFormer

Second, you must set your specified folder in order to run CodeFormer:
- "repair_path" is the path of your input folder and result folder.
- "repair_folder" is the folder where you want to save the pictures you want to repair.
- "repair_result_folder" is the folder where you want to save the results of the pictures after they have been repaired by CodeFormer.
- "CodeFormer_path" is the path of the main program of CodeFormer.

If you want to set the Enhancements, you need to check the README.md of CodeFormer. Then, you can modify your settings in PictureRepair_CodeFormer.py.

After completing your settings, place the pictures you want to repair into the "repair_folder".

Finally, execute the program Execution.py to obtain the pictures after they have been repaired.
