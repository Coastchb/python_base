mouth_related_feat = ["jawforward",
"mouthleft" ,
"mouthfrownleft",
"jawopen",
"mouthstretchright",
"browouterupright",
"mouthdimpleright",
"mouthstretchleft" ,
"mouthsmileleft",
"mouthupperupright",
"mouthfunnel",
"jawleft",
"mouthsmileright",
"mouthclose",
"mouthdimpleleft",
"mouthlowerdownleft",
"mouthright" ,
"mouthupperupleft" ,
"jawright" ,
"mouthlowerdownright" ,
"mouthfrownright"]

import json
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

def feat_to_json(file_path, feat):
    blendshape_dict = {}
    for (feat_name, feat_value) in zip(mouth_related_feat, feat):
        blendshape_dict[feat_name] = feat_value
    frame_dict = {"blendshape": blendshape_dict}
    print(frame_dict)
    frame_str = json.dumps(frame_dict, cls=NpEncoder)
    print(frame_str)
    with open(file_path,"w") as fd:
        #json.dump(frame_dict, fd)
        fd.write(frame_str)

if __name__ == "__main__":
    feat = np.arange(21)
    feat_to_json("aaa.json", feat)