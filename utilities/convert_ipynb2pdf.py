import glob
import subprocess

home = '/home/mrrobot/Documents/GitHub/AEM-ITESO/'
# home = '/home/mrrobot/GitHub/AEM-ITESO/'
jupyter_list = glob.glob(home + '/*/*.ipynb')
for item in jupyter_list:
    command = 'quarto render ' + item
    subprocess.call(command, shell=True)
    new_name = item.replace('.ipynb', '_code_only.ipynb')
    # remove_markdown_cells(item, new_name)
    print(item)
