import os

caminho_pasta = str(input('Digite o caminho: '))

os.chdir(caminho_pasta)
# os.chdir troca o diretório no qual o python vai trabalhar

for f in os.listdir():
    file_name, f_ext = os.path.splitext(f)

    f_hot, f_num, f_nome, f_hd = file_name.split('-')

    f_num = f_num.strip()
    f_nome = f_nome.strip()
    f_ext = f_ext.strip()

    new_name = (f'{f_num}-{f_nome}{f_ext}')

    os.rename(f, new_name)
