import os
import imageio

directory="/userdata/data/bhat/D6/KavliSP23/Test_Ni_Opacity/Long_Evolve_Ni/png/"

output_file="/userdata/data/bhat/D6/KavliSP23/Test_Ni_Opacity/Long_Evolve_Ni/png/movie_5he4_1,2_newnetwork_lateopacties.mp4"

files = sorted([file for file in os.listdir(directory) if file.endswith('.png')])

frames=[]

for file in files:
    file_path=os.path.join(directory,file)
    image=imageio.imread(file_path)
    frames.append(image)

imageio.mimsave(output_file,frames,fps=20)

