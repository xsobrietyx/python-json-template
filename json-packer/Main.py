import json_templates
import json

json_tmp = json_templates.JsonTemplates()
res = json_tmp.load("../resources/Template.json")

if res[0]:
    new_dict = json_tmp.generate({"f_name": "Something that we need to paste", "s_name": "Variable to replace #2"})
    with open('../outputs/data.json', 'w') as f:
        json.dump(new_dict[1], f)