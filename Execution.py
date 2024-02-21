from PictureRepair_CodeFormer import PictureRepair


def main(min_scale = 1, max_scale = 4):
    # please enter your specified folder path and name
    repair_path = 'C:\\Users\\user_name\\Desktop'
    repair_folder = 'input'
    repair_result_folder = 'output'
    CodeFormer_path = 'C:\\Users\\user_name\\CodeFormer'

    n = max_scale + 1
    while n > max_scale:
        n = int(input(f"Repair scalar({min_scale}-{max_scale}):"))
        if min_scale <= n <= max_scale:
            p = PictureRepair(n, repair_path, repair_folder, repair_result_folder, CodeFormer_path)
            p.Executable()
            print("Repair success!")
        elif n < min_scale:
            print("Exit")
        else:
            print('Too large, please enter available scale.\n')

main()
