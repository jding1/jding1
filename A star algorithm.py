import copy
import random
def moveup(grid,index):
    counter=0
    newgrid=[]
    while counter<len(grid):
        newgrid.append(grid[counter])
        counter=counter+1
    item=newgrid[index]
    newindex=index-3
    otheritem=newgrid[newindex]
    newgrid[newindex]=item
    newgrid[index]=otheritem
    return newgrid
def movedown(grid,index):
    counter=0
    newgrid=[]
    while counter<len(grid):
        newgrid.append(grid[counter])
        counter=counter+1
    item=newgrid[index]
    newindex=index+3
    otheritem=newgrid[newindex]
    newgrid[newindex]=item
    newgrid[index]=otheritem
    return newgrid
def moveleft(grid,index):
    counter=0
    newgrid=[]
    while counter<len(grid):
        newgrid.append(grid[counter])
        counter=counter+1
    item=newgrid[index]
    newindex=index-1
    otheritem=newgrid[newindex]
    newgrid[newindex]=item
    newgrid[index]=otheritem
    return newgrid
def moveright(grid,index):
    counter=0
    newgrid=[]
    while counter<len(grid):
        newgrid.append(grid[counter])
        counter=counter+1
    item=newgrid[index]
    newindex=index+1
    otheritem=newgrid[newindex]
    newgrid[newindex]=item
    newgrid[index]=otheritem
    return newgrid
#using the A* search
#calculating heuristic
def calch(grid,end):
    h=0
    counter=0
    while counter<len(grid):
        if grid[counter]!=end[counter]:
            h=h+1
        counter=counter+1
    print(h)
    return h
