import glob
import subprocess
# import nbformat

# def remove_markdown_cells(input_notebook, output_notebook):
#     # Load the notebook
#     with open(input_notebook, 'r') as f:
#         nb = nbformat.read(f, as_version=4)

#     # Filter out markdown cells
#     nb.cells = [cell for cell in nb.cells if cell.cell_type != 'markdown']

#     # Save the modified notebook
#     with open(output_notebook, 'w') as f:
#         nbformat.write(nb, f)


home = '/home/mrrobot/Documents/GitHub/AEM-ITESO/tema_2'
# home = '/home/mrrobot/GitHub/AEM-ITESO/'
jupyter_list = glob.glob(home + '/*/*.ipynb')
for item in jupyter_list:
    command = 'quarto render ' + item
    subprocess.call(command, shell=True)
    new_name = item.replace('.ipynb', '_code_only.ipynb')
    # remove_markdown_cells(item, new_name)
    print(item)
