def pasuti_tkreklus(skaits, apdruka, piegade):
 cenas = {"teksts":5, "zime":7, "foto":20}
 
 apdruka_vert = cenas[apdruka] * skaits
 
 while piegade:
   if apdruka_vert < 50:
    return apdruka_vert + 15
 
   elif apdruka_vert > 100:
    return apdruka_vert * 0.05
  
   else:
    return apdruka_vert
 
   else:
     if apdruka_vert <=100
     return apdruka_vert * 0.5
pasuti_tkreklus(6, "teksts", False)