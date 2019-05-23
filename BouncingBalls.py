def bouncingBall(h, bounce, window):
  count = 0
  i = 0
  if ( window<0 or h<=0 or window>=h or bounce >= 1 or bounce<=0):
       return -1 
  else: 
   while h > window:
    count = count + 1
    h = h * bounce
    if(h > window):
      count = count + 1
  return count
       
