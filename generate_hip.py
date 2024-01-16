import hou

obj = hou.node("/obj")
geo_node = obj.createNode("geo", run_init_scripts=False)
python_node = geo_node.createNode("python")

with open('python_sop_content.py') as f:
    python_sop_script = f.read()
    python_node.parm('python').set(python_sop_script)
    g = python_node.parmTemplateGroup()
    slices = hou.IntParmTemplate(name='slices', label='Slices', num_components=1, default_value=[
                                 8], min=3, max=100, min_is_strict=True)
    stacks = hou.IntParmTemplate(name='stacks', label='Stacks', num_components=1, default_value=[
                                 8], min=3, max=100, min_is_strict=True)
    g.append(slices)
    g.append(stacks)
    python_node.setParmTemplateGroup(g)


hou.hipFile.save(file_name='test_rusty.hip')
