import json_templates
import json
import os
from mapping import mappings

json_tmp = json_templates.JsonTemplates()
res = json_tmp.load("../resources/Template.json")

set_of_folders = {"prod", "dev"}
root_output_folder = "../outputs"


def create_dir_if_not_exist():
    if not os.path.exists(root_output_folder):
        os.mkdir(root_output_folder)
        print("Directory '% s' created" % root_output_folder)
    for p in set_of_folders:
        path = os.path.join(os.getcwd(), root_output_folder, p)
        if not os.path.exists(path):
            os.mkdir(path)
            print("Directory '% s' created" % path)


def generate_json_objects(json_res):
    file_name = "data.json"
    if json_res[0]:
        for k in mappings.keys():
            if k in set_of_folders:
                set_of_folders.remove(k)
                new_dict = json_tmp.generate(
                    {"f_name": mappings.get(k).get("f_name"), "s_name": mappings.get(k).get("s_name")})
                file_path = os.path.join(os.getcwd(), root_output_folder, k) + "/" + file_name
                with open(file_path, 'w') as f:
                    json.dump(new_dict[1], f)
                    print("File '% s' created" % file_path)


create_dir_if_not_exist()
generate_json_objects(res)