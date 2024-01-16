# This is the Rust code that was compiled and exposed via Python shim
import mesh

node = hou.pwd()
geo = node.geometry()

# This is to make the demo easy to test out performance with slider changing values
n_stacks = node.parm("stacks").eval()
n_slices = node.parm("slices").eval()

# This is the actual call to the underlying Rust function
data = mesh.uv_sphere(n_stacks, n_slices)

# Process the data that was return from Rust that has been Pythonified via the shim
fverts = data['fverts']
nverts = data['nverts']
verts = data['verts']

# For now, I only know how to deal with simple list rather than list of objects
num_points = len(verts) // 3

points = []
for i in range(num_points):
    x = verts[i*3]
    y = verts[i*3+1]
    z = verts[i*3+2]
    points.append(geo.createPoint())
    points[-1].setPosition((x, y, z))
    
offset = 0
for vert_count in nverts:
    poly = geo.createPolygon()
    for i in range(vert_count):
        index = fverts[offset]
        poly.addVertex(points[index])
        offset += 1