#check what moves are availabe
def findavailable(grid,element,openlist,movesmade,f,closedlist):
    closedlist.append(grid)
    if element==0:
        new1=moveright(grid,element)
        newgridinclosed=checkinclosed(new1,closedlist)
        if newgridinclosed=="n":
            openlist.append(new1)
            h1=calch(new1,solution)
            f1=movesmade+h1
            f.append(f1)
        new2=movedown(grid,element)
        newgridinclosed=checkinclosed(new2,closedlist)
        if newgridinclosed=="n":
            openlist.append(new2)
            h2=calch(new2,solution)
            f2=movesmade+h2
            f.append(f2)
        minf=min(f)
        counter=0
        while counter<len(f):
            if f[counter]==minf:
                grid=openlist[counter]
                newgrid=copy.deepcopy(grid)
            counter=counter+1
    #add all the elements
    elif element==1:
        new1=moveright(grid,element)
        newgridinclosed=checkinclosed(new1,closedlist)
        if newgridinclosed=="n":
            openlist.append(new1)
            h1=calch(new1,solution)
            f1=movesmade+h1
            f.append(f1)
        new2=movedown(grid,element)
        newgridinclosed=checkinclosed(new2,closedlist)
        if newgridinclosed=="n":
            openlist.append(new2)
            h2=calch(new2,solution)
            f2=movesmade+h2
            f.append(f2)
        new3=moveleft(grid,element)
        newgridinclosed=checkinclosed(new3,closedlist)
        if newgridinclosed=="n":
            openlist.append(new3)
            h3=calch(new3,solution)
            f3=movesmade+h3
            f.append(f3)
        minf=min(f)
        counter=0
        while counter<len(f):
            if f[counter]==minf:
                grid=openlist[counter]
                newgrid=copy.deepcopy(grid)
            counter=counter+1
    elif element==2:
        new1=moveleft(grid,element)
        newgridinclosed=checkinclosed(new1,closedlist)
        if newgridinclosed=="n":
            openlist.append(new1)
            h1=calch(new1,solution)
            f1=movesmade+h1
            f.append(f1)
        new2=movedown(grid,element)
        newgridinclosed=checkinclosed(new2,closedlist)
        if newgridinclosed=="n":
            openlist.append(new2)
            h2=calch(new2,solution)
            f2=movesmade+h2
            f.append(f2)
        minf=min(f)
        counter=0
        while counter<len(f):
            if f[counter]==minf:
                grid=openlist[counter]
                newgrid=copy.deepcopy(grid)
            counter=counter+1
    elif element==3:
        new1=moveright(grid,element)
        newgridinclosed=checkinclosed(new1,closedlist)
        if newgridinclosed=="n":
            openlist.append(new1)
            h1=calch(new1,solution)
            f1=movesmade+h1
            f.append(f1)
        new2=movedown(grid,element)
        newgridinclosed=checkinclosed(new2,closedlist)
        if newgridinclosed=="n":
            openlist.append(new2)
            h2=calch(new2,solution)
            f2=movesmade+h2
            f.append(f2)
        new3=moveup(grid,element)
        newgridinclosed=checkinclosed(new3,closedlist)
        if newgridinclosed=="n":
            openlist.append(new3)
            h3=calch(new3,solution)
            f3=movesmade+h3
            f.append(f3)
        minf=min(f)
        counter=0
        while counter<len(f):
            if f[counter]==minf:
                grid=openlist[counter]
                newgrid=copy.deepcopy(grid)
            counter=counter+1
    elif element==4:
        new1=moveright(grid,element)
        newgridinclosed=checkinclosed(new1,closedlist)
        if newgridinclosed=="n":
            openlist.append(new1)
            h1=calch(new1,solution)
            f1=movesmade+h1
            f.append(f1)
        new2=movedown(grid,element)
        newgridinclosed=checkinclosed(new2,closedlist)
        if newgridinclosed=="n":
            openlist.append(new2)
            h2=calch(new2,solution)
            f2=movesmade+h2
            f.append(f2)
        new3=moveup(grid,element)
        newgridinclosed=checkinclosed(new3,closedlist)
        if newgridinclosed=="n":
            openlist.append(new3)
            h3=calch(new3,solution)
            f3=movesmade+h3
            f.append(f3)
        new4=moveleft(grid,element)
        newgridinclosed=checkinclosed(new4,closedlist)
        if newgridinclosed=="n":
            openlist.append(new4)
            h4=calch(new4,solution)
            f4=movesmade+h4
            f.append(f4)
        minf=min(f)
        counter=0
        while counter<len(f):
            if f[counter]==minf:
                grid=openlist[counter]
                newgrid=copy.deepcopy(grid)
            counter=counter+1
    elif element==5:
        new1=moveleft(grid,element)
        newgridinclosed=checkinclosed(new1,closedlist)
        if newgridinclosed=="n":
            openlist.append(new1)
            h1=calch(new1,solution)
            f1=movesmade+h1
            f.append(f1)
        new2=movedown(grid,element)
        newgridinclosed=checkinclosed(new2,closedlist)
        if newgridinclosed=="n":
            openlist.append(new2)
            h2=calch(new2,solution)
            f2=movesmade+h2
            f.append(f2)
        new3=moveup(grid,element)
        newgridinclosed=checkinclosed(new3,closedlist)
        if newgridinclosed=="n":
            openlist.append(new3)
            h3=calch(new3,solution)
            f3=movesmade+h3
            f.append(f3)
        minf=min(f)
        counter=0
        while counter<len(f):
            if f[counter]==minf:
                grid=openlist[counter]
                newgrid=copy.deepcopy(grid)
            counter=counter+1
    elif element==6:
        new1=moveright(grid,element)
        newgridinclosed=checkinclosed(new1,closedlist)
        if newgridinclosed=="n":
            openlist.append(new1)
            h1=calch(new1,solution)
            f1=movesmade+h1
            f.append(f1)
        new2=moveup(grid,element)
        newgridinclosed=checkinclosed(new2,closedlist)
        if newgridinclosed=="n":
            openlist.append(new2)
            h2=calch(new2,solution)
            f2=movesmade+h2
            f.append(f2)
        minf=min(f)
        counter=0
        while counter<len(f):
            if f[counter]==minf:
                grid=openlist[counter]
                newgrid=copy.deepcopy(grid)
            counter=counter+1
    elif element==7:
        new1=moveright(grid,element)
        newgridinclosed=checkinclosed(new1,closedlist)
        if newgridinclosed=="n":
            openlist.append(new1)
            h1=calch(new1,solution)
            f1=movesmade+h1
            f.append(f1)
        new2=moveleft(grid,element)
        newgridinclosed=checkinclosed(new2,closedlist)
        if newgridinclosed=="n":
            openlist.append(new2)
            h2=calch(new2,solution)
            f2=movesmade+h2
            f.append(f2)
        new3=moveup(grid,element)
        newgridinclosed=checkinclosed(new3,closedlist)
        if newgridinclosed=="n":
            openlist.append(new3)
            h3=calch(new3,solution)
            f3=movesmade+h3
            f.append(f3)
        minf=min(f)
        counter=0
        while counter<len(f):
            if f[counter]==minf:
                grid=openlist[counter]
                newgrid=copy.deepcopy(grid)
            counter=counter+1
    elif element==8:
        new1=moveleft(grid,element)
        newgridinclosed=checkinclosed(new1,closedlist)
        if newgridinclosed=="n":
            openlist.append(new1)
            h1=calch(new1,solution)
            f1=movesmade+h1
            f.append(f1)
        new2=moveup(grid,element)
        newgridinclosed=checkinclosed(new2,closedlist)
        if newgridinclosed=="n":
            openlist.append(new2)
            h2=calch(new2,solution)
            f2=movesmade+h2
            f.append(f2)
        minf=min(f)
        counter=0
        while counter<len(f):
            if f[counter]==minf:
                grid=openlist[counter]
                newgrid=copy.deepcopy(grid)
            counter=counter+1
    return newgrid
#check if result of move is in closed list
def checkinclosed(grid,closedlist):
    gridinclosed="n"
    counter=0
    while counter<len(closedlist):
        if grid==closedlist[counter]:
            gridinclosed="y"
        else:
            gridinclosed="n"
        counter=counter+1
    return gridinclosed
#if it is then don't make the move, else: it remains in open list 


#main program
solution=[1,2,3,4,5,6,7,8,"*"]
li=["*",2,3,1,4,6,7,5,8]
newlist=copy.deepcopy(li)
closedli=[]
openli=[]
fx=[]
loopdone=0
moves=1
while loopdone==0:
    counter=0
    while counter<len(newlist):
        number=newlist[counter]
        if number=="*":
            element=counter
        counter=counter+1
    heuristic=calch(newlist,solution)
    if heuristic==0:
        loopdone=1
    else:
        newlist=findavailable(newlist,element,openli,moves,fx,closedli)
        print(newlist)
        moves=moves+1

