import cadquery as cq
from Helpers import show
# link: https://www.youtube.com/watch?v=NAK8JIZSjnE&ab_channel=ne1kncode
color = (   74, 35, 90 , 0.5 )

plane1 = cq.Workplane( "XY" )

(x,y) = p1 = ( 20 , 0 )
(x,y) = r1 = ( x+15 , y-15 )
(x,y) = r2 = (x-15 , y-15 )
(x,y) = p2 = (x-20 , y )

#block = plane1.lineTo( *p1 ).threePointArc( r1 , r2 ).lineTo( *p2 ).close()
#show(block)

block1 = plane1.lineTo( *p1 )
show(block1) # show() - hareketi ciz demek. show demezsek sadece diger bir cizginin baslangicini falan klavuzlamak icin hareket gibi oluyor


block2 = plane1.lineTo( *p1 ).threePointArc( r1 , r2 )
show(block2)