import os
import shutil


class PictureRepair():
    def __init__(self, n, repair_path, repair_folder, repair_result_folder, CodeFormer_path):
        self.n = n
        self.main_folder = CodeFormer_path
        self.executable = 'inference_codeformer.py'
        self.background = '--bg_upsampler realesrgan '
        self.face = '--face_upsample '
        self.weight = 0.7

        self.repair_path = repair_path
        self.repair_folder = repair_folder
        self.repair_result_folder = repair_result_folder

    def Paths(self):
        self.path = os.path.join(self.repair_path, self.repair_folder)
        self.name_txt_path = os.path.join(self.repair_path, self.repair_folder + "_names.txt")
        self.codeformer_result_path = '{}/results/{}_{}/final_results'.format(self.main_folder, self.repair_folder, self.weight)
        self.repair_result_path = os.path.join(self.repair_path, self.repair_result_folder)
                
    def Executable(self):
        self.Paths()
        print("Available paths")

        self.SaveImgName()
        print('Save Name success!')

        self.RenameImgInOrder()
        print('Reorder success, available to run CodeFormer.')

        print("\n-------- Running CodeFormer... --------")
        self.Executable_CodeFormer()
        print('-------- Repair complete --------\n')

        self.RestoreImgName(self.name_txt_path, self.codeformer_result_path)
        self.RestoreImgName(self.name_txt_path, self.path)
        print('Restore files name complete!')
        
        self.MoveResultsToSpecifiedFolder(self.codeformer_result_path, self.repair_result_path)
        print('Move to specified folder success!')

    def Executable_CodeFormer(self):
        os.chdir(self.main_folder)
        os.system(f'python {self.executable} -w 0.7 --input_path {self.path} {self.background}{self.face}--upscale {self.n}')
        

    def SaveImgName(self):
        if os.path.exists(self.name_txt_path):
            os.remove(self.name_txt_path)

        with open(self.name_txt_path, 'w', encoding='utf-8') as f:
            for file in os.listdir(self.path):
                file_name, _ = os.path.splitext(file)
                f.write(file_name + '\n')

    def RenameImgInOrder(self):
        folder_path = r"{}".format(self.path)
        count = 0
        
        for file in os.listdir(folder_path):
            _, file_extension = os.path.splitext(file)
            new_filename = f"{count:03}{file_extension}"
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_filename)        
            os.rename(old_path, new_path)
            count += 1
                
    def RestoreImgName(self, name_txt_path, folder_path):
        with open(name_txt_path, 'r', encoding='utf-8') as f:
            new_names = f.read().splitlines()        
        for i, file in enumerate(os.listdir(folder_path)):
            file_path = os.path.join(folder_path, file)
            _, file_extension = os.path.splitext(file)
            new_name = new_names[i] + file_extension
            new_file_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_file_path)


    def MoveResultsToSpecifiedFolder(self, previous_path, after_move_path):
        if not os.path.exists(after_move_path):
            os.makedirs(after_move_path)
        for filename in os.listdir(previous_path):
            source_file = os.path.join(previous_path, filename)
            destination_file = os.path.join(after_move_path, filename)
            if os.path.exists(destination_file):
                filename, file_extension = os.path.splitext(filename)
                while True:
                    new_filename = f"{filename}_copy{file_extension}"
                    destination_file = os.path.join(after_move_path, new_filename)
                    if not os.path.exists(destination_file):
                        break
            shutil.move(source_file, destination_file)
        
