import os
import imageio

directory="/userdata/data/bhat/D6/KavliSP23/Test_Ni_Opacity/Long_Evolve_Ni_opacity_massloss-10_7K/png/"

output_file="/userdata/data/bhat/D6/KavliSP23/Test_Ni_Opacity/Long_Evolve_Ni_opacity_massloss-10_7K/png/movie.mp4"

files = sorted([file for file in os.listdir(directory) if file.endswith('.png')])

frames=[]

for file in files:
    file_path=os.path.join(directory,file)
    image=imageio.imread(file_path)
    frames.append(image)

imageio.mimsave(output_file,frames,fps=10)

