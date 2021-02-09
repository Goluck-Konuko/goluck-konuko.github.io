import glob
import numpy as np
import imageio

vids = sorted(glob.glob("*.mp4"))

all_vids = []
for v in range(len(vids)):
    if v == 0:
        all_vids = imageio.mimread(vids[v], memtest=False)[:100]
    else:
        co = imageio.mimread(vids[v], memtest=False)
        try:
            composite = []
            for f in range(100):
                frame = np.concatenate((all_vids[f], co[f]), axis=0)
                composite.append(frame)
            all_vids = composite
        except:
            pass
        
imageio.mimsave("all_comp_xiph.mp4", all_vids, fps=15)


    

