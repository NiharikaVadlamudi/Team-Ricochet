import cv2
import os

list_main=open('list.txt','r')
print("before")
for image in list_main.readlines():
    # print("in loop")
    # print(image.strip('\n'))
    c=image.strip('\n')
    img=cv2.imread("Images/"+str(c),0)
    Y=img.shape[0]
    X=img.shape[1]
    file=image.replace('.jpg','.txt')
    file=file.strip('\n')
    print(file)
    g=open('new.txt','w')
    text_file=open('Labels_old/'+file,'r')
    for line in text_file:
        l=line.strip('\n')
        a,xt,yt,xb,yb = l.split(' ')
        xo=(float(xt)+float(xb))/2

        yo=(float(yt)+float(yb))/2
        w=abs(float(xt)-float(xb))
        h=abs(float(yt)-float(yb))
        g.write(str(1)+' '+str(xo/X)+' '+str(yo/Y)+' '+str(w/X)+' '+str(h/Y)+ "\n")
    
    g.close()

    g=open('new.txt','r')
    h=open('Labels_new/'+file,'w')
    for i in g:
        h.write(i)

    h.close()


    



