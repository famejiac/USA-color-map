# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 08:14:37 2024

@author: famej
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(15000)


def loag_image(image_name: str)-> list:
    """Loads the image located at the given path.  
    Parameters:  
        ruta_imagen (str): Path to the image to be loaded.  
    Returns:  
        list: Matrix (M, N, 3) representing the loaded image.  
    """
    image = mpimg.imread(image_name).tolist()
    return image

def turn_black_white(image:list)->list:
    """
    Transforms the image colors to black and white based on a range of 200 to 270 for light tones, with the rest set to black.  
    Parameters  
    ----------  
    image : list  
        List containing the image colors in RGB.  
    Returns  
    -------  
    image : list  
        Black and white version of the image.  
    """

    for linea in range(0,len(image)):
        for pixel in range(0,len(image[linea])):
            for color in range(0,len(image[linea][pixel])):
                if image[linea][pixel][color] in range(200, 270):
                    image[linea][pixel][color] = 255
                else:
                    image[linea][pixel][color] = 0
    return image

def visualize_image(img: list)->None:
    """Displays the given image.  
    Parameters:  
        img (list): Matrix (M, N, 3) representing the image to display.  
    """
    plt.imshow(img)
    plt.show()

#Here we test the functions so we know that the file is being imported correctly
#Also we visualice the image
    
image = loag_image("USA.jpg")
image = turn_black_white(image)
visualize_image(image)
        
def color1(coordenates, img):
    """
    This function is going to help pinpoint where in the map is each state
    to create a dict storing the location in the map of each state

    Parameters
    ----------
    coordenates : tuple
        These coordenates are going to be inputed by the user so
        it can be visualized where in the map we are standing in order to
        create a dictionary of states that store the coordenates of themselfs.
    img : list
        map of the country we want to color.

    Returns
    -------
    img : list
        colored point in the map so the user can determine if its locating
        correctly each coordinate.

    """
    for i in range(coordenates[0]-3, coordenates[0]+4):
        for j in range(coordenates[1]-3, coordenates[1]+4):
            img[i][j] = [255, 0, 0]
    return img


#Here we use the function color to pinpoint each state in the map 
#and the we create the dict of states. Note that some states have more
#than one set of coordenates, this is because in the map they apear separated.
#we change the coordenates as much as needed to find the correct coordenates 
#of each state    

image2 = loag_image("USA.jpg")
image2 = turn_black_white(image2)

image2 = color1((270, 255), image2)

visualize_image(image2)
image2 = loag_image("USA.jpg")
image2 = turn_black_white(image2)

#This dictionary is only for this map. It needs to be built for each 
#image that is used.
states_coordenates = {"washington": [(110, 250)],
                      "oregon": [(170, 220)],
                      "california": [(330, 200)],
                      "nevada": [(270, 255)],
                      "utah": [(290, 330)],
                       "arizona": [(380, 310)],
                       "new mexico": [(390, 395)],
                       "texas": [(450, 500)],
                       "alaska": [(565, 280), (660, 485)],
                       "colorado": [(310, 415)],
                       "kansas": [(330, 525)],
                       "missouri": [(330, 610)],
                       "oklahoma": [(390, 540)],
                       "arkansas": [(400, 610)],
                       "louisiana": [(465, 615)],
                       "mississippi": [(440, 660)],
                       "idaho": [(200, 310)],
                       "montana": [(150, 380)],
                       "wyoming": [(235, 395)],
                       "north dakota": [(155, 505)],
                       "south dakota": [(210, 505)],
                       "nebraska": [(270, 505)],
                       "minesota": [(180, 585)],
                       "iowa": [(260, 600)],
                       "wisconsin": [(210, 645)],
                       "michigan": [(235, 725),(180, 670)],
                       "ilinois": [(300, 655)],
                       "indiana": [(300, 705)],
                       "ohio": [(295, 755)],
                       "pennsylvania": [(270, 820)],
                       "new york": [(215, 850)],
                       "vermont": [(190, 880)],
                       "new hampshire": [(196, 900)],
                       "maine": [(155, 920)],
                       "kentucky": [(345, 725)],
                       "tennessee": [(380, 715)],
                       "alabama": [(435, 710)],
                       "georgia": [(435, 765)],
                       "florida": [(530, 805)],
                       "south carolina": [(410, 805)],
                       "north carolina": [(370, 820)],
                       "virginia": [(330, 820)],
                       "west virginia": [(315, 790)],
                       "maryland": [(297, 811), (297, 847), (305, 867)],
                       "delaware": [(297, 871)],
                       "new jersey": [(270, 875)],
                       "connecticut": [(235, 900)],
                       "rhode island": [(231, 912)],
                       "massachusetts": [(215, 910)]
                       }


#Flood fill
#This is how we are going to color each state in the map.
# the flood fill function works like paint flood fill. it oly stops once
#it finds that all the pixels within the limits are of the new color

def floodfill(img, y, x, old_color, new_color):
    """
    Fill each state based on the coordenates

    Parameters
    ----------
    img : str
        Map that is being used.
    y : int
        y coordenate.
    x : int
        x coordenate.
    old_color : list
        initial color that we want to modify.
    new_color : list
        final color that you want the state to be.

    Returns
    -------
    None.

    """
    #"hidden" stop clause - not reinvoking for "c" or "b", only for "a".
    if img[y][x] == old_color:  
        img[y][x] = new_color 
        #recursively invoke flood fill on all surrounding cells:
        if y > 0:
            floodfill(img, y-1, x, old_color, new_color)
        if y < len(img) - 1:
            floodfill(img, y+1, x, old_color, new_color)
        if x > 0:
            floodfill(img, y, x-1, old_color, new_color)
        if x < len(img[y]) - 1:
            floodfill(img, y, x+1, old_color, new_color)

#this function colors each state of red so you can visualize if every part of 
#the map is being colored as you want. If you want to cadjust the coloring,
#the state dict needs to be adjusted.
def test_flood_fill(img, coordenates):
    for i in coordenates:
        for j in coordenates[i]:
            y = j[0]
            x = j[1]
            floodfill(img, y , x, [255, 255, 255], [255, 0, 0])
    visualize_image(img)
    
test_flood_fill(image2, states_coordenates)



    

            
