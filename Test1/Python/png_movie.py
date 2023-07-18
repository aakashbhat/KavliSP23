import os
import imageio

directory="/userdata/data/bhat/D6/KavliSP23/Test_Ni/Long_Evolve/png"

output_file="/userdata/data/bhat/D6/KavliSP23/Test1/Long_Evolve/png/movie.mp4"

files = sorted([file for file in os.listdir(directory) if file.endswith('.png')])

frames=[]

for file in files:
    file_path=os.path.join(directory,file)
    image=imageio.imread(file_path)
    frames.append(image)

imageio.mimsave(output_file,frames,fps=20)

