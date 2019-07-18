from PIL import Image
import random
import math
 
def generate_voronoi_diagram(width, height): 
  image = Image.new("RGB", (width, height))
  putpixel = image.putpixel
  imgx, imgy = image.size
  nx = []
  ny = []
  nr = []
  ng = []
  nb = []

  nx = [20, 40, 40, 40, 40, 60, 60, 60, 60, 80, 80, 120, 120, 140, 140, 140, 140, 160, 160, 160, 160, 180]
  ny = [50, 20, 40, 60, 80, 20, 40, 60, 80, 40, 60, 40, 60, 20, 40, 60, 80, 20, 40, 60, 80, 50]


  nr = [215, 243, 230, 222, 200, 234, 210, 213, 213, 210, 213, 213, 214, 234, 234, 215, 243, 230, 222, 200, 234, 210, 213, 213, 210, 213, 213, 214, 234, 215]
  ng = [225, 233, 230, 200, 206, 213, 223, 245, 210, 213, 214, 214, 215, 234, 212, 225, 233, 230, 200, 206, 213, 223, 245, 210, 213, 214, 214, 215, 234, 225]
  nb = [215, 243, 210, 200, 100, 220, 235, 245, 210, 231, 234, 231, 234, 253, 213, 215, 243, 210, 200, 100, 220, 235, 245, 210, 231, 234, 231, 234, 253, 215]

  
  num_cells = len(nx)
    

  print(nx,"\n",ny)
  print(imgx, imgy)


  for y in range(imgy):
    for x in range(imgx):
      dmin = math.hypot(imgx, imgy)
      j = -1
      for i in range(num_cells):
        d = math.hypot(nx[i]-x, ny[i]-y)
        if d < dmin:
          dmin = d
          j = i
      putpixel((x, y), (nr[j], ng[j], nb[j]))

      for i in range(22):
         image.putpixel((nx[i],ny[i]), (0,0,0))

  image.save("VoronoiDiagram.png", "PNG")
  image.show()

 

if __name__== "__main__":
         generate_voronoi_diagram(200, 100)
